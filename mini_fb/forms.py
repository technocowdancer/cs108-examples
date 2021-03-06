from django import forms
from .models import Profile, StatusMessage


class CreateProfileForm(forms.ModelForm):
    '''A special class which inherits from forms.ModelForm.'''
    first_name = forms.CharField(label="First Name", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    last_name = forms.CharField(label="Last Name", required=True)
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email", required=True)
    class Meta:
        '''additional data about this form'''
        model = Profile # which model to create
        fields = ['first_name', 'last_name', 'city', 'email', 'profile_image_url', 'birth_date'] # which fields to create

class UpdateProfileForm(forms.ModelForm):
    '''A class UpdateProfileForm that inherits from forms.ModelForm'''
    city = forms.CharField(label="City", required=True)
    email = forms.CharField(label="Email", required=True)
    birth_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2012,1920,-1),),)
    class Meta:
        model = Profile
        fields = ['city', 'email', 'profile_image_url', 'birth_date']


class CreateStatusMessageForm(forms.ModelForm):
    '''A form to create a new message post on a profile.'''
    image_file = forms.ImageField(required=False)
    class Meta:
        '''additional data about this form'''
        model = StatusMessage # which model to create
        fields = ['message', 'image_file'] # which fields to create

