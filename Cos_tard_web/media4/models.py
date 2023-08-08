from django.db import models

# # Create your models here.
class testmodel(models.Model):
    name = models.CharField(primary_key=True)
    

