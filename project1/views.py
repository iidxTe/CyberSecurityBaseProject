from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import Blog

import datetime

import sqlite3

@login_required
def index(request):
    blog_list = Blog.objects.order_by('-pub_date')
    current_user = request.user
    context = {'blog_list': blog_list, 'user': current_user}
    
    return render(request, 'project1/index.html', context)

def findPost(request):
    conn = sqlite3.connect('db.sqlite3')
    query = request.POST.get('find_post')
    sql = f"SELECT * FROM project1_blog WHERE blog_header LIKE '%{query}%';"
    conn.execute(sql)
    conn.close()

    blog_list = Blog.objects.order_by('-pub_date')
    current_user = request.user
    context = {'blog_list': blog_list, 'user': current_user}
    return render(request, 'project1/index.html', context) 
    
@login_required
def showPost(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'project1/showPost.html', {'blog': blog})

@login_required
def showInfo(request, username):
    current_user = User.objects.get(username=username)
    return render(request, 'project1/showInfo.html', {'user': current_user})

@login_required
def addPost(request):
    if request.method == "POST":
        blog_owner = request.user
        blog_header = request.POST.get('header')
        blog_text = request.POST.get('text')
        Blog.objects.create(blog_owner=blog_owner, blog_header=blog_header, blog_text=blog_text, pub_date=datetime.datetime.now())
        return redirect('/project1/')

    return render(request, 'project1/addPost.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create_user(username=username, password=password)
        return redirect('signin')
    else: 
        return render(request, 'project1/register.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/project1/')

    return render(request, 'project1/signin.html')

def signout(request):
    logout(request)
    return redirect('signin')



