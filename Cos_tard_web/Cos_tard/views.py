from django.http.response import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,'Cos_tard/home.html')

def about_view(request):
    return render(request,'Cos_tard/about.html')

# 8/6 추가한 코드 by.조민환
def influencerList_view(request):
    return render(request, 'InfluencerList/influencerList.html')

#8/7 추가한 코드 by.조민환
def recommend_view(request):
    return render(request, 'recommend/recommend.html')

def analysis_view(request):
    return render(request, 'analysis/analysis.html')