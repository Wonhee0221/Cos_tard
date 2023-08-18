from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('',views.index,name='analysis-page'),
    path('test',views.index_test,name='analysis-page2'),
    path('get_influencer',views.get_influencer),
    path('get_influencer_analysis',views.get_influencer_analysis)
    ]