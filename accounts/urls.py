from django.urls import path
from .views import *

urlpatterns = [
  path('users/',users,name='getData'),
  path('userlogin/',userlogin,name='getData')
]