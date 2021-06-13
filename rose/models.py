from django.db import models

# Create your models here.
class Design(models.Model):
    name = models.CharField(max_length=100)
    cost = models.IntegerField()
    desc = models.TextField()
    review = models.IntegerField()
    img = models.ImageField(upload_to='pics')