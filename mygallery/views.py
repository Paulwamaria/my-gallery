from django.shortcuts import render
from django.http import Http404
from .models import ImagePost, ImageCategory, ImageLocation


# Create your views here.

def index(request):
    posts = ImagePost.objects.all()

    context = {
        "posts":posts
    }
    return render(request, 'general_templates/index.html',context)


def search_results(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_imageposts = ImagePost.search_image(search_term)

        message = f"{search_term}"



        context = {
            "message":message,
            "imageposts":searched_imageposts
        }

        return render(request, 'general_templates/search.html', context)


    else:
        message = "You haven't searched for any term"

        return render(request,'general_templates/search.html',{"message":message})

      

