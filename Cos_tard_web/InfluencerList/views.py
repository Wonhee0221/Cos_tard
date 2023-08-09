from django.shortcuts import render
from django.http import HttpResponse
from media4.models import Users_fix, Users_info

# Create your views here.

def index(request): 

    selected_users_fix = Users_fix.objects.values('ig_id', 'user_id', 'username')
    #selected_users_info

    context = {'selected_users_fix': selected_users_fix}

    
    return render(request,'InfluencerList/influencerList.html',context)



