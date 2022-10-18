from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(null=False, max_length=30)
    roll = models.IntegerField(null=False)
    school = models.CharField(null=False, max_length=30)
    class Meta:
        ordering = ['roll']