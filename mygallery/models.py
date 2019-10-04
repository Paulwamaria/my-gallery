from django.db import models

# Create your models here.
class ImageCategory(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_imagecategory(self):
        self.save()

class ImageLocation(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_imagelocation(self):
        self.save()

class ImagePost(models.Model):
    my_image = models.ImageField(upload_to ='allImage/', default = 'allImage/default.jpg')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    created_on = models.DateTimeField(auto_now = True)
    image_category = models.ForeignKey('ImageCategory', on_delete=models.CASCADE)
    image_location = models.ForeignKey(ImageLocation, on_delete = models.CASCADE)


    def __str__(self):
        return self.image_name


    def save_imagepost(self):
        self.save()

    def delete_imagepost(self):
        self.delete()

    
    def get_image_by_id(id):
        image = ImagePost.objects.get(pk=id)
        return image

    @classmethod
    def search_image(cls,category_name):
        images = cls.objects.filter(image_category=category_name)
        return images
