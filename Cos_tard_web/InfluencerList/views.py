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

admin_id = 17841402050732962
token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"
username="rkasl_"

users_fix = crawl_users_fix(admin_id, token, username)
users_fix = crawl_users_info(admin_id, token, username)
users_fix = crawl_media_fix(admin_id, token, username)
users_fix = crawl_media_info(admin_id, token, username)


#Users_fix.objects.create(ig_id=users_fix[0], user_id=users_fix[1], username= users_fix[2], website=users_fix[3], biography=users_fix[4])

