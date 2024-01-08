from django.db import models

import os
from uuid import uuid4

from django.utils import timezone



def unique_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4()}.{ext}"
    return os.path.join('images', filename)

def unique_video_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4()}.{ext}"
    return os.path.join('videos', filename)

def unique_report_path(instance,filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid4()}.{ext}"
    return os.path.join('videos', filename)

class Traffic(models.Model):
    date = models.DateField(auto_now_add=True)
    time = models.CharField(max_length=10,blank=True)
    location = models.CharField(max_length=100)
    number_plate = models.CharField(max_length=15)
    owner_name = models.CharField(max_length=100)
    violation_type = models.CharField(max_length=100)
    section = models.CharField(max_length=50)
    image = models.ImageField(upload_to=unique_image_path)
    video = models.FileField(upload_to=unique_video_path)
    camera = models.CharField(max_length=50)
    report = models.FileField(upload_to=unique_report_path)
    def save(self, *args, **kwargs):
        if not self.time:
            self.time = timezone.now().strftime('%H:%M')
        super().save(*args, **kwargs)


