from django.test import TestCase
from .models import Location,Image,Category
import datetime as dt

class LocationTestCase(TestCase):
    def setUp(self):
        self.Kigali =Location(photo_location='Rwanda')
        self.Kigali.save_location()

    def test_updating_location(self):
        location=Location.get_location_id(self.Kigali.id)
        location.update_location('Canada')
        location=Location.get_location_id(self.Kigali.id)
        self.assertTrue(location.photo_location == 'Canada')

    
    def test_delete_location(self):
        self.Kigali.save_location()
        loco=Location.objects.all()
        self.assertTrue(len(loco)>=1)


