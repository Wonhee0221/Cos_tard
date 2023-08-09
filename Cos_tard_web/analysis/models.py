from django.db import models

# Create your models here.
class testTable(models.Model):
    id=models.CharField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    followerCount=models.IntegerField()

    class Meta:
        managed=False
        db_table="testTable"