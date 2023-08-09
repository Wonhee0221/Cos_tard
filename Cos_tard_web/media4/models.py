from django.db import models

# # Create your models here.
class testmodel(models.Model):
    name = models.CharField(primary_key=True)
    
class Users_fix(models.Model):
    ig_id=models.CharField(primary_key=True)
    user_id=models.CharField()
    username=models.CharField()
    website=models.CharField()
    biography=models.CharField()

    class Meta:
        managed=False
        db_table = "users_fix"


class Users_info(models.Model):
    uid=models.CharField(primary_key=True)
    ig_id=models.CharField()
    date=models.CharField()
    follows_count=models.CharField()
    followers_count=models.CharField()
    media_count=models.CharField()

    class Meta:
        managed=False
        db_table = "users_info"


class Media_fix(models.Model):
    uid=models.CharField(primary_key=True)
    owner_id=models.CharField()
    media_id=models.CharField()
    caption=models.CharField()
    media_url=models.CharField()
    permalink=models.CharField()
    timestamp=models.CharField()

    class Meta:
        managed=False
        db_table = "media_fix"


class Media_info(models.Model):
    uid=models.CharField(primary_key=True)
    media_id=models.CharField()
    date=models.CharField()
    like_count=models.CharField()
    comments_count=models.CharField()

    class Meta:
        managed=False
        db_table = "media_info"



