from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from media4.models import *
from analysis.models import *
from analysis.processing import *
from analysis.hashtag import *
import json
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def get_influencer(request):
    data = json.loads(request.body)
    influencer_name = data.get('influencer_name')
    try:
        influencer = Users_fix.objects.get(user_id=influencer_name)
        influencer_data = {
            'userid': influencer.user_id,
            'username': influencer.username,
            'website': influencer.website,
            'biography': influencer.biography,
        }
        influencer_details = list(Users_info.objects.filter(ig_id=influencer.ig_id).order_by('-date')[:1].values())[0]
        influencer_data_details = {
            'follows_count': influencer_details.get('follows_count'),
            'followers_count': influencer_details.get('followers_count'),
            'media_count': influencer_details.get('media_count')
            # 다른 필요한 정보들도 추가할 수 있음
        }

        #팔로워 부분
        follower_trend = follower_graph(influencer.ig_id)

        image_link = get_image(influencer.ig_id)

        count_text = count_text_token(influencer.ig_id)
        count_hashtag=count_hashtags(influencer.ig_id)


        context = {
            'influencer_data' : influencer_data,
            'influencer_data_details' : influencer_data_details,
            'follower_trend' : follower_trend,
            'image_link' : image_link,
            'count_text' : count_text,
            'count_hashtag' : count_hashtag
            }


        return JsonResponse(context, safe=False)
    
    except Users_fix.DoesNotExist:
        return JsonResponse({'error': 'Influencer not found'}, status=404)