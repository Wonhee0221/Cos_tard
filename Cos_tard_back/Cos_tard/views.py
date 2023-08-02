from django.http.response import HttpResponse
from django.shortcuts import render

def home_view(request):
    return render(request,'Cos_tard/home_page.html')
