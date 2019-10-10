from django.db import models
import  datetime as dt
# Create your models here.


class Location(models.Model):
    photo_location = models.charField(max_length =30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self, update):
        self.photo_location=update
        self.save()

    @classmethod
    def get_location_id(cls, id):
        locate=Location.objects.get(pk=id)
        return locate

    def __str__(self):
        return self.photo_location


class Category(models.Model):
    photo_category =models.charField(max_length= 30)


    def save_category(self):
        self.save()
    
    
    def delete_category(self):
        self.delete()
    
    def update_category(self ,update):
        self.photo_category = update
        self.save()

    def get_category_id(cls ,id):
        return self.photo_category

    
