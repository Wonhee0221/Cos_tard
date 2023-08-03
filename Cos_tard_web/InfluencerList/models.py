from django.db import models

# Create your models here.

#
#test table 입니다람쥐
# class Menu(models.Model):
#     name = models.CharField(max_length=45)

#     class Meta:
#         #managed=False auto migration 방지
#         db_table = "menu"
#

class Users_fix(models.Model):
    ig_id=models.BigIntegerField(primary_key=True, null=False, unique=True)
    user_id=models.CharField()
    username=models.CharField()
    website=models.URLField()
    biography=models.TextField()

    class Meta:
        db_table = "Users_fix"

class Users_info(models.Model):
    ig_id=models.ForeignKey(Users_fix, on_delete=models.CASCADE)
    date=models.DateField()
    follows_count=models.IntegerField()
    followers_count=models.IntegerField()
    media_count=models.IntegerField()

    class Meta:
        db_table = "Users_info"

class Media_fix(models.Model):
    media_id=models.IntegerField(primary_key=True, null=False, unique=True)
    caption=models.TextField()
    media_url=models.URLField()
    permalink=models.URLField()
    timestamp=models.DateTimeField()

    class Meta:
        db_table = "Media_fix"

class Media_info(models.Model):
    media_id=models.ForeignKey(Media_fix, on_delete=models.CASCADE)
    date=models.DateField()
    like_count=models.IntegerField(null=True)
    comments_count=models.IntegerField(null=True)

    class Meta:
        db_table = "Media_info"

