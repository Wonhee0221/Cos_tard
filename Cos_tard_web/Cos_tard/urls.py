"""
URL configuration for Cos_tard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [
    path('',views.home_view,name='home-page'),
    path('about/',views.about_view,name='about-page'),
    path('InfluencerList/',include('InfluencerList.urls')),
    path('analysis/',include('analysis.urls')),
    path('recommend/',include('recommend.urls')),
    path('media4/',include('media4.urls')),
    path('admin/', admin.site.urls),

    # 8/5 추가한 코드 by.조민환
    path('home.html',views.home_view,name='home-page'),
    path('about.html',views.about_view,name='about-page'),

    # 8/6 추가한 코드 by.조민환
    path('InfluencerList/',views.influencerList_view,name='list-page'),
    path('recommend/recommend.html',views.recommend_view,name='recommend-page'),
    path('analysis/analysis.html',views.analysis_view,name="analysis-page")
]
