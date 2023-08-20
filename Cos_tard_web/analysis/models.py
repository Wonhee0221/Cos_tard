from django.db import models

class Feed(models.Model):
    ig_id=models.CharField()
    year=models.CharField()
    month=models.CharField()
    media=models.CharField()
    date_index=models.CharField()
    uid=models.CharField(primary_key=True)
    like_count=models.IntegerField()
    comments_count=models.IntegerField()

    class Meta:
        managed=False
        db_table = "feed"
