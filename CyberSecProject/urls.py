from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('project1/', include('project1.urls')),
    path('admin/', admin.site.urls),
]
