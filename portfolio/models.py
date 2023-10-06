from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

class Project(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)

    def __str__(self) -> str:
        return self.title
    
class Frontend(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='portfolio/frontend/')

    def __str__(self) -> str:
        return self.title
    
class Backend(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='portfolio/backend/')

    def __str__(self) -> str:
        return self.title
    
class Tools(models.Model):
    title = CharField(max_length=100)
    image = ImageField(upload_to='portfolio/backend/')

    def __str__(self) -> str:
        return self.title