from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.showPost, name='showPost'),
    path('<str:username>/', views.showInfo, name='showInfo'),
    path('register', views.register, name='register'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('addPost', views.addPost, name='addPost'),
    path('findPost', views.findPost, name='findPost')
]