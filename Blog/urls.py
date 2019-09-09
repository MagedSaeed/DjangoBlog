from django.urls import path
from django.contrib import admin
from .views import PostListView, PostDetailView, PostCreateView

from . import views
app_name = 'Blog'
urlpatterns = [
    # path('', views.home, name="blog-home"),
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('about/', views.about, name="blog-about"),

]
