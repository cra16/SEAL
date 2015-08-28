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

from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q
from functionhelper.views import *
 
def Course(request, offset): #강의 추천 된 것을 종합하는 것을 보여주는 기능
		if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")

		#현재 접속한 아이디 정보 받아옴
		try:
			UserData = Profile.objects.get(User = request.user)
		except :
			UserData =None
		
		#강의 추천 3번이상 안했을 시 정보 안 보여줌
		if UserData.RecommendCount <=2:
			if request.flavour =='full':
					return render_to_response("html/Course_error.html")
			else:
				return render_to_response("m_skins/m_html/Course_error.html")
		else:
				try:
					offset = int(offset)
				except:
					raise Http404()
				#보려는 강의 정보 
				LectureInformation=Lecture.objects.get(id=offset)

				CourseBoard=TotalCourse(offset)#해당 강의 전체 추천한 Data DB 불러오기
				
				
				#자신이 햇을 경우 자신이 평가한 정보를 보여주는 기능
				try:
					MyCourseBoard = Course_Evaluation.objects.get(Course = LectureInformation, CreatedID = UserData)
				except:
					MyCourseBoard = None
				
				#한 페이지에 뿌리는 기능
				PageFirst = 3*(1-1)
				PageLast = 3*(1-1)+3
				OtherCourse = Course_Evaluation.objects.filter(Course = LectureInformation).order_by('-id')[PageFirst:PageLast]
				
				OtherCourseBoard = []
				#접속한 아이디와 중복되는 경우 제거
				for Board in OtherCourse:
					if Board.CreatedID == UserData:
							pass
					else:
						OtherCourseBoard.append(Board)

				
				#pageNation과 관련된 기능
				DBCount =Course_Evaluation.objects.filter(Course=LectureInformation).count()
				O_Count = DataCount(3,DBCount)
				
				#전체 페이지가 11페이지 이상인 것을 기준으로 정의
				PageInformation=FirstPageView(O_Count)
				#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
				OtherCount=PageTotalCount(O_Count,PageInformation)
				dic ={'user':request.user,
					'BestBoard':BestBoardView(),
					'CourseBoard':CourseBoard,
					'MyCourseBoard':MyCourseBoard,
					'OtherCourseBoard':OtherCourseBoard,
					'OtherCount':OtherCount,
					'PageInformation':PageInformation
					}
				if request.flavour =='full':
					return render_to_response('html/course.html',dic)
				else:
					return render_to_response("m_skins/m_html/course.html",dic)
#페이지 넘겼을 때 작동되는 함수9
@csrf_exempt
def CoursePage(request, offset):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	try:
		offset = int(offset)
		if request.method=="POST":
			offset2 =int(request.POST["Page"]) 
		UserData=Profile.objects.get(User=request.user)
	except:
		raise Http404()
		
	#현 페이지에 대한 강의 정보
	LectureInformation = Lecture.objects.get(id = offset)


	CourseBoard = TotalCourse(offset)
	try:
			DBCount = Course_Evaluation.objects.filter(Course = LectureInformation).count()
			O_Count = DataCount(3,DBCount)
	except:
			DBCount = 0

	if UserData !=None:
		try:
				MyCourseBoard = Course_Evaluation.objects.get(Course = LectureInformation, CreatedID = UserData)
		except:
				MyCourseBoard=None
		            #자신 이외 다른사람이 추천한 정보 보여줌
	else:
		MyCourseBoard = None
	#이전페이지 다음페이지 기능 구현

	PageInformation=CurrentPageView(O_Count,offset2)
	
	OtherCount=PageTotalCount(O_Count,PageInformation)

	PageInformation[1]=offset2
	#해당 페이지에 출력할 데이터들 갯수 정하는 기능
	PageFirst = (offset2-1)*3
	PageLast = (offset2-1)*3+3
	try:
			OtherCourse = Course_Evaluation.objects.filter(Course = LectureInformation).order_by('-id')[PageFirst:PageLast]
	except:
		OtherCourse=None
	OtherCourseBoard = []
	#접속한 아이디와 중복되는 경우 제거
	for Board in OtherCourse:
		if Board.CreatedID == UserData:
				pass
		else:
			OtherCourseBoard.append(Board)

	dic ={'user':request.user,
			'BestBoard':BestBoardView(),
			'CourseBoard':CourseBoard,
			'MyCourseBoard':MyCourseBoard,
			'OtherCourseBoard':OtherCourseBoard,
			'PageInformation':PageInformation,
			'OtherCount':OtherCount
			}
	if request.flavour =='full':
		return render_to_response('html/coursepage.html',dic)
	else:
		return render_to_response("m_skins/m_html/coursepage.html",dic )

# Create your views here.

#해당 강의 총 평가 데이터 모음을 구현 하기 위한 함수
def TotalCourse(offset):
	try:
		CourseBoard = Total_Evaluation.objects.get(Course = Lecture.objects.get(id = offset))
		CourseBoard.Total_Speedy = CourseBoard.Total_Speedy/CourseBoard.Total_Count
		CourseBoard.Total_Reliance = CourseBoard.Total_Reliance/CourseBoard.Total_Count
		CourseBoard.Total_Helper = CourseBoard.Total_Helper/CourseBoard.Total_Count
		CourseBoard.Total_Question = CourseBoard.Total_Question/CourseBoard.Total_Count
		CourseBoard.Total_Exam = CourseBoard.Total_Exam/CourseBoard.Total_Count
		CourseBoard.Total_Homework = CourseBoard.Total_Homework/CourseBoard.Total_Count
	except:
		CourseBoard = Total_Evaluation(Course =Lecture.objects.get(id=offset))
		CourseBoard.Total_Speedy=5
		CourseBoard.Total_Reliance =5
		CourseBoard.Total_Question=5
		CourseBoard.Total_Helper=5
		CourseBoard.Total_Exam =5
		CourseBoard.Total_Homework = 5

	return CourseBoard