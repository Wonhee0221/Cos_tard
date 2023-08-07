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

# users_fix = crawl_users_fix(admin_id, token, username)
# users_info = crawl_users_info(admin_id, token, username)
# media_fix = crawl_media_fix(admin_id, token, username)
# media_info = crawl_media_info(admin_id, token, username)

# print(users_fix,users_info,media_fix,media_info)

# Users_fix.objects.all().delete()
# Users_info.objects.all().delete()
# Media_fix.objects.all().delete()
# Media_info.objects.all().delete()

#     ##저장##
# Users_fix.objects.create(ig_id=users_fix[0], user_id=users_fix[1], username= users_fix[2], website=users_fix[3], biography=users_fix[4])
# Users_info.objects.create(ig_id=users_info[0], date=users_info[1], follows_count= users_info[2], followers_count=users_fix[3], media_count=users_info[4])

# for i in media_fix:
#     Media_fix.objects.create(ig_id=media_fix[i][0], media_id=media_fix[i][1], caption=media_fix[i][2], media_url=media_fix[i][3], permalink=media_fix[i][4],timestamp=media_fix[i][5])
 
# for i in media_info:
#     Media_info.objects.create(media_id=media_info[i][0], date=media_info[i][1], like_count=media_info[i][2], comments_count=media_info[i][3])


