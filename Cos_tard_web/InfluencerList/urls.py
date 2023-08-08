from django.urls import path
from . import views

app_name = 'InfluencerList'

urlpatterns = [
    path('index',views.index, name='list-page')
]