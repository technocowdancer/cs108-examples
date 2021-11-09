# forms.py 

from django import forms
from .models import Image, Quote

class CreateQuoteForm(forms.ModelForm):
    '''A form to create a new Quote object.'''

    class Meta:
        '''additional data about this form'''
        model = Quote # which model to create
        fields = ['text', 'person'] # which fields to create


class UpdateQuoteForm(forms.ModelForm):
    '''A form to update a new Quote object.'''

    class Meta:
        '''additional data about this form'''
        model = Quote # which model to create
        fields = ['text', 'person'] # which fields to create

class AddImageForm(forms.ModelForm):
    '''A form to collect an iage from the user and store in database'''

    class Meta:
        model = Image
        fields = ["image_file",]