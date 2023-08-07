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

users = crawl_users(admin_id, token, "rkasl_")
Users_fix.objects.create(ig_id=users[0], user_id=users[1], username= users[2], biography=users[3], website="wlqdprkrhtlvek")

