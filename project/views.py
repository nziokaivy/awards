from django.shortcuts import render
from django.http  import HttpResponse
from .models import Project, Profile,Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ReviewForm, ProjectForm

# Create your views here.

def home(request):
    current_user = request.user
    projects = Project.objects.order_by('-pub_date')
    return render(request, 'index.html', {'projects':projects})

def profile(request):
    user = request.user    
    projects = Project.objects.all().filter(poster_id = user.id)
    return render(request, 'profile.html', {'projects':projects, "user":user, "current_user":request.user })


def project(request, id):
    project = Project.objects.get(pk = id)
    user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()
    return render(request, 'image.html', {"project": project, "form":form, "comments":comments})    

