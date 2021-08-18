from django.db import models
from django.urls import reverse
from datetime import date


# class Toy(models.Model):
#   name = models.CharField(max_length=50)
#   color = models.CharField(max_length=20)

#   def __str__(self):
#     return self.name

#   def get_absolute_url(self):
#     return reverse('toys_detail', kwargs={'pk': self.id})

class Clip(models.Model):
  streamer = models.CharField(max_length=100)
  game = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  date = models.DateField()
  url = models.URLField()
  twitch = models.URLField()


#   toys = models.ManyToManyField(Toy)

  def __str__(self):
    return self.streamer

  def get_absolute_url(self):
    return reverse('detail', kwargs={'clip_id': self.id})

class Comment(models.Model):
  date = models.DateField('Clip Date')
  comment = models.TextField(max_length=250)

  
  clip = models.ForeignKey(Clip, on_delete=models.CASCADE, null=True)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.description} on {self.date}"

  # change the default sort
  class Meta:
    ordering = ['-date']