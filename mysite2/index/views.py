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

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


	

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
				
				CourseCode = MajorSelect(request.user)
				
				
				T_Count1 = Lecture.objects.filter(Q(Code__contains=CourseCode[0]) | Q(Code__contains= CourseCode[1])).count()/5+1
				T_Count2 = Lecture.objects.filter(Q(Code__contains= CourseCode[2]) | Q(Code__contains=CourseCode[3])).count()/5+1
				T_Count3 = Lecture.objects.count()/5+1
				
				#main 페이지 활성화 기능(1전공, 2전공 all)
				Active = ["","",""]
				if URL_Path.find("FirstMajorPage") != -1:
					PageInformation1[1] = offset
					
					if T_Count1 >11:
						if offset>11:
							if (offset+10)>T_Count1:
								PageInformation1[0] = (offset -(offset%10))-9
								PageInformation1[2] = T_Count1
							else:
								PageInformation1[0] = (offset -(offset%10))-9
								PageInformation1[2] = (offset -(offset%10))+11
						else:
							PageInformation1[0] = 1
							PageInformation1[2] = (offset - (offset%10))+11
					else:
						PageInformation1[0] = 1
						PageInformation1[2] = T_Count1

					Active[0] = "active" #

				elif URL_Path.find("SecondMajorPage") != -1:
					PageInformation2[1] = offset

					if T_Count2 >11:
						if offset>11:
							PageInformation2[0] = (offset -(offset%10))-9
							PageInformation2[2] = (offset -(offset%10))+11
						elif (offset+10)>T_Count2:
							PageInformation2[0] = (offset -(offset%10))-9
							PageInformation2[2] = T_Count2           
						else:
							PageInformation2[0] = 1
							PageInformation2[2] = (offset - (offset%10))+11
					else:
						PageInformation2[0] = 1
						PageInformation2[2] = T_Count2
					Active[1] = "active"
	
				else:
					PageInformation3[1] = offset
					if T_Count3 >11:
						if offset>11:
							PageInformation3[0] = (offset -(offset%10))-9
							PageInformation3[2] = (offset -(offset%10))+11
						elif (offset+10)>T_Count3:
							PageInformation3[0] = (offset -(offset%10))-9
							PageInformation3[2] = T_Count3
						else:
							PageInformation3[0] = 1
							PageInformation3[2] = (offset - (offset%10))+11
					else:
						PageInformation3[0] = 1
						PageInformation3[2] = T_Count3
					Active[2] = "active"

				if CourseCode[0] !="ENG":
					TotalBoard1 = Lecture.objects.filter(Q(Code__contains = CourseCode[0]) | Q(Code__contains=CourseCode[1])).order_by('Code')[(PageInformation1[1]-1)*5:(PageInformation1[1]-1)*5+5]
					TotalBoard2 = Lecture.objects.filter(Q(Code__contains = CourseCode[2]) | Q(Code__contains=CourseCode[3])).order_by('Code')[(PageInformation2[1]-1)*5:(PageInformation2[1]-1)*5+5]
				else:
					TotalBoard1 = Lecture.objects.filter(Q(Code__contains =CourseCode[0]) |Q(Code__contains=CourseCode[1])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('Code')[(PageInformation1[1]-1)*5:(PageInformation1[1]-1)*5+5]
					TotalBoard2 = Lecture.objects.filter(Q(Code__contains =CourseCode[2]) |Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('Code')[(PageInformation2[1]-1)*5:(PageInformation2[1]-1)*5+5]
				TotalBoard3 = Lecture.objects.order_by('Code')[(PageInformation3[1]-1)*5:(PageInformation3[1]-1)*5+5]

				PageBoard = PageView(TotalBoard1,TotalBoard2,TotalBoard3)
				##Session Save
				request.session['PageInformation1'] = PageInformation1
				request.session['PageInformation2'] = PageInformation2
				request.session['PageInformation3'] = PageInformation3
				# 페이지 총 수(페이지 넘길 때)
				if (PageInformation1[1]/10) >= T_Count1/10:
						TotalCount1 = range(PageInformation1[1]-(PageInformation1[1]%10)+1,T_Count1+1)
				else:
						TotalCount1 = range(PageInformation1[1]-(PageInformation1[1]%10)+1,PageInformation1[1]-(PageInformation1[1]%10)+11)
				if (PageInformation2[1]+10) > T_Count2:
						TotalCount2 = range(PageInformation2[1]-(PageInformation2[1]%10)+1,T_Count2+1)
				else :
						TotalCount2 = range(PageInformation2[1]-(PageInformation2[1]%10)+1,PageInformation2[1]-(PageInformation2[1]%10)+11)
				if (PageInformation3[1]+10) > T_Count3:
						TotalCount3 = range(PageInformation3[1]-(PageInformation3[1]%10)+1,T_Count3+1)
				else:
						TotalCount3 = range(PageInformation3[1]-(PageInformation3[1]%10)+1,PageInformation3[1]-(PageInformation3[1]%10)+11)
				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard':PageBoard,

					   'TotalCount1' : TotalCount1,
					   'TotalCount2' : TotalCount2,
					   'TotalCount3' : TotalCount3,
					   'PageInformation1' : PageInformation1,
					   'PageInformation2' : PageInformation2,
					   'PageInformation3' : PageInformation3,
					   'Path':URL_Path,
					   'Active':Active,
					   'Tcount1':T_Count1,
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
			LikePage=[]
			UserBoard = Course_Evaluation.objects.filter(CreatedID = MyProfile)
			for Board1 in UserBoard:
				RecommendPage.append(Total_Evaluation.objects.get(CourseName = Board1.Course))
			for Board2 in UserBoard:
				LikePage.append(Total_Evaluation.objects.get(CourseName = Board2.Course))


			return render_to_response("mycourses.html", {'user':request.user, 'RecommendPage':RecommendPage,})

# def Search(request): #전체 검색 기능
# 	if request.user.username =="":
# 		return HttpResponseRedirect("/mysite2")
# 	else:
# 		if request.method =="POST"
# 			SearchData = request.POST['search']



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
                                                                      
def MajorSelect(user):
		try:
			Student = Profile.objects.get(User =user)
		except:
			return None
		MajorCode= [[],[],[],[],[],[]]	
		FirstMajor = str(Student.FirstMajor)
		SecondMajor = str(Student.SecondMajor)
			#1전공 선택 하는 조건문
		if FirstMajor.find("국제") != -1 or FirstMajor.find("영어") != -1:
			MajorCode[0]="ISE"
			MajorCode[1]="None"
		elif FirstMajor.find("경영학") != -1 or FirstMajor.find("경제학")!= -1:
			MajorCode[0]="GMP"
			MajorCode[1]="MEC"
		elif FirstMajor.find("한국법") != -1 or FirstMajor.find("UIL")!= -1:
			MajorCode[0]="LAW"
			MajorCode[1]="UIL"
		elif FirstMajor.find("공연영상")!= -1 or FirstMajor.find("언로정보학")!= -1:
			MajorCode[0]="CCC"
			MajorCode[1]="None"
		elif FirstMajor.find("건설공학") != -1 or FirstMajor.find("도시환경")!= -1:
			MajorCode[0]="CUE"
			MajorCode[1]="None"
		elif FirstMajor.find("기계공학")!= -1 or FirstMajor.find("전자제어")!= -1 or FirstMajor.find("기전공학")!=-1:
			MajorCode[0]="HMM"
			MajorCode[1]="None"
		elif FirstMajor.find("시각디자인")!= -1 or FirstMajor.find("제품디자인")!= -1:
			MajorCode[0]="IID"
			MajorCode[1]="None"
		elif FirstMajor.find("생명과학")!= -1:
			MajorCode[0]="BFT"
			MajorCode[1]="None"
		elif FirstMajor.find("컴퓨터") != -1 or FirstMajor.find("전자") != -1:
			MajorCode[0]="ECE"
			MajorCode[1]="ITP"
		elif FirstMajor.find("상담심리") != -1 or FirstMajor.find("사회복지")!= -1:
			MajorCode[0]="CSW"
			MajorCode[1]="None"
		elif FirstMajor.find("에디슨")!= -1 :
			MajorCode[0]="GEA"
			MajorCode[1]="None"
		elif FirstMajor.find("영어학과")!= -1 or FirstMajor.find("경영학과")!= -1 or FirstMajor.find("사회복지학과")!= -1:
			MajorCode[0]="SIE"
			MajorCode[1]="None"
		elif FirstMajor.find("None") != -1:
			MajorCode[2]="None"
			MajorCode[3]="None"
			MajorCode[4]="None"
			MajorCode[5]="None"
		else:
			MajorCode[0]="ENG"
			MajorCode[1]="GEK"
			MajorCode[2]="GCS"
			MajorCode[3]="PCO"
			MajorCode[4]="ISL"
			MajorCode[5]="PST"

		if SecondMajor.find("국제")!=-1 or SecondMajor.find("영어")!=-1:
			MajorCode[2]="ISE"
			MajorCode[3]="None"
		elif SecondMajor.find("경영학")!=-1 or SecondMajor.find("경제학")!=-1:
			MajorCode[2]="GMP"
			MajorCode[3]="MEC"
		elif SecondMajor.find("한국법")!=-1 or SecondMajor.find("UIL")!=-1:
			MajorCode[2]="LAW"
			MajorCode[3]="UIL"
		elif SecondMajor.find("공연영상") !=-1 or SecondMajor.find("언로정보학")!=-1:
			MajorCode[2]="CCC"
			MajorCode[3]="None"
		elif SecondMajor.find("건설공학") !=-1 or SecondMajor.find("도시환경")!=-1:
			MajorCode[2]="CUE"
			MajorCode[3]="None"
		elif SecondMajor.find("기계공학")!=-1 or SecondMajor.find("전자제어")!=-1 or SecondMajor.find("기전공학")!=-1:
			MajorCode[2]="HMM"
			MajorCode[3]="None"
		elif SecondMajor.find("시각디자인")!=-1 or SecondMajor.find("제품디자인")!=-1:
			MajorCode[2]="IID"
			MajorCode[3]="None"
		elif SecondMajor.find("생명과학")!=-1:
			MajorCode[2]="BFT"
			MajorCode[3]="None"
		elif SecondMajor.find("컴퓨터")!=-1 or SecondMajor.find("전자")!=-1:
			MajorCode[2]="ECE"
			MajorCode[3]="ITP"
		elif SecondMajor.find("상담심리")!=-1 or SecondMajor.find("사회복지")!=-1:
			MajorCode[2]="CSW"
			MajorCode[3]="None"
		elif SecondMajor.find("에디슨")!=-1:
			MajorCode[2]="GEA"
			MajorCode[3]="None"
		elif SecondMajor.find("영어학과") !=-1 or SecondMajor.find("경영학과") !=-1 or SecondMajor.find("사회복지학과")!=-1:
			MajorCode[2]="SIE"
			MajorCode[3]="None"
		elif SecondMajor.find("None") != -1:
			MajorCode[2]="None"
			MajorCode[3]="None"
			MajorCode[4]="None"
			MajorCode[5]="None"
		else:
			MajorCode[2]="GCS"
			MajorCode[3]="PCO"
			MajorCode[4]="ISL"
			MajorCode[5]="PST"
		


		return MajorCode

# Create your views here
