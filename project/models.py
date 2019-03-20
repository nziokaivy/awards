from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import numpy as np
from django.conf import settings
# Create your models here.

def post_save_user_model(sender,instance,created,*args,**kwargs):
    if created:
        try: 
            Profile.objects.create(user = instance)
        except:
            pass
post_save.connect(post_save_user_model,sender=settings.AUTH_USER_MODEL)


class Project(models.Model):
    '''
    This is project class model
    '''
    title = models.CharField(max_length =60, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User,related_name='images', on_delete=models.CASCADE, db_index=True, blank = True)
    url = models.URLField(max_length =100, null=True)
    rating = models.TextField(null=True)

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()


    def delete_project(self):
        self.delete()

    def update_caption(self):
        self.save()

    def get_project_id(cls, id):
        project = Project.objects.get(pk=id)
        return project

    class Meta:
        ordering = ('-pub_date',)

    
    @classmethod
    def search_project(cls,name):
        project = Project.objects.filter(title__icontains = name)
        return project

    
    def save_project(self):
       
       self.save()

    def delete_project(self):
       
       self.delete()  

    def __str__(self):
       return self.poster



class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='image/', null=True, blank=True)
    user_bio = models.TextField(null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default=1)
    project = models.ForeignKey(Project, null=True)

    def save_profile(self):
        self.save()

      
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile

    def get_absolute_url(self): 
        return reverse('user_profile')
    

    def __str__(self):
        return self.user


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
    pub_date = models.DateTimeField(auto_now_add = True,null = True)


    def get_comment(self, id):
        comments = Review.objects.filter(project_id =id)
        return comments

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    post_save.connect(create_user_profile, sender=User)


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


    @classmethod
    def search_users(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term)
        return profiles

    @property
    def image_url(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
   

class Comments(models.Model):
    comment = models.CharField(max_length = 100, blank = True)
    project = models.ForeignKey(Project, related_name = "comments")
    author = models.ForeignKey(User, related_name = "author", null=True)
    pub_date = models.DateTimeField(auto_now_add = True,null = True)


    def save_comment(self):
        self.save()
    
    @classmethod
    def get_comments_by_projects(cls, id):
        comments = Comments.objects.filter(project__pk = id)
        return comments
        
    def __str__(self):
        return self.text
        
    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()    

    def __str__(self):
        return self.comment        

