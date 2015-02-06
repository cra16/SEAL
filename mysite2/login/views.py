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

# 히스넷 체크를 위한 크롤링 모듈
from selenium import webdriver

@csrf_exempt
def Register(request):
	if request.method=='POST':
		user_id = request.POST['user_id']
		user_pw = request.POST['user_pw']
		user_email = request.POST['user_email']
		
		User.object.create_user(username=user_id, password=user_pw, email=user_email)

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
				count=Lecture.objects.count()

				TotalCount = (count/8)+1

				if TotalCount ==1:
					Next = 1
				else:
					Next =TotalCount
				Previous=1
	
				PageBoard = Lecture.objects.order_by('-id')[0:7]	
				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard':PageBoard, 
					   'TotalCount' : range(0,TotalCount), 
					   'Previous' : Previous, 
					   'Next' : Next,
					   })
			else:
				return render_to_response('login.html')
         
		elif request.user.username =="":
			return render_to_response('login.html')
		else:
			count=Lecture.objects.count()

			TotalCount = (count/6)+1

			if TotalCount ==1:
				Next = 1
			else:
				Next =TotalCount
			Previous=1
	
			PageBoard = Lecture.objects.order_by('-id')[0:5]	
			return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard':PageBoard, 
					   'TotalCount' : range(0,TotalCount), 
					   'Previous' : Previous, 
					   'Next' : Next,
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
			driver.save_screenshot('/opt/bitnami/apps/django/django_projects/darkzero/hisnet_haksa.png')
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

			ctx = {
				'stu_num':h_stu_num[1:3],
				'stu_name':h_stu_name,
				'first_major':first_major,
				'second_major':second_major,
			}

			# 학번 일치하는지 확인
			if stu_num == h_stu_num:
				return render_to_response('register.html', ctx)
		except:
			# 히스넷 체크 안될 시 에러페이지 출력
			return render_to_response('error.html')
	else:
		return render_to_response('login.html')

# def hinset_login(stu_num, hisnet_id, hisnet_pw):
# 	info_lst = []
# 	return info_lst 



# Create your views here.
