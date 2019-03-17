from django.db import models
from django.contrib.auth.models import User
import numpy as np
# Create your models here.


class Project(models.Model):
    '''
    This is project class model
    '''
    title = models.CharField(max_length =60)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User, related_name = "images", blank = True)
    url = models.URLField(max_length =100)
    rating = models.TextField()

    def average_design(self):
        design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
        return np.mean(design_ratings)

    def average_usability(self):
        usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
        return np.mean(usability_ratings)

    def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return np.mean(content_ratings)

    def save_project(self):
        self.save()

    
    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    

    def update_caption(self):
        self.save()

    def get_project_id(cls, id):
        project = Project.objects.get(pk=id)
        return project

    class Meta:
        ordering = ('-pub_date',)


    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='image/', null=True)
    user_bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)
    project = models.ForeignKey(Project, null=True)


class Review(models.Model):
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
        (10, '10'),

    )
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    
    def get_comment(self, id):
        comments = Review.objects.filter(project_id =id)
        return comments

class Comments(models.Model):
    comment = models.CharField(max_length = 100, blank = True)
    project = models.ForeignKey(Project, related_name = "comments")
    author = models.ForeignKey(User, related_name = "author")
    pub_date = models.DateTimeField(auto_now_add = True,null = True)


    def save_comment(self):
        self.save()
    
    
        
    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()    

    def __str__(self):
        return self.comment        

