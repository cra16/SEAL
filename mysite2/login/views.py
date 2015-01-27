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


def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            return HttpResponseRedirect('success')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {'form' : form})
    
    return render_to_response('register.html', variables)

def register_success(request):
    return render_to_response('success.html',)
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

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
    
def loginSuccess(request):
    return HttpResponseRedirect('/mysite2/home')

def index(request):
    return render_to_response('index.html')

# Create your views here.
