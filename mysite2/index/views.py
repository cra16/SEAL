# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from login.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q

def MyPage(request):	#MyPage 루트


	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("sealmypage.html", {'user':request.user}) 


def About(request): #About template 루트


	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("about.html",{'user':request.user})


def Schedule(request): #Schedule template 기능

	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("schedule.html",{'user':request.user})

def Judgement(request): # 신고 게시판 기능

	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_report.html",{'user':request.user})



		




def Main(request, offset): #Main 기능

	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:

				try:
					offset = int(offset)
				except ValueError:
					raise Http404()


	
		
				PageInformation1 = request.session['PageInformation1'] #First Major Page DB
				PageInformation2 = request.session['PageInformation2'] #Second Major Page DB
				PageInformation3 = request.session['PageInformation3'] #all Page DB

				#main 자바스크립트 조작 하기 위한 기능
				Active = ["","",""]

				URL_Path = request.path	#현재 페이지 URL 긁어오기
			
			
				##강의 DB에 저장된 자료들을 코드로 필터를 해서 Total Page를 만듦
				##그리고 나서 강의추천된 강의들만 따로 또 필터해서 데이터 넣는 과정임
				##다른 개발자분이 좀 알고리즘 잘짜서 더 최적화해주세요..(발적화임..))
				
				
				
				T_Count1 = Lecture.objects.filter(Q(Code__contains="ECE") | Q(Code__contains="ITP")).count()
				T_Count2 = Lecture.objects.filter(Code__contains ="SIE").count()
				T_Count3=Lecture.objects.count()
				
				
				


				#main 페이지 활성화 기능(1전공, 2전공 all)
				Active = ["","",""]


				if URL_Path.find("FirstMajorPage") != -1 :
					PageInformation1[1] = offset
					if T_Count1 >11:
						if offset>11:
							PageInformation1[0] = (offset -(offset%10))-9
							PageInformation1[2] = (offset -(offset%10))+11
						else:
							PageInformation1[0] = 1
							PageInformation1[2] = (offset - (offset%10))+11
					else:
						PageInformation[0] = 1
						PageInformation[2] = T_Count1

					Active[0] = "active" #

				elif URL_Path.find("SecondMajorPage") != -1:
					PageInformation2[1] = offset

					if T_Count1 >11:
						if offset>11:
							PageInformation2[0] = (offset -(offset%10))-9
							PageInformation2[2] = (offset -(offset%10))+11
						else:
							PageInformation2[0] = 1
							PageInformation2[2] = (offset - (offset%10))+11
					else:
						PageInformation2[0] = 1
						PageInformation2[2] = T_Count1
					Active[1] = "active"
	
				else:
					PageInformation3[1] = offset
					if T_Count1 >11:
						if offset>11:
							PageInformation3[0] = (offset -(offset%10))-9
							PageInformation3[2] = (offset -(offset%10))+11
						else:
							PageInformation3[0] = 1
							PageInformation3[2] = (offset - (offset%10))+11
					else:
						PageInformation3[0] = 1
						PageInformation3[2] = T_Count1
					Active[2] = "active"

				#TotalBoard1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP"))[(PageInformation1[1]-1)*5:(PageInformation1[1]-1)*5+5]
				TotalBoard1 = MajorSelect(request.user)
				TotalBoard2 = Lecture.objects.filter(Code__contains = "SIE")[(PageInformation2[1]-1)*5:(PageInformation2[1]-1)*5+5]
				TotalBoard3 = Lecture.objects.order_by('-id')[(PageInformation3[1]-1)*5:(PageInformation3[1]-1)*5+5]

				PageBoard = PageView(TotalBoard1,TotalBoard2,TotalBoard3)
				##Session Save
				request.session['PageInformation1'] = PageInformation1
				request.session['PageInformation2'] = PageInformation2
				request.session['PageInformation3'] = PageInformation3
				
				
				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard':PageBoard,
					   'TotalCount1' : range(PageInformation1[1]-(PageInformation1[1]%10)+1,PageInformation1[1]-(PageInformation1[1]%10)+11),
					   'TotalCount2' : range(PageInformation2[1]-(PageInformation2[1]%10)+1,PageInformation2[1]-(PageInformation2[1]%10)+11),
					   'TotalCount3' : range(PageInformation3[1]-(PageInformation3[1]%10)+1,PageInformation3[1]-(PageInformation3[1]%10)+11),
					   'PageInformation1' : PageInformation1,
					   'PageInformation2' : PageInformation2,
					   'PageInformation3' : PageInformation3,
					   'Path':URL_Path,
					   'Active':Active,
					   })

def SubScript(request):
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_improve.html", {'user':request.user})

def SiteMap(request):
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("sitemap.html", {'user':request.user})

def MyCourse(request):
        if request.user.username =="":
                return HttpResponseRedirect("/mysite2")
        else:
			MyProfile = Profile.objects.get(User=request.user)
			RecommendPage=[]
			UserBoard = Course_Evaluation.objects.filter(CreatedID = MyProfile)
			for Board1 in UserBoard:
				RecommendPage.append(Total_Evaluation.objects.get(CourseName = Board1.Course))


			return render_to_response("mycourses.html", {'user':request.user, 'RecommendPage':RecommendPage,})



#메인 페이지 view 함수로 옮김
def PageView(TotalBoard1,TotalBoard2,TotalBoard3):
	PageBoard = [[],[],[]]
	for Board in TotalBoard1:
		try:
			# 총 강의 추천된 DB 강의 명으로 호출
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
                                                                      
def MajorSelect(User):
		CourseCode= [[],[],[],[],[],[]]	
			#1전공 선택 하는 조건문
		if user.profile.FirstMajor.find("국제") || user.profile.FirstMajor.find("영어"):
			CourseCode[0]="ISE"
			CourseCode[1]="None"
		elif user.profile.FirstMajor.find("경영학전공") || user.profile.FirstMajor.find("경제학전공"):
			CourseCode[0]="GMP"
			CourseCode[1]="MEC"
		elif user.profile.FirstMajor.find("한국법") || user.profile.FirstMajor.find("UIL"):
			CourseCode[0]="LAW"
			CourseCode[1]="UIL"
		elif user.profile.FirstMajor.find("공연영상") || user.profile.FirstMajor.find("언로정보학"):
			CourseCode[0]="CCC"
			CourseCode[1]="None"
		elif user.profile.FirstMajor.find("건설공학") || user.profile.FirstMajor.find("도시환경"):
			CourseCode[0]="CUE"
			CourseCode[1]="None"
		elif user.profile.FirstMajor.find("기계공학") || user.profile.FirstMajor.find("전자제어") || user.profile.FirstMajor.find("기전공학"):
			CourseCode[0]="HMM"
			CourseCode[1]="None"
		elif user.profile.FirstMajor.find("시각디자인") || user.profile.FirstMajor.find("제품디자인"):
			CourseCode[0]="IID"
			CourseCode[1]="None"
		elif user.profile.FirstMajor.find("생명과학"):
			CourseCode[0]="BFT"
			CourseCode[1]="None"
		elif user.profile.FirstMajor.find("컴퓨터") || user.profile.FirstMajor.find("전자"):
			CourseCode[0]="ECE"
			CourseCode[1]="ITP"
		elif user.profile.FirstMajor.find("상담심리") || user.profile.FirstMajor.find("사회복지"):
			Coursecode[0]="CSW"
			CourseCode[1]="None"
		elif user.profile.FirstMajor.find("에디슨"):
			CourseCode[0]="GEA"
			CourseCode[1]="None"
		elif user.profile.FirstMajor.find("영어학과") || user.profile.FirstMajor.find("경영학과") ||user.profile.FirstMajor.find("사회복지학과"):
			CourseCode[0]="SIE"
			CourseCode[1]="None"
		else:
			CourseCode[0]="ENG"
			CourseCode[1]="GEK"
			CourseCode[2]="GCS"
			CourseCode[3]="PCO"
			CourseCode[4]="ISL"
			CourseCode[5]="PST"

		if user.profile.SecondMajor.find("국제") || user.profile.SecondMajor.find("영어"):
			CourseCode[2]="ISE"
			CourseCode[3]="None"
		elif user.profile.SecondMajor.find("경영학전공") || user.profile.SecondMajor.find("경제학전공"):
			CourseCode[2]="GMP"
			CourseCode[3]="MEC"
		elif user.profile.SecondMajor.find("한국법") || user.profile.SecondMajor.find("UIL"):
			CourseCode[2]="LAW"
			CourseCode[3]="UIL"
		elif user.profile.SecondMajor.find("공연영상") || user.profile.SecondMajor.find("언로정보학"):
			CourseCode[2]="CCC"
			CourseCode[3]="None"
		elif user.profile.SecondMajor.find("건설공학") || user.profile.SecondMajor.find("도시환경"):
			CourseCode[2]="CUE"
			CourseCode[3]="None"
		elif user.profile.SecondMajor.find("기계공학") || user.profile.SecondMajor.find("전자제어") || user.profile.SecondMajor.find("기전공학"):
			CourseCode[2]="HMM"
			CourseCode[3]="None"
		elif user.profile.SecondMajor.find("시각디자인") || user.profile.SecondMajor.find("제품디자인"):
			CourseCode[2]="IID"
			CourseCode[3]="None"
		elif user.profile.SecondMajor.find("생명과학"):
			CourseCode[2]="BFT"
			CourseCode[3]="None"
		elif user.profile.SecondMajor.find("컴퓨터") || user.profile.SecondMajor.find("전자"):
			CourseCode[2]="ECE"
			CourseCode[3]="ITP"
		elif user.profile.SecondMajor.find("상담심리") || user.profile.SecondMajor.find("사회복지"):
			Coursecode[2]="CSW"
			CourseCode[3]="None"
		elif user.profile.SecondMajor.find("에디슨"):
			CourseCode[2]="GEA"
			CourseCode[3]="None"
		elif user.profile.SecondMajor.find("영어학과") || user.profile.SecondMajor.find("경영학과") ||user.profile.SecondMajor.find("사회복지학과"):
			CourseCode[2]="SIE"
			CourseCode[3]="None"
		else:
			CourseCode[0]="ENG"
			CourseCode[1]="GEK"
			CourseCode[2]="GCS"
			CourseCode[3]="PCO"
			CourseCode[4]="ISL"
			CourseCode[5]="PST"

# Create your views here
