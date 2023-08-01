from django.shortcuts import render
from django.http import HttpResponse
from .models import Users

# Create your views here.
def index(request): 
    return render(request,'recommend/example.html')

#
#

# def Users_list(request):
#     User = Users.objects.all()
#     return render(request, 'recommend/example.html', {'User': User})
