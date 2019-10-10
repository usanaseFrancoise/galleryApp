# from django.test import TestCase
# from .models import Location,Image,Category
# import datetime as datetime
# # Create your tests here.
# class LocationTestClass(TestCase):
#     def setUp(Self):
#         Self.kigali =Location(photo_location='Rwanda')
#         self.kigali.save_location()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.kigali,Location))
        
#     def test_updating_location(self):
#         location= Location.get_location_id(self.kigali.id)
#         location.update_location('Canada')
#         location=Location.get_location_id(self.kigali.id)
#         self.assertTrue(location.photo_location =='Canada')

#     def tearDown(Self):
#         self.kigali.delete.location()

# class CategoryTestClass(TestCase):
#     def setUp(self):
#         self.boyswear =Category(photo_category='Menswear')
#         self.boyswear,save_category()

#     def test_instance(self):
#         self.assertTrue(isinstance(self.boyswear,Category))

#     def tearDown(self):
#         self.boyswear.delete_category()

# class ImageTestClass(TestCase):
#     '''
#     class of image and its all functions
#     '''
#     def setUp(self):
#         self.ladieswear =Category(photo_category='Ladieswear')
#         self.ladieswear,save_category()

#         self.kigali =Location(photo_location='Kigali')
#         self.kigali.save_location()

#         self.image=Image(title='Fashion',Description='ladieswear',location=self.kigali,category=self.Ladieswear)
#         self.image.save_image()
#         new_image =Image.objects.filter(photo='')

#     def test_instance(self):
#         self.assertTrue(isinstance(self.image,Image))

#     def test_save_method(self):
#         '''
#         function to test image
#         '''
#         self.image.save_image()
#         self.image.delete_image()

#     def test_update_method(self):
#         self.image.save_image()
#         self