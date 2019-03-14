from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    '''
    This is project class model
    '''
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User)
    url = models.URLField(max_length =100)
    rating = models.TextField()

class Profile(models.Model):
    photo = models.ImageField(upload_to='image/', null=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)

class DesignRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)

class UsabilityRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)

class ContentRating(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    )
    project = models.ForeignKey(Project)
    pub_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES, default=0)
