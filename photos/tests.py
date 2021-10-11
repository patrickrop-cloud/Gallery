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
    
    #Test to update an image
    def test_update_image(self):
        image=Image.objects.first()
        new_image=Image.update_image()
        expected_image=f'{new_image}'
        self.assertTrue(expected_image,'new_image')

    #Test to search for category
    def test_search_category(self):
        category=Image.objects.all()
        search_term='business'
        db_term=search_term
        if db_term !=search_term:
            return('no match')

        else:
            return(search_term)  
class CategoryTestClass(TestCase):
    
    #setup method
    def setUp(self):
        self.adventure=Category(category_name="photography")
    
    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.adventure,Category))

    #Test to save categories
    def test_save_categories(self):
        self.adventure.save_categories()
        category=Category.objects.all()
        self.assertTrue(len(category)>0)

    #Test to delete categories
    def test_delete_categories(self):
        self.adventure.save_categories()
        category_record=Category.objects.all()
        self.adventure.delete_category()
        self.assertTrue(len(category_record)==0)

class LocationTestClass(TestCase):
    #setup method
    def setUp(self):
        self.nairobi=Location(location_name="Nairobi")

    #Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi,Location))

    #Test to save location
    def test_save_location(self):
        self.nairobi.save_location()
        location=Location.objects.all()
        self.assertTrue(len(location)>0)
    #Test to delete location
    def test_delete_location(self):
        self.nairobi.save_location()
        location_record=Location.objects.all()
        self.nairobi.delete_location()
        self.assertTrue(len(location_record)==0)

    