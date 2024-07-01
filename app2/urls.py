from django.urls import path
from app2.views import *
app_name='rcbteam'

urlpatterns=[
    path('virat/',virat,name='virat'),
    
]