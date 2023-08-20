from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from media4.models import *
from analysis.models import *
from analysis.processing import *
from analysis.hashtag import *
import json
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models.functions import TruncDate
from datetime import datetime

# Create your views here.

def index_test(request):
    ig_id = request.GET.get('ig_id')
    return render(request,'analysis/index.html',{'ig_id':ig_id})

@csrf_exempt
def get_influencer_analysis(request):
    data = json.loads(request.body)
    ig_id = data.get('ig_id')

    influencer = Users_fix.objects.get(ig_id=ig_id)
    influencer_data = {
        'userid': influencer.user_id,
        'username': influencer.username,
        'website': influencer.website,
        'biography': influencer.biography,
    }
    influencer_details = list(Users_info.objects.filter(ig_id=ig_id).order_by('-date')[:1].values())[0]
    influencer_data_details = {
        'follows_count': influencer_details.get('follows_count'),
        'followers_count': influencer_details.get('followers_count'),
        'media_count': influencer_details.get('media_count'),
         'date': influencer_details.get('date')
        # 다른 필요한 정보들도 추가할 수 있음
    }
    follower = influencer_details.get('followers_count')
    
    #팔로워 부분
    follower_trend = follower_graph(ig_id)

    #피드미리보기
    image_link = get_image(ig_id)

    #좋아요max피드
    media_data = get_media_data(ig_id)

    #키워드분석
    count_text = count_text_token(influencer.ig_id)
    count_hashtag=count_hashtags(influencer.ig_id)

    statistic = get_statistic(ig_id,follower)
    ratio = get_ratio(ig_id)

    context = {
        'influencer_data' : influencer_data,
        'influencer_data_details' : influencer_data_details,
        'follower_trend' : follower_trend,
        'image_link' : image_link,
        'count_text' : count_text,
        'count_hashtag' : count_hashtag,
        'media_data' : media_data,
        'statistic' : statistic,
        'ratio' : ratio

    }

    return JsonResponse(context, safe=False)



