from django.urls import path
from home.views import home, feed

urlpatterns = [
    path('', home),
    path('feed/', feed),
]