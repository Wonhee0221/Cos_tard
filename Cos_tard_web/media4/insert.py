from django.shortcuts import render, redirect
from .models import testmodel, Users_fix, Users_info, Media_fix, Media_info
from .crawling import *
from django.db import models
import uuid

##크롤링 후 저장##
# admin_id = 17841402050732962
# token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"
# username = " "

# uf = crawl_users_fix(admin_id, token, username)
# ui = crawl_users_info(admin_id, token, username)
# mf = crawl_media_fix(admin_id, token, username)
# mi = crawl_media_info(admin_id, token, username)

##데이터 저장##
# uf=[]
# ui=[]
# mf=[]
# mi=[]

# users_fix = Users_fix()
# users_fix.ig_id=uf[0]
# users_fix.user_id=uf[1]
# users_fix.username=uf[2]
# users_fix.website=uf[3]
# users_fix.biography=uf[4]
# users_fix.save(force_insert=True)

# users_info = Users_info()
# users_info.uid=uuid.uuid4()
# users_info.ig_id=ui[0]
# users_info.date=ui[1]
# users_info.follows_count=ui[2]
# users_info.followers_count=ui[3]
# users_info.media_count=ui[4]
# users_info.save(force_insert=True)

# media_fix = Media_fix()
# for i in mf:
#     media_fix.owner_id=i[0]
#     media_fix.media_id=i[1]
#     media_fix.caption=i[2]
#     media_fix.media_url=i[3]
#     media_fix.permalink=i[4]
#     media_fix.timestamp=i[5]
#     media_fix.save(force_insert=True)


# media_info = Media_info()
# for i in mi:
#     media_info.uid=uuid.uuid4()
#     media_info.media_id=i[0]
#     media_info.date=i[1]
#     media_info.like_count=i[2]
#     media_info.comments_count=i[3]
#     media_info.save(force_insert=True)
