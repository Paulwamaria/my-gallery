from django.test import TestCase

# Create your tests here.
class TestImage(TestCase):
    
    def setUp(self):
        self.new_image = Image()
