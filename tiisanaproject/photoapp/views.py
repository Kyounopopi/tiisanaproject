from django.shortcuts import render, get_object_or_404
from .models import Photo

def photo_list(request):
    photos = Photo.objects.order_by("-id") 
    return render(request, "photoapp/photo_list.html", {"photos": photos})

def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, "photoapp/photo_detail.html", {"photo": photo})
