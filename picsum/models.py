from django.db import models
import pyperclip

class Location(models.Model):
   """
   Class to create locations
   """
   name = models.CharField(max_length = 30)

   def save_location(self):
       """
       Function to save the instance of this class
       """
       self.save()

   def delete_location(self):
       """
       Method to delete the instance
       """
       self.delete()

   def update_location(self,field,val):
       """
       Method to update the instance
       """
       Location.objects.get(id = self.id).update(field = val)

   def __str__(self):
       return self.name

class Category(models.Model):
   """
   Class to create categories
   """
   name = models.CharField(max_length = 30)
   def save_category(self):
       """
       Function to save the instance of this class
       """
       self.save()

   def delete_category(self):
       """
       Method to delete the instance
       """
       Category.objects.get(id = self.id).delete()

   def update_category(self,field,val):
       """
       Method to update the instance
       """
       Category.objects.get(id = self.id).update(field = val)

   def __str__(self):
       return self.name


class Image(models.Model):
   """
   Class to create images
   """
   image_url = models.ImageField(upload_to = "images/")
   name = models.CharField(max_length = 30)
   description = models.TextField()
   location = models.ForeignKey(Location)
   category = models.ForeignKey(Category)

   def save_image(self):
       """
       Function to save the instance of this class
       """
       self.save()

   def delete_image(self):
       """
       Function to delete the instance of this class
       """
       Image.objects.get(id = self.id).delete()

   def update_image(self,val):
       """
       Method to update the instance
       """
       Image.objects.filter(id = self.id).update(name = val)

   @classmethod
   def get_image_by_id(cls,image_id):
       """
       Method to get a specific image
       """
       return cls.objects.get(id = image_id)


   @classmethod
   def get_photos(cls):
       return cls.objects.all()


   @classmethod
   def search_by_category(cls,category):
        photo = Category.objects.filter(name__icontains = category)[0]
        return  cls.objects.filter(category_id = photo.id)

   @classmethod
   def filter_by_location(cls,location):
       """
       Method to get images taken in a certain location
       """
       the_location = Location.objects.get(name = location)
       return cls.objects.filter(location_id = the_location.id)

   def __str__(self):
       return self.name
