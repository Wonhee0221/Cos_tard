from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from media4.models import *
from analysis.models import *
from analysis.processing import *
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def index(request): 
    return render(request,'analysis/analysis.html')


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
    influencer_name = data.get('influencer_name')
    ig_id = Users_fix.objects.filter(ig_id=influencer_name).values('ig_id')
    follower_trend = follower_graph(ig_id) #from function in processing file

    context = {
        'follower_trend' : follower_trend
    }
    return render(request,'analysis/analysis.html',context)