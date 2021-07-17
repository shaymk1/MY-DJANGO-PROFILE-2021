from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

# class Home(models.Model):

#   image = models.ImageField(upload_to='static/images')
#   name = models.CharField(max_length=200,null=True)
#   overview = models.TextField(blank=True, null=True)
  
#   def __str__(self):
#     return self.name


class About(models.Model):

  image = models.ImageField(upload_to='static/images')
  name = models.CharField(max_length=200, null=True)
  overview = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name


class Work(models.Model):

  image = models.ImageField(upload_to='static/images')
  name = models.CharField(max_length=200, null=True)
  overview = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email










# class Contact(models.Model):

#   # image = models.ImageField(upload_to='static/images')
#   name = models.CharField(max_length=200, null=True)
#   overview = models.TextField(blank=True, null=True)

#   def __str__(self):
#     return self.name
