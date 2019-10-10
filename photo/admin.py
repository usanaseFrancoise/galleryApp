from django.contrib import admin
from .models import Location,Image,Category
# Register your models here.



admin.site.Register(Location)
admin.site.Register(Image)
admin.site.Register(Category)