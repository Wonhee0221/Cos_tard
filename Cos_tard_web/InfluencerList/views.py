from django.shortcuts import render
from django.http import HttpResponse
from InfluencerList.models import Users_fix, Users_info, Media_fix, Media_info
from InfluencerList.crawling import *
from django.db import models
import uuid

#from InfluencerList.models import Users_fix

# Create your views here.

def index(request): 
    
    influencer_dic = {

    'num1' : 'num1_url',
    'num2' : 'num2_url'

}

    return render(request,'InfluencerList/influencerList.html',context=influencer_dic)

    ##크롤링##
admin_id = 17841460966522233
token = "EAALHVkEeHV8BO4wwsy6ZAwa8QYO0FT0MRrO8xxM9029LI5xJFs7iiNSZB3o4rBTnqwZCY1ww1utoRXLp0pqvtVlEXpyNFP0gZAmQExyGDMZC9Kji2obXLmp0O4l0Q98VQda3k3rcUIQCQojxZCbfOwunJD3bUeQjxzNezDY8vjLPOM3ZAVC4I0dsstXSC9PvMCf"
username="rkasl_"

# uf = crawl_users_fix(admin_id, token, username)
# ui = crawl_users_info(admin_id, token, username)
mf = crawl_media_fix(admin_id, token, username)
mi = crawl_media_info(admin_id, token, username)

# print(uf,ui,mf,mi)

#Users_fix.objects.all().delete()
#Users_info.objects.all().delete()

    ##저장##
uf = [1537984987, '권가민', 'rkasl_', None, '@skku.official']
ui = [1537984987, '2023-08-08', 499, 560, 9]


Users_fix = Users_fix()
Users_fix.ig_id=uf[0]
Users_fix.user_id=uf[1]
Users_fix.username=uf[2]
Users_fix.website=uf[3]
Users_fix.biography=uf[4]
Users_fix.save(force_insert=True)

Users_info = Users_info()
Users_info.uid=uuid.uuid4()
Users_info.ig_id=ui[0]
Users_info.date=ui[1]
Users_info.follows_count=ui[2]
Users_info.followers_count=ui[3]
Users_info.media_count=ui[4]
Users_info.save(force_insert=True)

for i in mf:
    Media_fix = Media_fix()
    Media_fix.owner_id=i[0]
    Media_fix.media_id=i[1]
    Media_fix.caption=i[2]
    Media_fix.media_url=i[3]
    Media_fix.permalink=i[4]
    Media_fix.timestamp=i[5]
    Media_fix.save(force_insert=True)

for i in mi:
    Media_info = Media_info()
    Media_info.uid=uuid.uuid4()
    Media_info.media_id=i[0]
    Media_info.date=i[1]
    Media_info.like_count=i[2]
    Media_info.comments_count=i[3]
    Media_info.save(force_insert=True)
