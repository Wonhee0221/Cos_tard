from django.shortcuts import render
from django.http import HttpResponse

from InfluencerList.models import *
from InfluencerList.crawling import *

# Create your views here.
def index(request): 
    return HttpResponse("View inside media4")

