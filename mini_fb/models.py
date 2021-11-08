from django.db import models
import datetime 
from django.urls import reverse

# Create your models here.


class Profile(models.Model):
    '''
    Will model the data of the attributes of FB users. 
    Model will need to include the following data attributes: 
    first name, last name, city, email address, and a profile image url
    '''
    first_name = models.TextField(blank=True)
    last_name = models.TextField(blank=True)
    city = models.TextField(blank=True)
    email = models.TextField(blank=True)
    profile_image_url = models.URLField(blank=True)
    birth_date = models.TextField(blank=True)


    def __str__(self):
        '''return a string representation of this object.'''
        return f'{self.first_name} {self.last_name}'

    def get_status_message(self):
        '''obatain status messages for this profile.'''
        return StatusMessage.objects.filter(profile=self)

    def get_absolute_url(self):
        '''Provide a url to show this object.'''
        return reverse('show_profile_page', kwargs={'pk':self.pk})




class StatusMessage(models.Model):
    '''Will model the data attributes of Facebook status message.'''
    # time stamp
    time_stamp = models.DateTimeField(auto_now_add=True)
    # message
    message = models.TextField(blank=True)
    # profile
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        '''return a string representation of this model'''

        return f'{self.time_stamp} {self.message}'


        

