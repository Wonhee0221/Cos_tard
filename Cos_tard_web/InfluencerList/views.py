from django.shortcuts import render
from django.http import HttpResponse
from InfluencerList.models import *

# Create your views here.
    
#test insert 입니다   
#Menu.objects.create(name="커피")

def index(request): 
    
    influencer_dic = {

    'num1' : 'num1_url',
    'num2' : 'num2_url'

}

    return render(request,'InfluencerList/InfluencerList.html',context=influencer_dic)

