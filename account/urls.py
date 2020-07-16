from django.urls import path
from . views import dashboard, SignUp, profile


urlpatterns = [
     path('', dashboard, name='dashboard'),
     path('signup/', SignUp, name='signup'),
     # path('create/',CreateProfile.as_view(),name='create_profile'),
     path('create_profile/', profile, name='create_profile')
]
