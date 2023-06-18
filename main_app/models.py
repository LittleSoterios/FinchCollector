from django.db import models
from django.urls import reverse
# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    wingspan = models.IntegerField()
    length = models.IntegerField()
    weight = models.IntegerField()
    habitats = models.TextField(null=True)
    img = models.TextField(null=True)


    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id' : self.id})
        