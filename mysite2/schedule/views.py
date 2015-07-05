# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from lecture.models import *
from functionhelper.views import *
from django.views.decorators.csrf import csrf_exempt


# 시간표 선택시 검색 기능
def SelectPeriod(request, period, page):
	"""
	period -> 테이블에서 선택한 강의시간
	page -> pagination에서 선택한 page
	"""
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:
		cur_page = int(page)
		# cur_page = request.session['cur_page']

		start = 6 * (cur_page-1)
		end = 6 * cur_page
		cur_semester = '14-2'	# 데이터가 많으므로 현재 학기만 가져오도록 한다.
		if period[1] == '1':	# 1교시의 경우 10교시가 같이 나오는 것을 방지하기 위한 장치
			lec_cnt = Lecture.objects.filter(Semester=cur_semester, Period__contains=period).exclude(Period__contains='10').count()
			lec_lst = Lecture.objects.filter(Semester=cur_semester, Period__contains=period).exclude(Period__contains='10')[start:end]
		else:
			lec_cnt = Lecture.objects.filter(Semester=cur_semester, Period__contains=period).count()
			lec_lst = Lecture.objects.filter(Semester=cur_semester, Period__contains=period)[start:end]
		total_page = ( (lec_cnt - 1) / 6 ) + 1
		is_odd = lec_cnt % 2
		ctx = {
			'user':request.user,
			'period':period,
			'total_page': range(1, total_page+1),
			'lec_lst':lec_lst,
			'is_odd':is_odd,
			'cur_page':cur_page
		}
		# request.session['cur_page'] = cur_page + 1

		return render_to_response('schedule.html', ctx)

@csrf_exempt
def SearchSubject(request):
	CheckingLogin(request.user.username)

 	if request.method =="POST":
 		
		category = request.POST['category']
		major = request.POST['major']
		SearchName = request.POST['SearchName']
		Page = request.POST['Page']
		if Page !="0":
			cur_page = int(Page) 		
			New=0
		else:
			cur_page = 1
			New =1
		#cur_page = int(offset)

		start = 6 *(cur_page-1)
		end = 6 * (cur_page)


		SelectMajor=Major(major)
		SelectCategory=Category(category)

		Subject=[0]
		if SearchName == "":
			if SelectMajor != "전체" and SelectCategory !="전체":
					DBCount = Lecture.objects.filter(Major__contains=SelectMajor, CategoryDetail__contains=SelectCategory).count()
					SubjectCount=DataCount(6,DBCount)
					Subject[0] = Lecture.objects.filter(Major__contains=SelectMajor, CategoryDetail__contains=SelectCategory)[start:end]
			elif SelectMajor != "전체" and SelectCategory =="전체":
					DBCount = Lecture.objects.filter(Major__contains=SelectMajor).count()
					SubjectCount=DataCount(6,DBCount)
					Subject[0] = Lecture.objects.filter(Major__contains=SelectMajor)[start:end]
			elif SelectMajor =="전체" and SelectCategory !="전체":
					DBCount = Lecture.objects.filter(CategoryDetail__contains=SelectCategory).count()
					SubjectCount=Condition = (DBCount%6!=0)  and 1 or 0
					Subject[0] = Lecture.objects.filter(CategoryDetail__contains=SelectCategory)[start:end]
			else:
					DBCount= Lecture.objects.count()
					SubjectCount=DataCount(6,DBCount)
					Subject[0] = Lecture.objects.order_by('Code')[start:end]
			

		else:
			SubjectCount = Lecture.objects.filter(CourseName__contains=SearchName).count()
			Subject[0] = Lecture.objects.filter(CourseName__contains=SearchName)[start:end]

		if New == 1:
			PageInformation = FirstPageView(SubjectCount)
			TotalCount=PageTotalCount(SubjectCount,PageInformation)
		else :
			PageInformation = CurrentPageView(SubjectCount,cur_page)
			PageInformation[1]=cur_page
			TotalCount = PageTotalCount(SubjectCount,PageInformation)
		TotalBoard = PageView(Subject)
		Dic = {
				'user':request.user,
				'Subject':Subject,
				'SelectMajor' : SelectMajor,
				'SubjectCount':SubjectCount,
				'SearchName':SearchName,
				'PageInformation':PageInformation,
				'TotalCount':TotalCount,
				'cur_page':cur_page,
				'Page' :Page,
				'TotalBoard':TotalBoard
		}

		return render_to_response('scheduleTemplate.html', Dic)
	else:
		return render_to_response("schedule.html",{'user':request.user,'Data' :0})

def Major(major):
	if major == "0001":
		major = "글로벌"
	elif major == "0009":
		major = "창의융합교육원"
	elif major == "0010":
		major = "Global EDISON"
	elif major == "0011":
		major = "국제어문"
	elif major == "0012":
		major = "언론정보"
	elif major == "0021":
		major = "경영경제"
	elif major == "0022":
		major = "법학부"
	elif major =="0024":
		major = "상담복지"
	elif major =="0033":
		major = "생명과학"
	elif major == "0071":
		major = "전산전자"
	elif major == "0074":
		major = "산업디자인"
	elif major == "0077":
		major = "기계제어"
	elif major == "0078":
		major = "공간환경"
	else:
		major = "전체"

	return major
def Category(category):
	if category == "W04":
		category = "신앙1"
	elif category == "W05":
		category = "인성1"
	elif category == "W06":
		category = "인성2"
	elif category == "W07":
		category = "신앙2"
	elif category == "W08":
		category = "세계관1"
	elif category == "W09":
		category = "세계꽌2"
	elif category == "W10":
		category = "인문"
	elif category == "W11":
		category = "역사"
	elif category == "W12":
		category = "사회"
	elif category == "W13":
		category = "수학"
	elif category == "W14":
		category = "자연"
	elif category == "W15":
		category = "신앙3"
	elif category == "W16":
		category = "리더십"
	elif category == "W17":
		category = "예술"
	elif category == "W18":
		category = "전공기초"
	elif category == "W19":
		category = "외국어"
	elif category == "W22":
		category = "전공탐색"
	elif category == "W24":
		category = "제2외국어"
	elif category == "W25":
		category = "소통및융복합"
	elif category == "W26":
		category = "ICT융합기초"
	elif category == "W27":
		category = "인문학"
	elif category == "W28":
		category = "사회과학"
	elif category == "W29":
		category = "자연과학"
	elif category == "W30":
		category = "리더십문제해결"
	elif category == "W31":
		category = "스포츠"
	elif category == "W32":
		category = "영어1"
	elif category == "W33":
		category = "영어2"
	elif category == "W34":
		category = "기독교신앙기초1"
	elif category == "W35":
		category = "기독교신앙기초2"
	elif category == "W50":
		category = "실무영어"
	elif category == "W51":
		category = "실무한문"
	elif category == "W52":
		category = "실무전산"
	elif category == "W53":
		category = "실무한국어"
	elif category == "X01":
		category = "야간-영어"
	elif category == "X02":
		category = "야간-경영학"
	elif category == "X03":
		category = "야간-실무"
	elif category == "X04":
		category = "야간-교양"
	elif category == "X06":
		category = "야간-실무전산"
	elif category == "X07":
		category = "야간-실무영어"
	elif category == "X08":
		category = "야간-실무한문"
	else:
		category = "전체"

	return category
		