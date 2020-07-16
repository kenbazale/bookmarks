from django.urls import path
from .views import image_create, Image_detail, image_like


urlpatterns = [
    path('create/', image_create, name='create'),
    path('detail/<id>/<slug>', Image_detail, name='detail'),
    path('like/', image_like, name='like'),
]
