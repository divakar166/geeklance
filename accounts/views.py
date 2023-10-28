from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.contrib.auth.hashers import make_password
# Create your views here.
def users(request):
  data = UserProfile.objects.all()
  item_list = [{'name':item.first_name,'mobile':item.mobile} for item in data]
  return JsonResponse({'items':item_list})

@csrf_exempt
def userlogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    profile_obj = UserProfile.objects.filter(email=username)
    if profile_obj.exists():
      return JsonResponse({'data':'kr rhe h'})
    else:
      return JsonResponse({'data':'User doesnt exist!'})
  return JsonResponse({'res':'kuch ni hua'})

@csrf_exempt
def userregister(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    hashed = make_password(password)
    profile_obj = UserProfile.objects.filter(email=email)
    if not profile_obj.exists():
      user = UserProfile.objects.create(first_name=first_name,last_name=last_name,email=email,password=hashed)
      user.save()
      return JsonResponse({'data':user})
    else:
      return JsonResponse({'data':'user already exist!'})


@csrf_exempt
def lancerlogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    profile_obj = lancer.objects.filter(email=username)
    if profile_obj.exists():
      return JsonResponse({'data':'kr rhe h'})
    else:
      return JsonResponse({'data':'User doesnt exist!'})
  return JsonResponse({'res':'kuch ni hua'})

@csrf_exempt
def lancerregister(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')
    hashed = make_password(password)
    profile_obj = lancer.objects.filter(email=email)
    if not profile_obj.exists():
      user = lancer.objects.create(firt_name=first_name,last_name=last_name,email=email,password=hashed)
      user.save()
      return JsonResponse({'data':user})
    else:
      return JsonResponse({'data':'user already exist!'})
