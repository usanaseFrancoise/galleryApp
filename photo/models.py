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
