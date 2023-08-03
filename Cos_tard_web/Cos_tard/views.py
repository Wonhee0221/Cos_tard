from django.http.response import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,'Cos_tard/home.html')

def about_view(request):
    return render(request,'Cos_tard/about.html')

def home_view2(request):
    return render(request, 'Cos_tard/home.html')
