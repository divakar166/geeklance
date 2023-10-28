from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
# Create your views here.
def users(request):
  data = UserProfile.objects.all()
  item_list = [{'name':item.first_name,'mobile':item.mobile} for item in data]
  return JsonResponse({'items':item_list})

def userlogin(request):
  return JsonResponse({'res':'Success'})