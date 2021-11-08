from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView

from mini_fb.forms import CreateProfileForm
from .models import Profile, StatusMessage

# Create your views here.


class ShowAllProfilesView(ListView):
    '''
    Obtain data for all Profile records, and to deleguate work to a 
    template called show_all_profiles.html to display all Profiles.
    '''
    model = Profile
    template_name = "mini_fb/show_all_profiles.html"
    context_object_name = "profiles"

class ShowProfilePageView(DetailView):
    '''obtain data for one Profile and delegate work to template
    called show_profile_page.html to display the profile'''
    model = Profile
    template_name = "mini_fb/show_profile_page.html"
    context_object_name = "profile"

class CreateProfileView(CreateView):
    '''A class-based view which inherits from the generic CreateView class'''
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"
    context_object_name = "form"
