from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse
from mini_fb.forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
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


    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm() 
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    '''A class-based view which inherits from the generic CreateView class'''
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_fb/create_profile_form.html"
    context_object_name = "form"

class UpdateProfileView(UpdateView):
    '''a class-based view which inherits from the generic UpdateView class'''
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"
    context_object_name = "form"

def post_status_message(request, pk):
    '''
    Process a form submission to post a new status message.
    '''

    # if and only if we are processing a POST request, try to read the data
    if request.method == 'POST':

        # print(request.POST) # for debugging at the console

        # create the form object from the request's POST data
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        if form.is_valid():

            # create the StatusMessage object with the data in the CreateStatusMessageForm
            status_message = form.save(commit=False) # don't commit to database yet

            # find the profile that matches the `pk` in the URL
            profile = Profile.objects.get(pk=pk)

            # attach FK profile to this status message
            status_message.profile = profile

            # now commit to database
            status_message.save()
        # redirect the user to the show_profile_page view
    url = reverse('show_profile_page', kwargs={'pk': pk})
    return redirect(url)




class DeleteStatusMessageView(DeleteView):
    '''Delete a status message object and remove it in the database.'''


    template_name = "mini_fb/delete_status_form.html"
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['status_to_delete'] = st_msg
        # return this context dictionary
        return context

    def get_object(self):
        '''Select one quote at random'''

        # obtain all quotes using the object manager

        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        # select one at random
        return st_msg

    
    def get_success_url(self):
        
        '''return a url to which we should be directed after the delete.'''
    
        # read the URL data values into variables

        # read the URL data values into variables
        # # get the pk for this quote
        pk = self.kwargs.get('status_pk')
        message = StatusMessage.objects.filter(pk=pk).first()

        # # find the person associated with the quote
        person = message.profile
        return reverse('show_profile_page', kwargs={'pk':person.pk})

class ShowNewsFeedView(DetailView):
    '''create a view for the news feed of a profile's friends'''
    # time = models.TimeField(auto_now_add=True)
    model = Profile
    template_name = "mini_fb/show_news_feed.html"
    context_object_name = "profile_for_feed"
    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass; 
        # this will include the Profile record to display for this page view
        context = super(ShowNewsFeedView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary

        # find the profile objects
        pk = self.kwargs.get('pk')
        get_profile_object = Profile.objects.get(pk=pk) # <-- in pre-class material
        # call the news feed method on that object
        News_feed = get_profile_object.get_news_feed()
        # put the news feed into object
        context['news_feed'] = News_feed
        # return this context dictionary
        return context
