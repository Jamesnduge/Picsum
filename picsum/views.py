from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Location


def home(request):
    images = Image.get_photos()
    return render(request,'home.html',{"images":images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_by_category(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any image"
        return render(request, 'search.html',{"message":message})
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"image.html", {"image":image})
def location(request,location):
        locations = Image.filter_by_location(location)
        return render(request,'location.html',{"images": locations})

def page(request):
    return render(request,"page.html",{"title":location})
