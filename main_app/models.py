from django.db import models
from django.urls import reverse

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner'),
)
# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  habitat = models.CharField(max_length=100)
  description = models.TextField(max_length=300)
  diet = models.CharField(max_length=100)


  def get_absolute_url(self):
    return reverse('detail', kwargs={'finch_id': self.id})
  
  def __str__(self):
    return self.name
  

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField(
    max_length=1,
    # add the 'choices' field option
    choices=MEALS,
    # set the default value for meal to be 'B'
    default=MEALS[0][0]
  )
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.get_meal_display()} on {self.date}'
  class Meta:
    ordering = ['-date']