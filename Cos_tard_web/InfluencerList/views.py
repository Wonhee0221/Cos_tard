from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request): 
    
    influencer_dic = {

    'num1' : 'num1_url',
    'num2' : 'num2_url'

}

    return render(request,'InfluencerList/influencerList.html',context=influencer_dic)
