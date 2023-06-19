from django.db import models
from django.urls import reverse
# Create your models here.


class Finch(models.Model):
    name = models.CharField(max_length=100)
    wingspan = models.IntegerField()
    length = models.IntegerField()
    weight = models.IntegerField()
    habitats = models.TextField(null=True)
    img = models.TextField('Image link', null=True)


    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id' : self.id})
        

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    class Meta:
        ordering = ['-date']