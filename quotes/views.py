from django.shortcuts import render
from django.views.generic import ListView
from .models import Quote

class HomePageView(ListView):
    '''SHow a listing of Quotes.'''
    model = Quote # retrieve Quote objects from database
    template_name = "quotes/home.html"
    context_object_name = "quotes"
# Create your views here.
