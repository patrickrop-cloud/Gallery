from django.test import TestCase
from photos.models import Image,Location,Category
# Create your tests here.

class ImageTestClass(TestCase):
    #setup method
    def setUp(self):
        self.image1=Image(image="image",name='Car',description="Nice Car!")

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image1,Image))

    #Test to save images
    def test_save_images(self):
        self.image1.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images)>0)

    #Test to delete saved images
    def test_delete_images(self):
        self.image1.save_image()
        images_record=Image.objects.all()
        self.image1.delete_image()
        self.assertTrue(len(images_record)==0)
    