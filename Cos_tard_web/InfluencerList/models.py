from django.db import models

# Create your models here.

class Users_fix(models.Model):
    users_fix_id=models.BigIntegerField(primary_key=True, null=False)
    user_id=models.CharField()
    username=models.CharField()
    website=models.URLField(null=True)
    biography=models.TextField()

    class Meta:
        #managed=False
        db_table = "Users_fix"


class Users_info(models.Model):
    users_info_id=models.BigIntegerField()
    date=models.DateField()
    follows_count=models.IntegerField()
    followers_count=models.IntegerField()
    media_count=models.IntegerField()

    class Meta:
        #managed=False
        db_table = "Users_info"


class Media_fix(models.Model):
    owner_id=models.BigIntegerField()
    media_fix_id=models.TextField(primary_key=True, null=False)
    caption=models.TextField(null=True)
    media_url=models.URLField()
    permalink=models.URLField()
    timestamp=models.DateTimeField()

    class Meta:
        #managed=False
        db_table = "Media_fix"


class Media_info(models.Model):
    media_info_id=models.BigIntegerField()
    date=models.DateField()
    like_count=models.IntegerField(null=True)
    comments_count=models.IntegerField(null=True)

    class Meta:
        #managed=False
        db_table = "Media_info"



