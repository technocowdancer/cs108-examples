from django.db import models

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


    def __str__(self):
        '''return a string representation of this object.'''
        return f'{self.first_name} {self.last_name}'
