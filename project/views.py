from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http  import HttpResponse
from .models import Project, Profile, Review, Comments
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import ReviewForm, ProjectForm, NewProjectForm

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
    latest_review_list = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()
    return render(request, 'project.html', {"project": project, "form":form, "comments":comments,})    

def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        return redirect('home')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})

def search_projects(request):

    # search for a user by their username
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_projects(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "projects": searched_projects})

    else:
        message = "You haven't searched for any person"
        return render(request, 'search.html', {"message": message})

