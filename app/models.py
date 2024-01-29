from django.db import models

# Create your models here.

class Friends(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=100)
    loc=models.CharField(max_length=199)


    def __str__(self):
        return self.sname