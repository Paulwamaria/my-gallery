from django.shortcuts import render
from django.models import ImagePost, ImageCategory, ImageLocation

# Create your views here.

def index(request):
    posts = ImgePost.objects.all()

    context = {
        "posts":posts
    }
    return render(request, 'index.html',context)
