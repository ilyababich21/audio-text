from django.db import models
from django.urls import reverse


# Create your models here.
class Audio(models.Model):
    title = models.CharField(max_length=20)
    audio = models.FileField(upload_to='audio/%Y/%m/%d/%H/%M/%S/')
    text = models.TextField(default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('audio:export_doc',
                       args=[self.id])
