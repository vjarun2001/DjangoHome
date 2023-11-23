from django.db import models

class HomeDB(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=50)
    

    