from django.urls import path

from mini_fb.forms import CreateStatusMessageForm
from .views import DeleteStatusMessageView, ShowAllProfilesView, ShowNewsFeedView, ShowProfilePageView, CreateProfileView, UpdateProfileView, post_status_message, ShowPossibleFriendsView

urlpatterns =[
    path('', ShowAllProfilesView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('create_profile', CreateProfileView.as_view(), name='create_profile'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name='update_profile'),
    path('profile/<int:pk>/post_status', post_status_message, name='post_status_message'),
    path('profile/<int:profile_pk>/delete_message/<int:status_pk>', DeleteStatusMessageView.as_view(), name='delete_message'),
    path('profile/<int:pk>/news_feed', ShowNewsFeedView.as_view(), name='news_feed'),
    path('profile/<int:pk>/show_possible_friend', ShowPossibleFriendsView.as_view(), name='show_possible_friends'),
]
