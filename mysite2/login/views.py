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
from index.models import *
from index.views import *

from selenium import webdriver	# 히스넷 체크를 위한 크롤링 모듈
from login.models import Profile	# 회원 추가 정보 model
from django.contrib.auth.models import User	# user model 등록

@csrf_exempt
def loginCheck(request):
		##로그인 할때 체킹하는 부분
		if request.method == 'POST':
			username = request.POST['UserID']
			userpassword = request.POST['UserPassword']
			user = authenticate(username = username, password=userpassword)
			##로그인 완료시 메인페이지 view
			if user is not None:
				auth_login(request,user)
				
				##메인 페이지 전공과 교양 보여주는 페이지
				CourseCode = MajorSelect(request.user)
				
				
				T_Count1 = Lecture.objects.filter(Q(Code__contains=CourseCode[0]) |Q(Code__contains= CourseCode[1])).count()
				T_Count2 = Lecture.objects.filter(Q(Code__contains= CourseCode[2]) | Q(Code__contains=CourseCode[3])).count()
				T_Count3 = Lecture.objects.count()

		

				##메인페이지 전공 교양 페이지 넘기는 것을 독립적으로 돌리는 기능
				PageInformation1 = [1,1,1];
				PageInformation2 = [1,1,1];
				PageInformation3 = [1,1,1];
						
				##페이지 넘기는 기능
				if T_Count1<11:
					PageInformation1[2] = 11
				else:
					PageInformation1[2] =T_Count1
				if T_Count2<11:
					PageInformation2[2] = 11
				else:
					PageInformation2[2] = T_Count2
				if T_Count3<11:
					PageInformation3[2] = 11
				else:
					PageInformation3[2] = T_Count3


				if CourseCode[0] !="ENG":
					TotalBoard1 = Lecture.objects.filter(Q(Code__contains = CourseCode[0]) | Q(Code__contains=CourseCode[1]))[(PageInformation1[1]-1)*5:(PageInformation1[1]-1)*5+5]
					TotalBoard2 = Lecture.objects.filter(Q(Code__contains = CourseCode[2]) | Q(Code__contains=CourseCode[3]))[(PageInformation2[1]-1)*5:(PageInformation2[1]-1)*5+5]
				else:
					TotalBoard1 = Lecture.objects.filter(Q(Code__contains =CourseCode[0]) |Q(Code__contains=CourseCode[1])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5]))[(PageInformation1[1]-1)*5:(PageInformation1[1]-1)*5+5]
					TotalBoard2 = Lecture.objects.filter(Q(Code__contains =CourseCode[2]) |Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5]))[(PageInformation2[1]-1)*5:(PageInformation1[1]-1)*5+5]
				TotalBoard3 = Lecture.objects.order_by('-id')[(PageInformation3[1]-1)*5:(PageInformation3[1]-1)*5+5] 
				
				PageBoard = PageView(TotalBoard1,TotalBoard2,TotalBoard3)

				##독립적 페이지 위치를 다음 페이지 넘기는 것할 때 정보 넘김
				request.session['PageInformation1'] = PageInformation1
				request.session['PageInformation2'] = PageInformation2
				request.session['PageInformation3'] = PageInformation3
				
				##보여주려는 페이지 자바스크립트 active
				Active = ["active","",""]

				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard':PageBoard,
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
		##조만간 패치하겠지만 위와 마찬가지 기능
		else:
				CourseCode = MajorSelect(request.user)
				
				T_Count1 = Lecture.objects.filter(Q(Code__contains=CourseCode[0]) |Q(Code__contains= CourseCode[1])).count()
				T_Count2 = Lecture.objects.filter(Q(Code__contains= CourseCode[2]) | Q(Code__contains=CourseCode[3])).count()
				T_Count3 = Lecture.objects.count()


				
				PageInformation1 = [1,1,1];
				PageInformation2 = [1,1,1];
				PageInformation3 = [1,1,1];
			

				if T_Count1<11:
					PageInformation1[2] = T_Count1
				else:
					PageInformation1[2] =11
				if T_Count2<11:
					PageInformation2[2] = T_Count2
				else:
					PageInformation2[2] = 11
				if T_Count3<11:
					PageInformation3[2] = T_Count3
				else:
					PageInformation3[2] = 11

				if CourseCode[0] !="ENG":
					TotalBoard1 = Lecture.objects.filter(Q(Code__contains = CourseCode[0]) | Q(Code__contains=CourseCode[1]))[(PageInformation1[1]-1)*5:(PageInformation1[1]-1)*5+5]
					TotalBoard2 = Lecture.objects.filter(Q(Code__contains = CourseCode[2]) | Q(Code__contains=CourseCode[3]))[(PageInformation2[1]-1)*5:(PageInformation2[1]-1)*5+5]
				else:
					TotalBoard1 = Lecture.objects.filter(Q(Code__contains =CourseCode[0]) |Q(Code__contains=CourseCode[1])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5]))[(PageInformation1[1]-1)*5:(PageInformation1[1]-1)*5+5]
					TotalBoard2 = Lecture.objects.filter(Q(Code__contains =CourseCode[2]) |Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5]))[(PageInformation2[1]-1)*5:(PageInformation2[1]-1)*5+5]
				TotalBoard3 = Lecture.objects.order_by('-id')[(PageInformation3[1]-1)*5:(PageInformation3[1]-1)*5+5]
				
				PageBoard = PageView(TotalBoard1,TotalBoard2,TotalBoard3)
			

				request.session['PageInformation1'] = PageInformation1
				request.session['PageInformation2'] = PageInformation2
				request.session['PageInformation3'] = PageInformation3
			
				Active = ["active","",""]
				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard':PageBoard,
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
			return render_to_response('confirm_error.html')
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



##main 페이지 강의 보여주는 기능(로그인에 쓰는거)
def PageView(TotalBoard1,TotalBoard2,TotalBoard3):
	PageBoard=[[],[],[]]


	for Board in TotalBoard1:
		try:
			Board1 = Total_Evaluation.objects.get(CourseName=Board)
		except :
			Board1 = None
		if Board1 is not None:
			Board1.Total_Speedy = Board1.Total_Speedy/Board1.Total_Count
			Board1.Total_Reliance = Board1.Total_Reliance/Board1.Total_Count
			Board1.Total_Helper = Board1.Total_Helper/Board1.Total_Count
			Board1.Total_Question = Board1.Total_Question/Board1.Total_Count
			Board1.Total_Exam = Board1.Total_Exam/Board1.Total_Count
			Board1.Total_Homework = Board1.Total_Homework/Board1.Total_Count
			PageBoard[0].append(Board1)
		else:
			Board1 = Total_Evaluation(CourseName=Board)
			Board1.Total_Speedy =5
			Board1.Total_Reliance =5
			Board1.Total_Helper = 5
			Board1.Total_Question = 5
			Board1.Total_Exam = 5
			Board1.Total_Homework = 5
			Board1.Total_Count =0
			PageBoard[0].append(Board1)
	for Board in TotalBoard2:
		try:
			Board2 = Total_Evaluation.objects.get(CourseName=Board)
		except :
			Board2 = None

		if Board2 is not None:
			Board2.Total_Speedy = Board2.Total_Speedy/Board2.Total_Count
			Board2.Total_Reliance = Board2.Total_Reliance/Board2.Total_Count
			Board2.Total_Helper = Board2.Total_Helper/Board2.Total_Count
			Board2.Total_Question = Board2.Total_Question/Board2.Total_Count
			Board2.Total_Exam = Board2.Total_Exam/Board2.Total_Count
			Board2.Total_Homework = Board2.Total_Homework/Board2.Total_Count
			PageBoard[1].append(Board2)
		else:
			Board2 = Total_Evaluation(CourseName=Board)
			Board2.Total_Speedy =5
			Board2.Total_Reliance =5
			Board2.Total_Helper = 5
			Board2.Total_Question = 5
			Board2.Total_Exam = 5
			Board2.Total_Homework = 5
			Board2.Total_Count =0
			PageBoard[1].append(Board2)
	for Board in TotalBoard3:
		try:
			Board3 = Total_Evaluation.objects.get(CourseName=Board)
		except :
			Board3 = None
		if Board3 is not None:
			Board3.Total_Speedy = Board3.Total_Speedy/Board3.Total_Count
			Board3.Total_Reliance = Board3.Total_Reliance/Board3.Total_Count
			Board3.Total_Helper = Board3.Total_Helper/Board3.Total_Count
			Board3.Total_Question = Board3.Total_Question/Board3.Total_Count
			Board3.Total_Exam = Board3.Total_Exam/Board3.Total_Count
			Board3.Total_Homework = Board3.Total_Homework/Board3.Total_Count
			PageBoard[2].append(Board3)
		else:
			Board3 = Total_Evaluation(CourseName=Board)
			Board3.Total_Speedy =5
			Board3.Total_Reliance =5
			Board3.Total_Helper = 5
			Board3.Total_Question = 5
			Board3.Total_Exam = 5
			Board3.Total_Homework = 5
			Board3.Total_Count =0
			PageBoard[2].append(Board3)
	return PageBoard

	# Create your views here.
