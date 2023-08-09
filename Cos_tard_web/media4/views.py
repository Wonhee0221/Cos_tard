from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import testmodel, Users_fix, Users_info, Media_fix, Media_info
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .crawling import *
from django.db import models
import uuid
import json

# Create your views here.
def index(request): 
    return render(request,'media4/media4.html')

@csrf_exempt
def save_name(request):
    data = json.loads(request.body)
    username = data.get('username')

        ##크롤링##

    admin_id = 17841402050732962
    token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"

    uf = crawl_users_fix(admin_id, token, username)
    ui = crawl_users_info(admin_id, token, username)
    mf = crawl_media_fix(admin_id, token, username)
    mi = crawl_media_info(admin_id, token, username)
    # print(uf,ui,mf,mi)

        ##중복으로 insert 전 삭제 코드##

    #Users_fix.objects.filter().delete() 
    #Users_info.objects.filter().delete()

        ##저장##
    users_fix = Users_fix()
    users_fix.ig_id=uf[0]
    users_fix.user_id=uf[1]
    users_fix.username=uf[2]
    users_fix.website=uf[3]
    users_fix.biography=uf[4]
    users_fix.save(force_insert=True)

    users_info = Users_info()
    users_info.uid=uuid.uuid4()
    users_info.ig_id=ui[0]
    users_info.date=ui[1]
    users_info.follows_count=ui[2]
    users_info.followers_count=ui[3]
    users_info.media_count=ui[4]
    users_info.save(force_insert=True)

    media_fix = Media_fix()
    for i in mf:
        media_fix.owner_id=i[0]
        media_fix.media_id=i[1]
        media_fix.caption=i[2]
        media_fix.media_url=i[3]
        media_fix.permalink=i[4]
        media_fix.timestamp=i[5]
        media_fix.save(force_insert=True)


    media_info = Media_info()
    for i in mi:
        media_info.uid=uuid.uuid4()
        media_info.media_id=i[0]
        media_info.date=i[1]
        media_info.like_count=i[2]
        media_info.comments_count=i[3]
        media_info.save(force_insert=True)

    return JsonResponse({'msg' : 'success'}, safe=False)

@csrf_exempt
def save_name_user_info(request):
    data = json.loads(request.body)
    user_info_id = data.get('user_info_id')

        ##크롤링##

    admin_id = 17841402050732962
    token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"

    ui = crawl_users_info(admin_id, token, user_info_id)
   
    # print(uf,ui,mf,mi)

        ##중복으로 insert 전 삭제 코드##

    #Users_fix.objects.filter().delete() 
    #Users_info.objects.filter().delete()

        ##저장##
    users_info = Users_info()
    users_info.uid=uuid.uuid4()
    users_info.ig_id=ui[0]
    users_info.date=ui[1]
    users_info.follows_count=ui[2]
    users_info.followers_count=ui[3]
    users_info.media_count=ui[4]
    users_info.save(force_insert=True)

    return JsonResponse({'msg' : 'success'}, safe=False)

@csrf_exempt
def all_user_info(request):
    data = json.loads(request.body)
    password = data.get('password')

        ##크롤링##

    admin_id = 17841400029634031
    token = "EAAKoyNOZAm4UBOZB2IZAQBu91Nq3vZBZCwpSsemWPYkcvEJdiXVLAUOF1M2eKnGABbVFtvYzipJjITU7oJqospRiQrFdPjRr51OQd2p8T4dBfbueEzJKuPxAO1iKHoQjF39LGmzGiL2ReNsqC3iOBMd4KDZBh7oFijQkElaelLSkOOUlKrmLIRw6oH"
    username=["a_arang_", "doublesoup", "calarygirl_a", "yulri_0i", "yeondukong", "lamuqe_magicup", "fallininm", "im_jella_",
            "hamnihouse", "ssinnim", "yu__hyewon", "hyojinc_", "leojmakeup", "2__yun__2", "areumsongee", "makeup_maker_",
            "r_yuhyeju", "vivamoon", "risabae_art", "yujin_so", "kisy0729", "ponysmakeup"]

    for i in username:
        ui = crawl_users_info(admin_id, token, i)
   
        # print(uf,ui,mf,mi)

            ##중복으로 insert 전 삭제 코드##

        #Users_fix.objects.filter().delete() 
        #Users_info.objects.filter().delete()

            ##저장##
        users_info = Users_info()
        users_info.uid=uuid.uuid4()
        users_info.ig_id=ui[0]
        users_info.date=ui[1]
        users_info.follows_count=ui[2]
        users_info.followers_count=ui[3]
        users_info.media_count=ui[4]
        users_info.save(force_insert=True)

    return JsonResponse({'msg' : 'success'}, safe=False)







