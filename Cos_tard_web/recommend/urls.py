from django.urls import path
from . import views

app_name = 'recommend'

urlpatterns = [
    path('',views.index,name='recommend-page'),
    path('recommend_values', views.recommend)
]