from django.shortcuts import render
from django.http import HttpResponse
from media4.models import Users_fix, Users_info
from django.db.models import Subquery, OuterRef

# Create your views here.

def index(request): 

    selected_users_fix = Users_fix.objects.values('ig_id', 'user_id', 'username','website')
    total_rows = Users_fix.objects.all().count()
    selected_users_info = Users_info.objects.order_by('-date')[:total_rows].values('ig_id', 'follows_count', 'followers_count', 'media_count', 'date')
    first_row = selected_users_info[0]
    date = first_row['date']

    joined_query = selected_users_info.annotate(
        user_id=Subquery(selected_users_fix.filter(ig_id=OuterRef('ig_id')).values('user_id')),
        username=Subquery(selected_users_fix.filter(ig_id=OuterRef('ig_id')).values('username')),
        website=Subquery(selected_users_fix.filter(ig_id=OuterRef('ig_id')).values('website'))
        )
    context = {'joined_query': joined_query, 'date': date }

    return render(request,'InfluencerList/influencerList.html',context)



