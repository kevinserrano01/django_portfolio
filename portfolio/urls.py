from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('projects/', get_projects, name='projects'),
]