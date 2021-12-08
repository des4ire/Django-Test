from django.db import models


class Visit(models.Model):

    visitor = models.CharField(max_length=100)
    reason = models.CharField(max_length=140)
    date_time = models.DateTimeField()
    email=models.EmailField(30)
    image=models.ImageField(upload_to='visits_images', blank=True)
    
