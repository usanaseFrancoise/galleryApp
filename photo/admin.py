from django.contrib import admin
from django.contrib import admin
from .models import Location,Image,Category
# Register your models here.


admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image)
