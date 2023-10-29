from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import *
from django.contrib.auth.hashers import make_password
# Create your views here.
def users(request):
  data = UserProfile.objects.all()
  item_list = [{'name':item.first_name,'email':item.email} for item in data]
  return JsonResponse({'items':item_list})

@csrf_exempt
def userlogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    print(username,password)
    profile_obj = UserProfile.objects.filter(email=username)
    if not profile_obj.exists():
      data = {
        'message': "Account doesn't exist!"
      }
      return JsonResponse(data)
    if profile_obj[0]:
      data = {
        'message': "success",
        "userID":profile_obj[0].uid,
        "first_name":profile_obj[0].first_name,
        "last_name":profile_obj[0].last_name,
        "email":profile_obj[0].email
      }
      return JsonResponse(data)
    

@csrf_exempt
def userregister(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    password = data.get('password')
    hashed = make_password(password)
    profile_obj = UserProfile.objects.filter(email=email)
    if not profile_obj.exists():
      user = UserProfile.objects.create(first_name=first_name,last_name=last_name,email=email,password=hashed)
      user.save()
      data = {
        'message': "success",
        "userID":user.uid,
        "first_name":user.first_name,
        "last_name":user.last_name,
        "email":user.email
      }
      return JsonResponse(data)
    else:
      data = {
        'message': "Account already exist!"
      }
      return JsonResponse(data)


@csrf_exempt
def lancerlogin(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    profile_obj = lancer.objects.filter(email=username)
    if not profile_obj.exists():
      data = {
        'message': "Account doesn't exist!"
      }
      return JsonResponse(data)
    if profile_obj[0]:
      data = {
        'message': "success",
        "userID":profile_obj[0].uid,
        "first_name":profile_obj[0].first_name,
        "last_name":profile_obj[0].last_name,
        "email":profile_obj[0].email
      }
      return JsonResponse(data)

@csrf_exempt
def lancerregister(request):
  if request.method == 'POST':
    data = json.loads(request.body)
    first_name = data.get('firstName')
    last_name = data.get('lastName')
    email = data.get('email')
    password = data.get('password')
    hashed = make_password(password)
    profile_obj = lancer.objects.filter(email=email)
    if not profile_obj.exists():
      user = lancer.objects.create(first_name=first_name,last_name=last_name,email=email,password=hashed)
      user.save()
      data = {
        'message': "Registered Successfully!",
        "userID":user.uid,
        "first_name":user.first_name,
        "last_name":user.last_name,
        "email":user.email
      }
      return JsonResponse(data)
    else:
      data = {
        'message': "Account already exist!"
      }
      return JsonResponse(data)
