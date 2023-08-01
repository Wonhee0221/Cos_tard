from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='recommend-page'),
    #path('',views.Users_list,name='recommend-page')
]