from django.shortcuts import render
from . models import Image,Location,Category

# Create your views here.
def fashion(request):
    images = Image.objects.all()
    return render(request,'fashion.html',{'images':images})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_photos= Image.search_by_category(search_term)
        message= f"{search_term}"
        return render(request, 'all-photo/search.html',{"message":message,"photos":searched_photos})

    else:
        message ="try again"
        return render(request,'all-photo/search.html',{"message":message})

def image(request,image_id):
    try:

        images = Image.objects.get(id =image_id)

    except DoesNotExist:
        raise Http404()
    return render(request,"all-photo/image.html",{"image":image})

def filter_by_location(request,location_id):
    '''
    filter the image location_id
    '''
    images =Image.filter_by_location(location_id)
    return render(request,'location.html', {"images":images})
