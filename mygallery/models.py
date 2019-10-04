from django.db import models

# Create your models here.
class ImageCategory(models.Model):
    category_name = models.CharField(max_length=60)


class ImageLocation(models.Model):
    location_name = models.CharField(max_length=60)

class Image(models.Model):
    my_image = models.ImageField(upload_to ='allImage/', default = 'allImage/default.jpg')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    created_on = models.DateTimeField(auto_now = True)
    image_category = models.ForeignKey('ImageCategory', on_delete=models.CASCEADE)
    image_location = models.ForeignKey(Location, on_delete = models.CASCADE)
