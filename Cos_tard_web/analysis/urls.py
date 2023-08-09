from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('',views.index,name='analysis-page'),
    path('get_influencer',views.get_influencer,name="getinfluencer")
]