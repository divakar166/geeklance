from django.urls import path
from .views import *

urlpatterns = [
  path('users/',users,name='users'),
  path('userlogin/',userlogin,name='userlogin'),
  path('userregister/',userregister,name='userregister'),
  path('lancerregister/',lancerregister,name='lancerregister')

]