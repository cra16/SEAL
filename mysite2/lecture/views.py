# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from lecture.models import Lecture
import xlrd
# selenium module
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# csrf
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def func_strip(arg):
	if type(arg) == str:
		return arg.strip()
	return arg

def UpdateLogin(request):
	return render_to_response('html/DBUpdate.html')

@csrf_exempt
def auto_lec_update(request):
	"""
	Hisnet 개설시간표 자동 update function
	"""
	if request.method == 'POST':
		hisnet_id = request.POST['HisnetID']
		hisnet_pw = request.POST['HisnetPassword']
		hisnet_url = "http://hisnet.handong.edu/login/login.php"
		hak_year = "2015"
		hak_term = "2"
		cur_semester = "15-2"
		hakbu_lst = [
			'0001', '0009', '0010', '0011',
			'0012', '0021', '0022', '0024',
			'0033', '0071', '0074', '0077',
			'0078', '0090'
		]	# 학부 코드 list
		# hakbu_lst = ['0071']	# Debug list

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

		all_info_lst = []
		for hakbu in hakbu_lst:
			# 학부 설정 후 첫페이지 이동
			first_link = "https://hisnet.handong.edu/for_student/course/PLES330M.php?hak_year=" \
			 + hak_year \
			 + "&hak_term=" \
			 + hak_term \
			 + "&prof_name=&gwamok=&gwamok_code=&hakbu=" \
			 + hakbu \
			 + "&isugbn=%C0%FC%C3%BC&injung=%C0%FC%C3%BC&ksearch=search"
			driver.get(first_link)

			try:
				link_02 = driver.find_element_by_link_text("02")	# 2page 없으면 1page 만 존재
				last_button = driver.find_element_by_xpath("//img[@src='/myboard/images/btn_say_last.gif']")	# 마지막 페이지 이동 버튼
				last_button.click()
			except NoSuchElementException as e:
				pass
			
			last_num = int(driver.find_element_by_class_name("orangebold").text)	# 마지막 페이지 number

			hakbu_info_lst = []
			for page in range(1, last_num+1):	# from 1 to last_num
				href = "https://hisnet.handong.edu/for_student/course/PLES330M.php?Page=" \
				 + str(page) \
				 + "&hak_year=" \
				 + hak_year \
				 + "&hak_term=" \
				 + hak_term \
				 + "&prof_name=&gwamok=&gwamok_code=&hakbu=" \
				 + hakbu \
				 + "&isugbn=%C0%FC%C3%BC&injung=%C0%FC%C3%BC&ksearch=search"
				driver.get(href)
				for i in range(2, 17):	# 1 page 당 15 강의, 1번째는 컬럼명
					try:
						lec_parent = driver.find_element_by_xpath("//table[@id='att_list']/tbody/tr["+ str(i) + "]")
						lec_category = lec_parent.find_element_by_xpath("./td[1]").text 	# 과목구분
						lec_code = lec_parent.find_element_by_xpath("./td[2]").text 	# 과목코드
						lec_class = lec_parent.find_element_by_xpath("./td[3]").text 	# 과목분반
						lec_name = lec_parent.find_element_by_xpath("./td[4]").text 	# 과목명
						kr_name = lec_name.split('\n')[0]
						en_name = lec_name.split('\n')[1][1:-1]	# 괄호 제외
						lec_credit = lec_parent.find_element_by_xpath("./td[5]").text 	# 과목학점
						lec_major = lec_parent.find_element_by_xpath("./td[6]").text.split('\n')[0] # 강의전공
						lec_prof = lec_parent.find_element_by_xpath("./td[6]/font").text # 강의교수
						lec_period = lec_parent.find_element_by_xpath("./td[7]").text 	# 강의시간
						kr_period = lec_period.split('\n')[0]	# 강의시간(한글)
						lec_room = lec_parent.find_element_by_xpath("./td[8]").text 	# 강의실
						lec_fix_num = lec_parent.find_element_by_xpath("./td[9]").text # 수강정원
						lec_take_num = lec_parent.find_element_by_xpath("./td[10]").text # 수강인원
						lec_eng_ratio = lec_parent.find_element_by_xpath("./td[11]").text # 영어비율
						lec_category_detail = lec_parent.find_element_by_xpath("./td[12]").text # 교양실무
						temp_lec = (
							lec_category, lec_code, lec_class, kr_name,
							lec_credit,  lec_major,  kr_period, lec_room,
							lec_fix_num, lec_take_num, lec_eng_ratio, lec_category_detail,
							en_name, lec_prof
						)
						temp_lec = list(map(func_strip, temp_lec))	# tuple -> list(strip_string)
						hakbu_info_lst.append(temp_lec)
						if temp_lec[9] == '':
							temp_lec[9] = 0
						else:
							temp_lec[9] = int(temp_lec[9])
						temp_lec[2] = int(temp_lec[2])
						temp_lec[8] = int(temp_lec[8])
						# DB 값 Update
						db_lec = Lecture.objects.filter(Semester=cur_semester, Code=temp_lec[1], Class=temp_lec[2])

						if db_lec:
							db_lec.update(
								Semester=cur_semester,
								Category=temp_lec[0],
								Code=temp_lec[1],
								Class=temp_lec[2],
								CourseName=temp_lec[3],
								Credit=temp_lec[4],
								Major=temp_lec[5],
								Period=temp_lec[6],
								ClassRoom=temp_lec[7],
								Fix_num=temp_lec[8],
								Take_num=temp_lec[9],
								EnglishRatio=temp_lec[10],
								CategoryDetail=temp_lec[11],
								CourseName_Eng=temp_lec[12],
								Professor=temp_lec[13]
							)
						else:
							new_lec = Lecture(
								Semester=cur_semester,
								Category=temp_lec[0],
								Code=temp_lec[1],
								Class=temp_lec[2],
								CourseName=temp_lec[3],
								Credit=temp_lec[4],
								Major=temp_lec[5],
								Period=temp_lec[6],
								ClassRoom=temp_lec[7],
								Fix_num=temp_lec[8],
								Take_num=temp_lec[9],
								EnglishRatio=temp_lec[10],
								CategoryDetail=temp_lec[11],
								CourseName_Eng=temp_lec[12],
								Professor=temp_lec[13]
							)
							new_lec.save()
					except NoSuchElementException as e:		# page에 강의가 15개 이하인 경우
						break
			all_info_lst.append(hakbu_info_lst)
		return HttpResponse('성공적으로 데이터를 입력했습니다.')
	else:
		return HttpResponseRedirect('/')


def lec_update(request):
	semester_lst = [
	'11-1', '11-2', '11-Summer', '11-Winter', 
	'12-1', '12-2', '12-Summer', '12-Winter', 
	'13-1', '13-2', '13-Summer', '13-Winter', 
	'14-1', '14-2', '14-Summer', '14-Winter',
	'15-1', '15-2', '15-Summer'
	]
	# semester_lst = ['15-2']
	semester_lst.sort(reverse=True)
	
	file_location = "/opt/bitnami/apps/django/django_projects/darkzero/mysite2/gasul_table/"
	# 학부별 정리
	for semester in semester_lst:
		file_lst = [
			file_location+semester+'/0001.xlsx',
			file_location+semester+'/0009.xlsx',
			file_location+semester+'/0010.xlsx',
			file_location+semester+'/0011.xlsx',
			file_location+semester+'/0012.xlsx',
			file_location+semester+'/0021.xlsx',
			file_location+semester+'/0022.xlsx',
			file_location+semester+'/0024.xlsx',
			file_location+semester+'/0033.xlsx',
			file_location+semester+'/0071.xlsx',
			file_location+semester+'/0074.xlsx',
			file_location+semester+'/0077.xlsx',
			file_location+semester+'/0078.xlsx',
			file_location+semester+'/0090.xlsx'
		]
		for xls in file_lst:
			try:
				workbook = xlrd.open_workbook(xls)
			except:
				continue
			sheet = workbook.sheet_by_index(0)
			lec_lst = []
			for row in range(3, sheet.nrows, 4):
				lec_info = []
				for col in range(sheet.ncols):
					val = sheet.cell_value(row,col)
					# if val == '' :	# 값이 NULL이면 조작안함
					lec_info.append(val)
				lec_info.append(sheet.cell_value(row+1,3))	# 과목영어이름
				lec_info.append(sheet.cell_value(row+1,5))	# 교수님 성함
				lec_lst.append(lec_info)
			for var in lec_lst:
				if var[9] == '':
					var[9] = 0
				else:
					var[9] = int(var[9])
				if not (var[4] == ''):
					var[4] = int(var[4])
				if not (var[8] == ''):
					var[8] = int(var[8])
				var = list(map(func_strip, var))
				try:
					d_lec = Lecture.objects.filter(Semester=semester, Code=var[1], Class=var[2])
					if d_lec: # 업데이트 가능한 요소들
						d_lec.update(
							Class=var[2],
							Credit=var[4],
							Period=var[6],
							ClassRoom = var[7],
							Fix_num = var[8],
							Take_num = var[9],
							EnglishRatio = var[10],
							Professor = var[-1]
							)
					else:
						new_lec = Lecture(
							Semester=semester,
							Category=var[0],
							Code=var[1],
							Class=var[2],
							CourseName=var[3],
							Credit=var[4],
							Major=var[5],
							Period=var[6],
							ClassRoom=var[7],
							Fix_num=var[8],
							Take_num=var[9],
							EnglishRatio=var[10],
							CategoryDetail=var[11],
							CourseName_Eng=var[-2],
							Professor=var[-1],
							)
						new_lec.save()
				except:
					return HttpResponse('데이터 입력 중 오류가 발생했습니다.')
	return HttpResponse('성공적으로 데이터를 입력했습니다.')


