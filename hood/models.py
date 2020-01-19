from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class UserProfile(models.Model):
    description = HTMLField()
    neighbourhood = models.ForeignKey(neighbourhood, on_delete=models.CASCADE)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    cover = models.ImageField(upload_to='images/')
    

class Blog(models.Model):
    title = models.CharField(max_length=150)
    postcover = models.ImageField(upload_to='imagas/')
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood= models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



class Business(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    email = models.EmailField()
    address =models.CharField(max_length=100)
    contact = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user
    
    @classmethod
    def search_business(cls,search_term):
        businesses = cls.objects.filter(description__icontains=search_term)
        return businesses
    

class Education(models.Model):
    user =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    educationservices = models.ManyToManyField(educationservices)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user


class Authorities(models.Model):
    neighbourhood = models.ForeignKey(neighbourhood,on_delete=models.CASCADE)
    name =models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.IntegerField()
    address =models.CharField(max_length=100)
    description = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

