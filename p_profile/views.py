from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, Post
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PostSerializer, ProfileSerializer
import datetime as dt
from . forms import ProfileForm, PostForm

def index(request):
    date =dt.date.today()
    posts = Post.objects.all()
    return render(request, 'projects/index.html', {"date":date, "posts":posts })
