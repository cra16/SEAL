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
	#아직 3번 입력해야 들어갈 수 있는 기능 안만듬.(뭐 이건 금방하니까..)
		try:
			UserData = Profile.objects.get(User = request.user)
		except :
			UserData =None
		CheckingLogin(request.user.username)
		if UserData.RecommendCount <=2:
			return render_to_response("Course_error.html")
		else:
				try:
					offset = int(offset)
				except:
					raise Http404()

				PageInformation=[1,1,1]
				CourseBoard=TotalCourse(offset)#해당 강의 전체 추천한 Data DB 불러오기
				
				DBCount =Course_Evaluation.objects.filter(Course=Lecture.objects.get(id=offset)).count()
				O_Count = DataCount(3,DBCount)
				
				try:
					MyCourseBoard = Course_Evaluation.objects.get(Course = Lecture.objects.get(id=offset), CreatedID = UserData)
				            #자신 이외 다른사람이 추천한 정보 보여줌
				except:
					MyCourseBoard = None
				OtherCourse = Course_Evaluation.objects.filter(Course = Lecture.objects.get(id = offset)).order_by('-id')[0:3]
				OtherCourseBoard = []
				#접속한 아이디와 중복되는 경우 제거
				for Board in OtherCourse:
					if Board.CreatedID == UserData:
							pass
					else:
						OtherCourseBoard.append(Board)

				#전체 페이지가 11페이지 이상인 것을 기준으로 정의
				PageInformation=FirstPageView(O_Count)
				#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
				OtherCount=PageTotalCount(O_Count,PageInformation)
				return render_to_response("course.html",
                                  {'user':request.user,
                                  'BestBoard':BestBoardView(),
                                   'CourseBoard':CourseBoard,
                                   'MyCourseBoard':MyCourseBoard,
                                   'OtherCourseBoard':OtherCourseBoard,
                                   'OtherCount':OtherCount,
                                   'PageInformation':PageInformation,
  
                                   })
#페이지 넘겼을 때 작동되는 함수
def CoursePage(request, offset, offset2):
	CheckingLogin(request.user)
	try:
		offset = int(offset)
		offset2 = int(offset2)
		UserData=Profile.objects.get(User=request.user)
	except:
		raise Http404()

	PageInformation=[1,1,1]
	CourseBoard = TotalCourse(offset)

	DBCount = Course_Evaluation.objects.filter(Course = Lecture.objects.get(id = offset)).count()
	O_Count = DataCount(3,DBCount)


	if UserData !=None:
		MyCourseBoard = Course_Evaluation.objects.get(Course = Lecture.objects.get(id=offset), CreatedID = UserData)
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
	OtherCourse = Course_Evaluation.objects.filter(Course = Lecture.objects.get(id = offset)).order_by('-id')[PageFirst:PageLast]
	
	OtherCourseBoard = []
	#접속한 아이디와 중복되는 경우 제거
	for Board in OtherCourse:
		if Board.CreatedID == UserData:
				pass
		else:
			OtherCourseBoard.append(Board)

	return render_to_response("course.html",
                                      {'user':request.user,
                                      'BestBoard':BestBoardView(),
                                       'CourseBoard':CourseBoard,
                                       'MyCourseBoard':MyCourseBoard,
                                       'OtherCourseBoard':OtherCourseBoard,
                                       'PageInformation':PageInformation,
                                       'OtherCount':OtherCount
                                       })

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