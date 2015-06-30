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
from functionhelper.views import *
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


	

def MyPage(request):	#MyPage 루트
	CheckingLogin(request.user.username)
	return render_to_response("sealmypage.html", {'user':request.user}) 

def About(request): #About template 루트
	CheckingLogin(request.user.username)
	return render_to_response("about.html",{'user':request.user})

def Schedule(request): #Schedule template 기능
	CheckingLogin(request.user.username)
	return render_to_response("schedule.html",{'user':request.user})

def Judgement(request): # 신고 게시판 기능
	CheckingLogin(request.user.username)
	return render_to_response("subscribe_report.html",{'user':request.user})


def Main(request, offset): #Main 기능
	CheckingLogin(request.user.username)	

	try:
		offset = int(offset)
	except ValueError:
		raise Http404() 

	PageInformation=request.session['PageInformation']
	#main 자바스크립트 조작 하기 위한 기능
	Active = ["","",""]
	URL_Path = request.path	#현재 페이지 URL 긁어오기


	##강의 DB에 저장된 자료들을 코드로 필터를 해서 Total Page를 만듦
	##그리고 나서 강의추천된 강의들만 따로 또 필터해서 데이터 넣는 과정임
	##후배여러분이 좀 알고리즘 잘짜서 더 최적화해주세요..(최대한 했지만..발적화임..))
	
	CourseCode = MajorSelect(request.user)
	
	#2차원 list로 각 전공당 총 페이지 수 저장
	T_Count=[[] ,[] ,[]]
	T_Count[0] = Lecture.objects.filter(Q(Code__contains=CourseCode[0]) | Q(Code__contains= CourseCode[1])).count()/5+1
	T_Count[1] = Lecture.objects.filter(Q(Code__contains= CourseCode[2]) | Q(Code__contains=CourseCode[3])).count()/5+1
	T_Count[2] = Lecture.objects.count()/5+1
	
	#main 페이지 활성화 기능(1전공, 2전공 all)
	Active = ["","",""]
	ActivieCount=0
	#URL을 통해 무슨 전공 페이지에 있는지 확인해서 그 정보 긁어옴
	PageData= ["FirstMajorPage","SecondMajorPage","AllPage"]
	for i in range(0,len(T_Count)):
		if URL_Path.find(PageData[i]) != -1:
			#페이지 갯수가 11개 이상일 경우
			PageInformation[i]=CurrentPageView(T_Count,offset,i)
			PageInformation[i][1] = offset
			Active[i] = "active" # main 페이지
			ActivieCount+=1
		else:
			pass
	if ActiveCount ==0:
		Activie=None
	#각 강의 전공에 해당하는 DB 정보 저장 함 
	TotalBoard = [[],[],[]]
	if CourseCode[0] !="ENG":
		TotalBoard[0] = Lecture.objects.filter(Q(Code__contains = CourseCode[0]) | Q(Code__contains=CourseCode[1])).order_by('Code')[(PageInformation[0][1]-1)*5:(PageInformation[0][1]-1)*5+5]
		TotalBoard[1] = Lecture.objects.filter(Q(Code__contains = CourseCode[2]) | Q(Code__contains=CourseCode[3])).order_by('Code')[(PageInformation[1][1]-1)*5:(PageInformation[1][1]-1)*5+5]
	else:
		TotalBoard[0] = Lecture.objects.filter(Q(Code__contains =CourseCode[0]) |Q(Code__contains=CourseCode[1])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('Code')[(PageInformation[0][1]-1)*5:(PageInformation[0][1]-1)*5+5]
		TotalBoard[1] = Lecture.objects.filter(Q(Code__contains =CourseCode[2]) |Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('Code')[(PageInformation[1][1]-1)*5:(PageInformation[1][1]-1)*5+5]
	TotalBoard[2] = Lecture.objects.order_by('Code')[(PageInformation[2][1]-1)*5:(PageInformation[2][1]-1)*5+5]

	PageBoard = PageView(TotalBoard)
	##Session Save
	request.session['PageInformation'] = PageInformation

	# 페이지 총 수(페이지 넘길 때)
	TotalCount=list()
	for i in range(0,len(T_Count)):
		TotalCount.append(PageTotalCount(i,T_Count,PageInformation[i]))
	return render_to_response("index.html",
		  {'user':request.user,
		   'PageBoard':PageBoard,
		   'TotalCount' : TotalCount,
		   'PageInformation' : PageInformation,
		   'Path':URL_Path,
		   'Active':Active,
		   })

def SubScript(request):
	CheckingLogin(request.user.username)
	return render_to_response("subscribe_improve.html", {'user':request.user})

def SiteMap(request):
	CheckingLogin(request.user.username)
	return render_to_response("sitemap.html", {'user':request.user})

def MyCourse(request):
		CheckingLogin(request.user.username)
		MyProfile = Profile.objects.get(User=request.user)
		RecommendPage=[]
		LikePage=[]
		UserBoard = Course_Evaluation.objects.filter(CreatedID = MyProfile)
		for BoardData in UserBoard:
			RecommendPage.append(Total_Evaluation.objects.get(CourseName = BoardData.Course))
		for Board2 in UserBoard:
			LikePage.append(Total_Evaluation.objects.get(CourseName = Board2.Course))


		return render_to_response("mycourses.html", {'user':request.user, 'RecommendPage':RecommendPage,})
@csrf_exempt
def Search(request): #전체 검색 기능
	CheckingLogin(request.user.username)

	if request.method =="POST":
		SearchData = request.POST['search']
		#여기 문제
		LectureData = [[]]
		LectureData[0]=Lecture.objects.filter(CourseName__contains=SearchData).order_by('Code')[0:5]
		SearchCount =list()
		SearchCount.append(Lecture.objects.filter(CourseName__contains=SearchData).count()/5+1)
		L_Data=PageView(LectureData)
		PageInformation =[1,1,1]

		PageInformation=FirstPageView(0,SearchCount)

		T_Count = PageTotalCount(0,SearchCount,PageInformation)

		request.session['SearchPageInformation'] = PageInformation
		request.session['SearchValue'] = SearchData
		return render_to_response('index.html', {
											'user':request.user,
											'Search' : L_Data,
											'PageInformation' : PageInformation,
											'T_Count':T_Count,
										})
	else:
		return HttpResponseRedirect("/mysite2")

def SearchPage(request, offset):
	CheckingLogin(request.user.username)

	try:
			offset = int(offset)
	except ValueError:
			raise Http404()
	SearchData = request.session['SearchValue']
	
	PageInformation = request.session['SearchPageInformation']
	PageInformation[1] = offset
	LectureData = [[]]
	LectureData[0]=Lecture.objects.filter(CourseName__contains=SearchData).order_by('Code')[(PageInformation[1]-1)*5:(PageInformation[1]-1)*5+5]
	SearchCount =list()
	SearchCount.append(Lecture.objects.filter(CourseName__contains=SearchData).count()/5+1)

	L_Data=PageView(LectureData)
	
	PageInformation = CurrentPageView(SearchCount,offset,0)
	T_Count=PageTotalCount(0,SearchCount,PageInformation)
	

	request.session['SearchPageInformation'] = PageInformation
	return render_to_response('index.html', {
										'user':request.user,
										'Search' : L_Data,
										'PageInformation' : PageInformation,
											'T_Count' : T_Count,
									})
#메인 페이지 view 함수로 옮김
def PageView(TotalBoard):
	PageBoard=[[],[],[]]
	count =0
	for DBBoard in TotalBoard:
		for Board in DBBoard:
			try:
				# 총 강의 추천된 DB 강의 명으로 호출
				BoardData = Total_Evaluation.objects.get(Course=Board)
			except :
				BoardData = None

			if BoardData is not None:
				BoardData.Total_Speedy = BoardData.Total_Speedy/BoardData.Total_Count
				BoardData.Total_Reliance = BoardData.Total_Reliance/BoardData.Total_Count
				BoardData.Total_Helper = BoardData.Total_Helper/BoardData.Total_Count
				BoardData.Total_Question = BoardData.Total_Question/BoardData.Total_Count
				BoardData.Total_Exam = BoardData.Total_Exam/BoardData.Total_Count
				BoardData.Total_Homework = BoardData.Total_Homework/BoardData.Total_Count
				PageBoard[count].append(BoardData)
			else:
				BoardData = Total_Evaluation(Course=Board)
				BoardData.Total_Speedy =5
				BoardData.Total_Reliance =5
				BoardData.Total_Helper = 5
				BoardData.Total_Question = 5
				BoardData.Total_Exam = 5
				BoardData.Total_Homework = 5
				BoardData.Total_Count =0
				PageBoard[count].append(BoardData)
		count=count+1
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
		elif FirstMajor==None :
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
		elif SecondMajor==None :
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
