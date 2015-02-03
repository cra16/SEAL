# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


def Register(request):
	if request.method=='POST':
		UserID = request.POST['username']
		UserPassword =request.POST['userpassword']
		UserEmail = request.POST['email']
		

		return render_to_response('login.html')
	else:
		return render_to_response('login.html')


	

    

@csrf_exempt
def loginCheck(request):
		if request.method == 'POST':
			username = request.POST['UserID']
			userpassword = request.POST['UserPassword']
			user = authenticate(username = username, password=userpassword)
			if user is not None:
				auth_login(request,user)
				return render_to_response('index.html',{'user':request.user})
			else:
				return render_to_response('login.html')
         
		elif request.user.username =="":
			return render_to_response('login.html')
		else:
			return render_to_response('index.html',{'user':request.user})
		
      
	

def login(request):
    return render_to_response('login.html')
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/mysite2')

def index(request):
    return render_to_response('index.html')


def Confirm(request):
	
	if request.method =='POST':
		UserStuNumber = request.POST['year']
		UserName = request.POST['username']
		UserPassword = request.POST['userpassword']

		return render_to_response('register.html')

	else :
		return render_to_response('confirm.html')


# Create your views here.
