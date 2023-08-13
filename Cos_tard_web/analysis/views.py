from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from media4.models import *
from analysis.models import *
from analysis.processing import *
import json
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def get_influencer_infofix(request):
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
        return JsonResponse(influencer_data, safe=False)
    except Users_fix.DoesNotExist:
        return JsonResponse({'error': 'Influencer not found'}, status=404)

@csrf_exempt
def get_influencer_info(request):
    data = json.loads(request.body)
    influencer_name = data.get('influencer_name')
    try:
        influencer = Users_fix.objects.get(user_id=influencer_name)
        influencer_details = list(Users_info.objects.filter(ig_id=influencer.ig_id).order_by('-date')[:1].values())[0]
        influencer_data = {
            'follows_count': influencer_details.get('follows_count'),
            'followers_count': influencer_details.get('followers_count'),
            'media_count': influencer_details.get('media_count')
            # 다른 필요한 정보들도 추가할 수 있음
        }
        return JsonResponse(influencer_data, safe=False)
    except Users_fix.DoesNotExist:
        return JsonResponse({'error': 'Influencer not found'}, status=404)
    

    



# DB에서 검색해서 웹페이지에 결과 띄우는거 시험해보는중..
# def search_view(request):
#     if request.method == 'POST':
#         input_text = request.POST.get('search_text')
#         results = testTable.objects.filter(some_field__icontains=input_text)

#         # 검색 결과를 JSON 형식으로 반환하는 경우
#         # results_data = [{'some_field': item.some_field} for item in results]
#         # return JsonResponse(results_data, safe=False)

#         # 검색 결과를 HTML로 렌더링하여 반환하는 경우
#         return render(request, 'search_results.html', {'results': results})

#     return render(request, 'analysis.html')

@csrf_exempt
def get_influencer(request):
    data = json.loads(request.body)
    influencerName= data.get('influencerName')
    ig_id = Users_fix.objects.get(user_id=influencerName)
    follower_trend = follower_graph(ig_id)
    context = {
        'follower_trend' : follower_trend 
    }
    return render(request, 'analysis/analysis.html', context)