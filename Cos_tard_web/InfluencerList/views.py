from django.shortcuts import render
from django.http import HttpResponse
from InfluencerList.models import *
from InfluencerList.crawling import *

# Create your views here.

def index(request): 
    
    influencer_dic = {

    'num1' : 'num1_url',
    'num2' : 'num2_url'

}

    return render(request,'InfluencerList/influencerList.html',context=influencer_dic)

    ##크롤링##
# admin_id = 17841402050732962
# token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"
# username="rkasl_"

# uf = crawl_users_fix(admin_id, token, username)
# ui = crawl_users_info(admin_id, token, username)
# mf = crawl_media_fix(admin_id, token, username)
# mi = crawl_media_info(admin_id, token, username)

# print(uf, ui, mf, mi)

#     #저장##
# Users_fix.objects.create(ig_id=uf[0], user_id=uf[1], username= uf[2], website=uf[3], biography=uf[4])
# Users_info.objects.create(ig_id=ui[0], date=ui[1], follows_count= ui[2], followers_count=ui[3], media_count=ui[4])

# for i in mf:
#     Media_fix.objects.create(ig_id=mf[i][0], media_id=mf[i][1], caption=mf[i][2], media_url=mf[i][3], permalink=mf[i][4],timestamp=mf[i][5])
 
# for i in mi:
#     Media_info.objects.create(media_id=mi[i][0], date=mi[i][1], like_count=mi[i][2], comments_count=mi[i][3])


