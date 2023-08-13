from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('',views.get_influencer_infofix,name='analysis-page'),
    path('get_influencer_infofix',views.get_influencer_infofix,name="getinfluencerinfo"),
    path('',views.get_influencer_info,name='analysis-page'),
    path('get_influencer_info',views.get_influencer_info,name="getinfluencerinfo")
]