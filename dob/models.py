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