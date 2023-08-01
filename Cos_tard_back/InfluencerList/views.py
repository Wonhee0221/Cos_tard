from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


influencer_dic = {

    'num1' : 'num1_url',
    'num2' : 'num2_url'

}
     
def index(request,key): 
    return HttpResponse(influencer_dic[key])

