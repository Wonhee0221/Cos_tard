from django.urls import path
from . import views

app_name = 'media4'

urlpatterns = [
    path('',views.index,name='media4-page'),
    path('save_name',views.save_name),
    path('save_name_user_info',views.save_name_user_info),
    path('all_user_info',views.all_user_info)
]