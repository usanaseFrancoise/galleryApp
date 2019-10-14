from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt

class LocationTestCase(TestCase):
  

    def test_updating_location(self):
        location=Location.get_location_id(self.Kigali.id)
        location.update_location('Canada')
        location=Location.get_location_id(self.Kigali.id)
        self.assertTrue(location.photo_location == 'Canada')

    
    def test_delete_location(self):
        self.Kigali.save_location()
        loco=Location.objects.all()
        self.assertTrue(len(loco)>=1)


    def setUp(self):
        self.Kigali =Location(photo_location='Rwanda')
        self.Kigali.save_location()

class CategoryTestCase(TestCase): 

    def setUp(self):
        self.clothes =Category(photo_category='shoes')
        self.clothes.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.clothes,Category))

    def test_delete_category(self):
        self.clothes.save_category()
        cat=Category.objects.all()
        self.assertTrue(len(cat)<=1)

class ImageTestCase(TestCase): 
    
    
    def setUp(self):
        self.shoes=Category(photo_category='shoes')
        self.shoes.save_category()
        self.Kigali=Location(photo_location='Kigali')
        self.Kigali.save_location()
        self.image=Image(title='Galleryapp',location=self.Kigali,category=self.shoes)
        self.image.save_image()


    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_method(self):
        self.image.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()

   
    def test_filter_by_location(self):
        self.image.save_image()
        img=self.image.filter_by_location(self.image.location_id)
        image=Image.objects.filter(location=self.image.location_id)
        self.assertTrue(img,image)