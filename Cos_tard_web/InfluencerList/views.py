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
# admin_id = 17841400029634031
# token = "EAAKoyNOZAm4UBOZB2IZAQBu91Nq3vZBZCwpSsemWPYkcvEJdiXVLAUOF1M2eKnGABbVFtvYzipJjITU7oJqospRiQrFdPjRr51OQd2p8T4dBfbueEzJKuPxAO1iKHoQjF39LGmzGiL2ReNsqC3iOBMd4KDZBh7oFijQkElaelLSkOOUlKrmLIRw6oH"
# username="rkasl_"

# uf = crawl_users_fix(admin_id, token, username)
# ui = crawl_users_info(admin_id, token, username)
# mf = crawl_media_fix(admin_id, token, username)
# mi = crawl_media_info(admin_id, token, username)

# print(ui)

    ##저장##
#Users_fix.objects.create(ig_id=uf[0], user_id=uf[1], username= uf[2], website=uf[3], biography=uf[4])
#Users_info.objects.create(ig_id=ui[0], date=ui[1], follows_count= ui[2], followers_count=ui[3], media_count=ui[4])
#Users_info.objects.create(user_id=1537984987, date='2023-08-07', follows_count= 500, followers_count=500, media_count=10)

# for i in mf:
#     Media_fix.objects.create(ig_id=mf[i][0], media_id=mf[i][1], caption=mf[i][2], media_url=mf[i][3], permalink=mf[i][4],timestamp=mf[i][5])
 
# for i in mi:
#     Media_info.objects.create(media_id=mi[i][0], date=mi[i][1], like_count=mi[i][2], comments_count=mi[i][3])


