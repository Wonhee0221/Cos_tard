from django.db import models

# Create your models here.

# class Users(models.Model):
#     user_id = models.IntegerField(max_length=100)
#     username = models.CharField(max_length=100)

#     def __str__(self):
#         return self.username

class Comment(models.Model):
    ig_id = models.CharField(primary_key=True)
    username = models.CharField()
    infocomment = models.IntegerField()
    totalcomment = models.IntegerField()
    inforate = models.FloatField()
    imagecomment = models.IntegerField()
    imagerate = models.FloatField()
    domain = models.IntegerField()
    cute = models.IntegerField()
    pure = models.IntegerField()
    gorg = models.IntegerField()
    maximage = models.CharField()
    maximagerate = models.FloatField()

    class Meta:
        managed=False
        db_table = "comment"


class Combined_caption(models.Model):
    ig_id = models.CharField(primary_key=True)
    caption = models.TextField()
    label = models.CharField()

    class Meta:
        managed=False
        db_table = "comment"