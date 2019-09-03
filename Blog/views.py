from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'MS-World',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'Aug 27, 2018'
    }
]


# Create your views here.

def home(request):
    context = {
        'title': 'this title is to test titles',
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
