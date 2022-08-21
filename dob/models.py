from django.db import models
from django.contrib.auth.models import User

class Wishes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    relation = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(max_length=250, blank=True, null=True)
    image = models.ImageField(upload_to='dob/images/')
    audio = models.FileField(upload_to='music/')
    dob = models.DateField(auto_now=False)

    class Meta:
        db_table = "wish"
        verbose_name = 'wish'
        verbose_name_plural = 'wishes'
        ordering = ['-pk']
class SongDedication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    audio = models.FileField(upload_to='music/dedication')

    class Meta:
        db_table = "song dedication"
        verbose_name = 'song dedication'
        verbose_name_plural = 'song dedications'
        ordering = ['-pk']


class Memories(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dob/memories')

    class Meta:
        db_table = 'memories'
        verbose_name = 'memories'
        verbose_name_plural = 'memories'
        ordering =['-pk']