from django.db import models

# Create your models here.

class Users_fix(models.Model):
    ig_id=models.BigIntegerField(primary_key=True, null=False, unique=True)
    user_id=models.CharField()
    username=models.CharField()
    website=models.TextField()
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
    media_url=models.TextField()
    permalink=models.TextField()
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

