from django.test import TestCase
from .models import Image,Comment,Profile
import datetime as dt

# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new profile and saving it
        self.profile = Profile(id=1,user='joseph',bio="programmer")
        self.profile.save_profile()

        # Creating a new comment and saving it
        self.comment = Comment(id=1,image="joseph.jpg",pub_date="08-08-2020",comment="wow",author="joseph")
        self.comment.save_comment()

        self.new_image= Image(id=1, image_name='image',description="wow",pub_date="20202-08-08",Author=self.profile,author_profile=self.profile,likes="yes")
        self.new_image.save()

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        
    def test_save_method(self):
        self.new_image.save_image()
        new_image = Image.objects.all()      
        self.assertTrue(len(new_image) >0)
        
    def test_delete_image(self):
        self.new_image.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)== 0)
        
    def test_update_image(self):
        self.new_image.save_image()
        self.new_image.update_image(self.new_image.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)
