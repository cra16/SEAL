# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from login.models import Profile
from functionhelper.views import CheckingLogin

import mechanize
from bs4 import BeautifulSoup
# django encoding
from django.utils.encoding import smart_str, smart_unicode

# Create your views here.
#암호 바꾸기
@csrf_exempt
def NicknameChange(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	else:
		if request.method =="POST":
			nickname = request.POST['Nickname']
			myprofile = Profile.objects.filter(User = request.user)
			is_same = Profile.objects.filter(UserName = nickname)
			if len(is_same) > 0:	# 중복 여부 검사
				return 'Duplicate error'		# 사실상 의도된 에러 발생.

			myprofile.update(UserName = nickname)
			if request.flavour =='full':
				return render_to_response('html/sealmypage.html')
			else:	
				return render_to_response("m_skins/m_html/sealmypage.html")

		else:
			if request.flavour =='full':
				return render_to_response('html/sealmypage.html')
			else:
				return render_to_response("m_skins/m_html/sealmypage.html")
@csrf_exempt
def Student_Information_Change(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	else:
		if request.method=="POST":
			myprofile = Profile.objects.get(User= request.user)
			hisnet_id = request.POST['hisnet_id']
			hisnet_pw = request.POST['hisnet_password']
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

			myprofile.FirstMajor= first_major
			if second_major==None:
				myprofile.SecondMajor="None"
			else:
				myprofile.SecondMajor=second_major
			try:
				myprofile.LectureRecord=all_rec
			except:
				raise Exception
			myprofile.save()
			ctx = {
				'stu_num': stu_num,
				'stu_name': stu_name,
				'first_major': first_major,
				'second_major': second_major,
				'all_rec': all_rec,
			}
			if request.flavour =='full':
				return render_to_response('html/sealmypage.html', ctx)
			else:
				return render_to_response('m_skins/m_html/agree_reg.html', ctx)