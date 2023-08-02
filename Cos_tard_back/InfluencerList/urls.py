from django.urls import path
from . import views

app_name = 'InfluencerList'

urlpatterns = [
    path('',views.index, name='InfluencerList-page')
]