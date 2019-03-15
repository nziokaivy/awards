from django.shortcuts import render
from django.http  import HttpResponse
from .models import Project, Profile, DesignRating, UsabilityRating, ContentRating
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    current_user = request.user
    projects = Project.objects.order_by('-pub_date')
    return render(request, 'index.html', {'projects':projects})

def profile(request):
    user = request.user    
    images = Image.objects.all().filter(poster_id = user.id)
    return render(request, 'profile.html', {'images':images, "user":user, "current_user":request.user })
      