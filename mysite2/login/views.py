# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from login.forms import *
from lecture.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

@csrf_exempt
def Register(request):
	if request.method=='POST':
		UserID = request.POST['userID']
		UserPassword =request.POST['userpassword']
		UserEmail = request.POST['email']
		
		User.object.create_user(username =UserID, password = UserPassword, email=UesrEmail)

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

				PageBoard1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP"))[0:5]
				PageBoard2 = Lecture.objects.filter(Code__contains = "SIE")[0:5]
				PageBoard3 = Lecture.objects.order_by('-id')[0:5]

				TotalCount1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP")).count()
				TotalCount2 =  Lecture.objects.filter(Code__contains = "SIE").count()
				TotalCount3 =  Lecture.objects.count()
				
				PageInformation1 = [0,0,0];
				PageInformation2 = [0,0,0];
				PageInformation3 = [0,0,0];
				
				PageInformation1[0] = 1
				PageInformation2[0] = 1
				PageInformation3[0] = 1
				
				PageInformation1[1] = 1
				PageInformation2[1] = 1
				PageInformation3[1] = 1
		

				if TotalCount1<11:
					PageInformation1[2] = 11
				else:
					PageInformation1[2] =TotalCount1
				if TotalCount2<11:
					PageInformation2[2] = 11
				else:
					PageInformation2[2] = TotalCount2
				if TotalCount3<11:
					PageInformation3[2] = 11
				else:
					PageInformation3[2] = TotalCount3
				

				request.session['PageInformation1'] = PageInformation1
				request.session['PageInformation2'] = PageInformation2
				request.session['PageInformation3'] = PageInformation3
				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard1':PageBoard1,
					   'PageBoard2':PageBoard2,
					   'PageBoard3':PageBoard3,
					   'TotalCount1' : range(1,11),
					   'TotalCount2' : range(1,11),
					   'TotalCount3' : range(1,11),
					   'PageInformation1' : PageInformation1,
					   'PageInformation2' : PageInformation2,
					   'PageInformation3' : PageInformation3,
					   })
			else:
				return render_to_response('login.html')
         
		elif request.user.username =="":
			return render_to_response('login.html')
		else:
	
				PageBoard1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP"))[0:5]
				PageBoard2 = Lecture.objects.filter(Code__contains = "SIE")[0:5]
				PageBoard3 = Lecture.objects.order_by('-id')[0:5]
			
				TotalCount1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP")).count()
				TotalCount2 =  Lecture.objects.filter(Code__contains = "SIE").count()
				TotalCount3 =  Lecture.objects.count()

				PageInformation1 = [0,0,0];
				PageInformation2 = [0,0,0];
				PageInformation3 = [0,0,0];
				
				PageInformation1[0] = 1
				PageInformation2[0] = 1
				PageInformation3[0] = 1
				
				PageInformation1[1] = 1
				PageInformation2[1] = 1
				PageInformation3[1] = 1
		

				if TotalCount1<11:
					PageInformation1[2] = 11
				else:
					PageInformation1[2] =TotalCount1
				if TotalCount2<11:
					PageInformation2[2] = 11
				else:
					PageInformation2[2] = TotalCount2
				if TotalCount3<11:
					PageInformation3[2] = 11
				else:
					PageInformation3[2] = TotalCount3
				

				request.session['PageInformation1'] = PageInformation1
				request.session['PageInformation2'] = PageInformation2
				request.session['PageInformation3'] = PageInformation3
			
				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard1':PageBoard1,
					   'PageBoard2':PageBoard2,
					   'PageBoard3':PageBoard3,
					   'TotalCount1' : range(1,11),
					   'TotalCount2' : range(1,11),
					   'TotalCount3' : range(1,11),
					   'PageInformation1' : PageInformation1,
					   'PageInformation2' : PageInformation2,
					   'PageInformation3' : PageInformation3,
					   'Path':request.path,
					   })
			
      
	

def login(request):
    return render_to_response('login.html')
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/mysite2')


    

@csrf_exempt
def Confirm(request):
	
	if request.method =='POST':
		UserStuNumber = request.POST['year']
		UserName = request.POST['username']
		UserPassword = request.POST['userpassword']

		return render_to_response('register.html')

	else :
		return render_to_response('confirm.html')


# Create your views here.
