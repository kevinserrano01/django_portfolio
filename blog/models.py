from django.db import models
from django.db.models.fields import CharField
import datetime

class Post(models.Model):
    title = CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images') # Crea nueva carpeta para las imagenes
    date = models.DateField(datetime.date.today) # Fecha actual

    def __str__(self) -> str:
        return self.title