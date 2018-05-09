from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,logout,login
from  django.conf import settings
import os,re,json
from web import models
#from backend.task_manager import MultiTaskManger

from backend import audit
# Create your views here.

@login_required
def dashboard(request):
    return render(request,'index.html')
