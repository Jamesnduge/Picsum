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
