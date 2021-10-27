# file: hello_world/urls.py
# description: direct URL requests to view functionsq

from django.urls import path 
from .views import homePageView

urlpatterns = [
    path('', homePageView, name='home'),

]