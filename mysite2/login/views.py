# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

# login app 정리 부분적으로 완료(2/22)

from lecture.models import *#강의 목록
from django.contrib.auth.decorators import login_required#로그인 허용기능
from django.contrib.auth import logout #로그아웃 기능
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q #데이터 베이스 OR 기능 구현
from index.models import * #아직 시험중
from index.views import MajorSelect, PageView#전공 선택 및 페이지 메인 페이지 보여주는 함수를 불러옴

from selenium import webdriver	# 히스넷 체크를 위한 크롤링 모듈
from login.models import Profile	# 회원 추가 정보 model
from django.contrib.auth.models import User	# user model 등록
from functionhelper.views import *

@csrf_exempt
def loginCheck(request):
	##로그인 할때 체킹하는 부분
	if request.method == 'POST':
		if 'stuNum' in request.POST:	# 학번 값이 들어올 경우 해당 학번으로 로그인 제공.
			if not request.POST['stuNum']:
				return HttpResponse("igo에서 다시 로그인해주세요.")
			if request.user.is_authenticated():	# 로그인 중일 때는 로그아웃 후에 재 로그인
				logout(request)
			username = request.POST['stuNum']
			try:
				user = User.objects.filter(username=username)[0]
			except IndexError:
				return HisnetCheck(request)
				# user = None
		else:
			username = request.POST['UserID']
			userpassword = request.POST['UserPassword']
			user = authenticate(username = username, password=userpassword)
		##로그인 완료시 메인페이지 view
		if user is not None:
			user.backend = 'django.contrib.auth.backends.ModelBackend'	# To login without password
			auth_login(request, user)
			#메인페이지 보여줄 함수 호출
			UserData = MainPageView(request.user,None,None,None)
			request.session['PageInformation']=[[1,1,1],[1,1,1],[1,1,1]]
			if request.flavour =='full':
				return render_to_response('html/index.html',UserData)
			else:
				return render_to_response("m_skins/m_html/index.html",UserData)
		else:
			if request.flavour =='full':
				return render_to_response('html/login_error.html')
			else:
				return render_to_response("m_skins/m_html/login_error.html")
	#로그인 되지 않았을 경우 다시 로그인페이지로
	elif request.user.username =="":
		if request.flavour =='full':
			return render_to_response('html/login.html')
		else:
			return render_to_response('m_skins/m_html/login.html')
	#이미 로그인 되어있으면 
	else:
		UserData = MainPageView(request.user,None,None,None)
		request.session['PageInformation']=[[1,1,1],[1,1,1],[1,1,1]]
		if request.flavour =='full':
			return render_to_response('html/index.html',UserData)
		else:
			return render_to_response("m_skins/m_html/index.html", UserData)
#로그인 페이지	
def login(request):
	if request.flavour =='full':
		return render_to_response('html/login.html')
	else:
		return render_to_response('m_skins/m_html/login.html')
#로그아웃
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def Confirm(request):
	if request.flavour =='full':
		return render_to_response('html/confirm.html')
	else:
		return render_to_response('m_skins/m_html/confirm.html')

@csrf_exempt
def HisnetCheck(request):
	hisnet_url = "http://hisnet.handong.edu/login/login.php"
	if request.method == 'POST':
		if 'stuNum' in request.POST:
			stu_num = request.POST['stuNum']
			stu_name = request.POST['usr_name']
			stu_major = request.POST['stuMajor'].split('.')
			first_major = stu_major[0].strip()
			second_major = stu_major[1].strip()

			ctx = {
				'stu_num': stu_num,
				'stu_name': stu_name,
				'first_major': first_major,
				'second_major': second_major,
			}

			if request.flavour =='full':
				return render_to_response('html/agree_reg.html', ctx)
			else:
				return render_to_response('m_skins/m_html/agree_reg.html', ctx)

		else:
			try:
				hisnet_id = request.POST['hisnet_id']
				hisnet_pw = request.POST['hisnet_pw']
				
				if User.objects.filter(username=stu_num):
					# return render_to_response('html/stu_num_duplicate.html')
					return render_to_response('html/stu_num_duplicate.html')

				# 히스넷 로그인
				driver = webdriver.PhantomJS(service_log_path='/opt/bitnami/python/lib/python2.7/site-packages/selenium/webdriver/phantomjs/ghostdriver.log')
				driver.get(hisnet_url)
				driver.set_window_size(1024,768)
				main_login_frame = driver.find_element_by_name("MainFrame")
				driver.switch_to_frame(main_login_frame)
				idinput = driver.find_element_by_name("id")
				idinput.send_keys(hisnet_id)
				pwinput = driver.find_element_by_name("password")
				pwinput.send_keys(hisnet_pw)
				login_button = driver.find_element_by_xpath("//input[@type='image'][@src='/2012_images/intro/btn_login.gif']")
				login_button.click()
				# 로그인 이후 지연시간 발생 예외처리
				while True:
					try:
						driver.get("https://hisnet.handong.edu/haksa/hakjuk/HHAK110M.php")	# 학사정보 접근
						# haksa_button = driver.find_element_by_xpath("//a[@href='/for_student/haksa_info/01.php']")
						break
					except:
						continue
				# haksa_button.click()
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
					'stu_num':h_stu_num,
					'stu_name':h_stu_name,
					'first_major':first_major,
					'second_major':second_major,
				}

				# # 수강정보 들어가기 *에러발생 시 반복수행
				# sugang_button = driver.find_element_by_xpath("//a[@href='/for_student/course/01.php']")
				# sugang_button.click()

				# # 시간표 읽어들이기
				# lecture_lst = []
				# for period in range(2,12):
				# 	for day in range(2,8):
				# 		detail = {}	# 딕셔너리 초기화
				# 		try:
				# 		# xpath 각각의 딕셔너리 사용 방법
				# 		# detail['name'] = driver.find_element_by_xpath("//table[@id='att_list']/tbody/tr[%d]/td[%d]/a/font[1]" % (period, day)).text
				# 		# detail['prof'] = driver.find_element_by_xpath("//table[@id='att_list']/tbody/tr[%d]/td[%d]/a/font[2]" % (period, day)).text
				# 		# detail['room'] = driver.find_element_by_xpath("//table[@id='att_list']/tbody/tr[%d]/td[%d]/a/font[3]" % (period, day)).text

				# 			# 텍스트로 분류 방법
				# 			t_text = driver.find_element_by_xpath("//table[@id='att_list']/tbody/tr[%d]/td[%d]" % (period, day)).text
				# 			t_lst = t_text.split('\n')
				# 			detail['name'] = t_lst[0]
				# 			detail['prof'] = t_lst[1]
				# 			detail['room'] = t_lst[2]

				# 			# 시간표 찾기 위한 장치
				# 			detail['period'] = period
				# 			detail['day'] = day

				# 			lecture_lst.append(detail)
				# 		except:
				# 			continue
				# ctx['lecture_lst'] = lecture_lst
				
				if request.flavour =='full':
					return render_to_response('html/register.html', ctx)
				else:
					return render_to_response('m_skins/m_html/register.html', ctx)
			except:
				# 히스넷 체크 안될 시 에러페이지 출력
				if request.flavour =='full':
					return render_to_response('html/confirm_error.html')
				else:
					return render_to_response('m_skins/m_html/confirm_error.html')
	else:
		if request.flavour =='full':
			return render_to_response('html/login.html')
		else:
			return render_to_response('m_skins/m_html/login.html')

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
			if request.flavour =='full':
				render_to_response('html/error.html')
			else:
				render_to_response('m_skins/m_html/error.html')
		if request.flavour =='full':
			return HttpResponseRedirect('/')
		else:
			return render_to_response('m_skins/m_html/login.html')
		
	else:
		if request.flavour =='full':
			return render_to_response('html/login.html')
		else:
			return render_to_response('m_skins/m_html/login.html')

@csrf_exempt
def RegisterInfo(request):
	if request.method=='POST':
		stu_num = request.POST['stu_num']
		stu_name = request.POST['stu_name']
		first_major = request.POST['first_major']
		second_major = request.POST.get('second_major', 'None')

		try:
			user = User.objects.create_user(username=stu_num)
			user.save()
			get_user = User.objects.get(username=stu_num)
			profile = Profile(User=get_user, FirstMajor=first_major, SecondMajor=second_major, UserName=stu_name)
			profile.save()
		except:
			# User를 만들었으나 Profile에서 실패할 경우 User만 등록되는 겨우가 발생함.
			# 예외처리로 User만 등록되었을 때를 위한 처리
			e_user = User.objects.filter(username=stu_num)
			if e_user:
				e_user.delete()

			if request.flavour =='full':
				render_to_response('html/stu_num_duplicate.html')
			else:
				render_to_response('m_skins/m_html/stu_num_duplicate.html')	# m_skin 없음

		if request.flavour =='full':
			return HttpResponseRedirect('/')
		else:
			return render_to_response('m_skins/m_html/login.html')

	else:
		if request.flavour =='full':
			return render_to_response('html/login.html')
		else:
			return render_to_response('m_skins/m_html/login.html')