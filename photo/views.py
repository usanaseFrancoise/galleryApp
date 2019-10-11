from django.shortcuts import render
from . models import Image,Location,Category
from django.http import HttpResponse,Http404
import datetime as datetime
# Create your views here.
def index(request):
    images = Image.objects.all()
    return render(request, 'index.html',{'images':images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos= Image.search_by_category(search_term)
        message= f"{search_term}"
        return render(request, 'allPhoto/search.html',{"message":message,"photos":searched_photos})

    else:
        message ="try again"
        return render(request,'allPhoto/search.html',{"message":message})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"allPhoto/image.html", {"image":image})
def filter_by_location(request,location_id):
   """
   Function that filters images by location
   """
   images = Image.filter_by_location(id=location_id )
   return render (request, 'location.html', {"images":images})

def filter_by_category(request,category_id):
   """
   Function that filters images by location
   """
   images = Image.filter_by_category(id=category_id )
   print(images)
   return render (request, 'category.html', {"images":images})
