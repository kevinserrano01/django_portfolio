from django.shortcuts import render
from .models import *

def home(request):
    projects = Project.objects.all()
    languagesFrontend = Frontend.objects.all()
    languagesBackend = Backend.objects.all()
    herramientas = Tools.objects.all()

    data = {
        'projects':projects,
        'frontend': languagesFrontend,
        'backend': languagesBackend,
        'tools': herramientas
    }
    return render(request, 'home.html', data)