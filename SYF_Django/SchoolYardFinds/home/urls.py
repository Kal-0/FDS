from django.urls import path
from home.views import home, feed

urlpatterns = [
    path('', home, name='home'),
    path('feed/', feed, name='feed'),
]