from .models import Review, Profile, Project
from django import forms
from django.forms import ModelForm, Textarea, IntegerField


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user',]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [ 'usability_rating', 'design_rating', 'content_rating' , 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15}),
        }