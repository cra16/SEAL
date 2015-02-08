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

from selenium import webdriver	# 히스넷 체크를 위한 크롤링 모듈
from login.models import Profile	# 회원 추가 정보 model
from django.contrib.auth.models import User	# user model 등록

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
				
				Active = ["active","",""]

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
					   'Active' : Active,
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
			
				Active = ["active","",""]
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
					   'Active':Active,
					   })
			
def login(request):
    return render_to_response('login.html')
    
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/mysite2')

@csrf_exempt
def Confirm(request):
	return render_to_response('confirm.html')

@csrf_exempt
def HisnetCheck(request):
	hisnet_url = "http://hisnet.handong.edu/login/login.php"
	if request.method == 'POST':
		try:
			stu_num = request.POST['stu_num']
			hisnet_id = request.POST['hisnet_id']
			hisnet_pw = request.POST['hisnet_pw']
			
			if User.objects.filter(username=stu_num):
				render_to_response('stu_num_duplicate.html')

			# 히스넷 로그인
			driver = webdriver.PhantomJS(service_log_path='/opt/bitnami/python/lib/python2.7/site-packages/selenium/webdriver/phantomjs/ghostdriver.log')
			driver.get(hisnet_url)
			driver.set_window_size(1024,768)
			hisnet_main_frame = driver.find_element_by_name("MainFrame")
			driver.switch_to_frame(hisnet_main_frame)
			idinput = driver.find_element_by_name("id")
			idinput.send_keys(hisnet_id)
			pwinput = driver.find_element_by_name("password")
			pwinput.send_keys(hisnet_pw)
			login_button = driver.find_element_by_xpath("//input[@type='image'][@src='/2012_images/intro/btn_login.gif']")
			login_button.click()
			# 스크린샷 안찍으면 에러 발생. 이유는 불분명함. 추후 해결 필요.
			# driver.save_screenshot('/opt/bitnami/apps/django/django_projects/darkzero/hisnet_haksa.png')
			haksa_button = driver.find_element_by_xpath("//a[@href='/for_student/haksa_info/01.php']")
			haksa_button.click()
			# 학사 정보에서 학번 확인하기
			grade_info = driver.find_element_by_xpath("//form[@name='form1']/table/tbody/tr[2]/td[2]")
			# driver.save_screenshot('hisnet_haksa.png')
			h_stu_num = grade_info.text[7:]
			# 학사 정보에서 이름 확인하기
			name_info = driver.find_element_by_xpath("//form[@name='form1']/table/tbody/tr[1]/td[2]")
			h_stu_name = name_info.text[:3]
			major_info = driver.find_element_by_xpath("//form[@name='form1']/table/tbody/tr[6]/td[4]")
			first_major = major_info.text.split('.')[0]
			second_major = major_info.text.split('.')[1]

			# 학번 일치하는지 확인
			if stu_num == h_stu_num:
				ctx = {
					'stu_num':h_stu_num,
					'stu_name':h_stu_name,
					'first_major':first_major,
					'second_major':second_major,
				}

				return render_to_response('register.html', ctx)
		except:
			# 히스넷 체크 안될 시 에러페이지 출력
			return render_to_response('error.html')
	else:
		return render_to_response('login.html')

@csrf_exempt
def Register(request):
	if request.method=='POST':
		stu_num = request.POST['stu_num']
		user_pw = request.POST['user_pw']
		user_email = request.POST['user_email']
		user_name = request.POST['user_name']
		first_major = request.POST['first_major']
		second_major = request.POST.get('second_major', 'None')

		try:
			user = User.objects.create_user(username=stu_num, password=user_pw, email=user_email)
			user.save()
			get_user = User.objects.get(username=stu_num)
			profile = Profile(User=get_user, FirstMajor=first_major, SecondMajor=second_major, UserName=user_name)
			profile.save()
		except:
			# User를 만들었으나 Profile에서 실패할 경우 User만 등록되는 겨우가 발생함.
			# 예외처리로 User만 등록되었을 때를 위한 처리
			e_user = User.objects.filter(username=stu_num)
			if e_user:
				e_user.delete()
			render_to_response('error.html')

		return render_to_response('login.html')
		
	else:
		return render_to_response('login.html')


# Create your views here.
