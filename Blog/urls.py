from django.urls import path
from django.contrib import admin

from . import views
app_name = 'Blog'
urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about")
]
