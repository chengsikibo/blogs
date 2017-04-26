# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blogs/post_list.html', {'posts':posts})
