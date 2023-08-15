from django.shortcuts import render
from django.http import HttpResponse
from media4.models import *
from recommend.models import *
from recommend.utils import *
#from .models import Users

# Create your views here.
def index(request): 
    followers=followerslevel(4475701104)
    context = {'followers' : followers}
    return render(request,'recommend/recommend.html', context)

