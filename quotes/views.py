from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Quote
import random

class HomePageView(ListView):
    '''SHow a listing of Quotes.'''
    model = Quote # retrieve Quote objects from database
    template_name = "quotes/home.html"
    context_object_name = "quotes"


class QuotePageView(DetailView):
    '''Display  single quote object.'''
    model = Quote                        # Retrieve Quote objects from the database
    template_name = "quotes/quote.html"  # Delegate the display to this teplate
    context_object_name = "quote"        # Use this variable name in the template 

class RandomQuotePageView(DetailView):
    '''Display  single quote object.'''
    model = Quote                        # Retrieve Quote objects from the database
    template_name = "quotes/quote.html"  # Delegate the display to this teplate
    context_object_name = "quote"        # Use this variable name in the template 

    def get_object(self):
        '''Select one quote at random'''

        # obtain all quotes using the object manager
        quotes = Quote.objects.all()

        # select one at random
        q = random.choice(quotes)
        return q

