from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import testmodel
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from InfluencerList.crawling import *

# Create your views here.
def index(request): 
    return render(request,'media4/media4.html')

@csrf_exempt
def save_name(request):
    data = json.loads(request.body)
    username = data.get('username')

    admin_id = 17841402050732962
    token = "EAAIvJjhX7PgBO9abNiUoqdZBEc9cSUjW1J9Up1ZCMXiBlJNrmYL4rEiZAjPXHKpZCuZAzE9okSwYUgyTAOYKcdI5iTNv0nD7vq5jVXEIO37dtm0YccPtlGdIozP7A0VeVQ6FZCjysZCdETKBqVVqLP0fiLqzpFthXauUsMj8bgJZBTSdG0BDjTLIBW3BToEwbkwZD"

    uf = crawl_users_fix(admin_id, token, username)

    print(uf)

    return JsonResponse({'msg' : 'success'}, safe=False)

