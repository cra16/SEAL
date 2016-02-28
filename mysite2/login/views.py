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

# from selenium import webdriver	# 히스넷 체크를 위한 크롤링 모듈
from login.models import Profile	# 회원 추가 정보 model
from django.contrib.auth.models import User	# user model 등록
from functionhelper.views import *
import mechanize
from bs4 import BeautifulSoup

@csrf_exempt
def loginCheck(request):
	##로그인 할때 체킹하는 부분
	Mobile = request.flavour
	if request.method == 'POST':
		if request.POST.get('id', 'None') == 'admin_seal':
			username = request.POST['id']
			password = request.POST['pw']
			user = authenticate(username=username, password=password)

		elif 'stu_num' in request.POST:	# 학번 값이 들어올 경우 해당 학번으로 로그인 제공.
			username = request.POST['stu_num']
			user = User.objects.filter(username=username)[0]

		elif 'stuNum' in request.POST:	# 학번 값이 들어올 경우 해당 학번으로 로그인 제공.
			if request.user.is_authenticated():	# 로그인 중일 때는 로그아웃 후에 재 로그인
				logout(request)
			username = request.POST['stuNum']
			if not username:
				LoginError(request)	# igo에서 받아온 값이 비어있을 경우 로그인 에러 발생
			try:
				user = User.objects.filter(username=username)[0]
			except IndexError:
				return HisnetCheck(request)
				# user = None
			
		elif request.POST.get('id', 'None'):
			username = request.POST['id']
			password = request.POST['pw']

			# 크롤링 Configuration
			browser = mechanize.Browser()
			browser.set_handle_robots(False)
			browser.open("https://hisnet.handong.edu/login/login.php")  
			browser.select_form(name='login') 
			browser.form['id'] = username
			browser.form['password'] = password  
			browser.submit()

			browser.open("https://hisnet.handong.edu/haksa/hakjuk/HHAK110M.php")
			contents = browser.response().read()
			soup = BeautifulSoup(contents, "html.parser")
			titles = soup.find_all(class_='tblcationTitlecls')
			# Save the information
			try:
				stu_num = titles[2].next_sibling.next_sibling.text[-8:]
				temp_major = titles[11].next_sibling.next_sibling.text.split('.')
				first_major = temp_major[0]
			except IndexError as e:
				return LoginError(request)	# 학번 혹은 전공 확인되지 않으면 로그인 에러
			try:
				second_major = temp_major[1]
			except IndexError as e:
				second_major = None

			try:
				user = User.objects.filter(username=stu_num)[0]
			except IndexError:
				return HisnetCheck(request)	# 해당 학번이 가입되지 않았을 경우 가입

		##로그인 완료시 메인페이지 view
		if user is not None:
			user.backend = 'django.contrib.auth.backends.ModelBackend'	# To login without password
			auth_login(request, user)
			#메인페이지 보여줄 함수 호출
			UserData = MainPageView(request.user,None,None,None,Mobile)
			request.session['PageInformation']=[[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
			if request.flavour =='full':
				return render_to_response('html/index.html',UserData)
			else:
				return render_to_response("m_skins/m_html/index.html",UserData)

		else:
			return LoginError(request)

	#로그인 되지 않았을 경우 다시 로그인페이지로
	elif request.user.username =="":
		if request.flavour =='full':
			return render_to_response('html/login.html')
		else:
			return render_to_response('m_skins/m_html/login.html')
			
	#이미 로그인 되어있으면 
	else:
		UserData = MainPageView(request.user,None,None,None,Mobile)
		request.session['PageInformation']=[[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
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

def LoginError(request):
	if request.flavour =='full':
		return render_to_response('html/login_error.html')
	else:
		return render_to_response("m_skins/m_html/login_error.html")

def Confirm(request):
	if request.flavour =='full':
		return render_to_response('html/confirm.html')
	else:
		return render_to_response('m_skins/m_html/confirm.html')

@csrf_exempt
def HisnetCheck(request):
	#hisnet_url = "http://hisnet.handong.edu/login/login.php"
	if request.method == 'POST':
		if 'stuNum' in request.POST:
			stu_num = request.POST['stuNum']
			stu_name = request.POST['usr_name']
			stu_major = request.POST['stuMajor'].split('.')
			first_major = stu_major[0].strip()
			try:
				second_major = stu_major[1].strip()
			except:
				second_major = None

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
			hisnet_id = request.POST['id']
			hisnet_pw = request.POST['pw']

			browser = mechanize.Browser()
			browser.set_handle_robots(False)
			browser.open("https://hisnet.handong.edu/login/login.php")  
			browser.select_form(name='login') 
			browser.form['id'] = hisnet_id
			browser.form['password'] = hisnet_pw  
			browser.submit()

			browser.open("https://hisnet.handong.edu/haksa/hakjuk/HHAK110M.php")
			contents = browser.response().read()
			soup = BeautifulSoup(contents, "html.parser")
			titles = soup.find_all(class_='tblcationTitlecls')
			# Save the information
			stu_name = titles[0].next_sibling.next_sibling.text[:-1]
			stu_num = titles[2].next_sibling.next_sibling.text[-8:]
			temp_major = titles[11].next_sibling.next_sibling.text.split()
			first_major = temp_major[0][:-1]

			try:
				second_major = temp_major[1]
			except IndexError as e:
				second_major = None

			browser.open("https://hisnet.handong.edu/haksa/record/HREC110M.php")
			record_contents = browser.response().read()
			record_soup = BeautifulSoup(record_contents, "html.parser")

			tables = record_soup.find_all(id='att_list')	# navigate to lecture list table
			all_rec = ''	# 전체 수강목록 string 초기화

			for i, table in enumerate(tables):
				if i < 2:
					continue
				trs = table.find_all('tr')
				# rec_semester = trs[0].text.split()[0]	# 수강 학기
				for i, tr in enumerate(trs):
					if i < 2:
						continue
					rec_code = tr.find('td')
					rec_name = rec_code.next_sibling.next_sibling
					all_rec += rec_code.text + '->' + rec_name.text + '$$'		# 구분자 '$$' 나중에 split하기 위함.
			all_rec = all_rec[:-2]	# 마지막 구분자 '$$'' 제거

			ctx = {
				'stu_num': stu_num,
				'stu_name': stu_name,
				'first_major': first_major,
				'second_major': second_major,
				'all_rec': all_rec,
			}

			if request.flavour =='full':
				return render_to_response('html/agree_reg.html', ctx)
			else:
				return render_to_response('m_skins/m_html/agree_reg.html', ctx)
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
		all_rec = request.POST['all_rec']

		try:
			user = User.objects.create_user(username=stu_num, password=user_pw, email=user_email)
			user.save()
			get_user = User.objects.get(username=stu_num)
			profile = Profile(User=get_user, FirstMajor=first_major, SecondMajor=second_major, UserName=user_name, LectureRecord=all_rec)
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
		all_rec = request.POST['all_rec']
		# 신입생 전공 비어있는 경우 직접 할당
		if not first_major:
			first_major = '글로벌리더십'

		try:
			user = User.objects.create_user(username=stu_num)
			user.save()
			get_user = User.objects.get(username=stu_num)
			profile = Profile(User=get_user, FirstMajor=first_major, SecondMajor=second_major, UserName=stu_name, LectureRecord=all_rec)
			profile.save()

		except:
			# User를 만들었으나 Profile에서 실패할 경우 User만 등록되는 겨우가 발생함.
			# 예외처리로 User만 등록되었을 때를 위한 처리
			e_user = User.objects.filter(username=stu_num)
			if e_user:
				e_user.delete()

			if request.flavour =='full':
				return render_to_response('html/stu_num_duplicate.html')
			else:
				return render_to_response('m_skins/m_html/stu_num_duplicate.html')	# m_skin 없음

		if request.flavour =='full':
			return loginCheck(request)
		else:
			return loginCheck(request)

	else:
		if request.flavour =='full':
			return render_to_response('html/login.html')
		else:
			return render_to_response('m_skins/m_html/login.html')