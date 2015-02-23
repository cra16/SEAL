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


def Course(request, offset): #강의 추천 된 것을 종합하는 것을 보여주는 기능
	#아직 3번 입력해야 들어갈 수 있는 기능 안만듬.(뭐 이건 금방하니까..)
		try:
			UserData = Profile.objects.get(User = request.user)
		except :
			UserData =None
		if request.user.username =="":
				return  HttpResponseRedirect("/mysite2")
		elif UserData.RecommendCount <=2:
			return render_to_response("Course_error.html")
		else:
				try:
					offset = int(offset)
				except:
					raise Http404()

				PageInformation=[1,1,1]
				CourseBoard=TotalCourse(offset)#해당 강의 전체 추천한 Data DB 불러오기
				O_Count = Course_Evaluation.objects.filter(Course=Lecture.objects.get(id=offset)).count()/3+1
				UserProfile=Profile.objects.get(User=request.user)
				try:
					MyCourseBoard = Course_Evaluation.objects.get(CreatedID = UserProfile)
                                #자신 이외 다른사람이 추천한 정보 보여줌
				except:
					MyCourseBoard = None
				if MyCourseBoard is None:
					MyCourseBoard = Course_Evaluation(Course = Lecture.objects.get(id=offset), CreatedID = UserProfile)
				OtherCourse = Course_Evaluation.objects.filter(Course = Lecture.objects.get(id = offset)).order_by('-id')[0:3]
				OtherCourseBoard = []
				#접속한 아이디와 중복되는 경우 제거
				for Board in OtherCourse:
					if Board.CreatedID == UserProfile:
							pass
					else:
						OtherCourseBoard.append(Board)

				#전체 페이지가 11페이지 이상인 것을 기준으로 정의
				if O_Count<11:
					PageInformation[0] = 1
					PageInformation[2] = O_Count
				else:
					PageInformation[0] =1
					PageInformation[2] =11

				#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
				if (PageInformation[1]/10) >= O_Count/10:
						OtherCount = range(PageInformation[1]-(PageInformation[1]%10)+1,O_Count+1)
				else:
						OtherCount = range(PageInformation[1]-(PageInformation[1]%10)+1,PageInformation[1]-(PageInformation[1]%10)+11)
				
				return render_to_response("course.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                           'MyCourseBoard':MyCourseBoard,
                                           'OtherCourseBoard':OtherCourseBoard,
                                           'OtherCount':OtherCount,
                                           'PageInformation':PageInformation,
                                           })
#페이지 넘겼을 때 작동되는 함수
def CoursePage(request, offset, offset2):
	if request.user.username == "":
		return HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
			offset2 = int(offset2)
		except:
			raise Http404()

		PageInformation=[1,1,1]
		CourseBoard = TotalCourse(offset)
		O_Count = Course_Evaluation.objects.filter(Course = Lecture.objects.get(id = offset)).count()/3+1
		UserProfile=Profile.objects.get(User=request.user)
		try:
			MyCourseBoard = Course_Evaluation.objects.get(CreatedID = UserProfile)
                                #자신 이외 다른사람이 추천한 정보 보여줌
		except:
			MyCourseBoard = None
		if MyCourseBoard is None:
			MyCourseBoard = Course_Evaluation(Course = Lecture.objects.get(id=offset), CreatedID = UserProfile)
		#이전페이지 다음페이지 기능 구현
		PageInformation[1]=offset2
		if O_Count >11:
			if offset>11:
				PageInformation[0] = (offset2 -(offset2%10))-9
				PageInformation[2] = (offset2 -(offset2%10))+11
			elif (offset2+10)>O_Count:
				PageInformation[0] = (offset2 -(offset2%10))-9
				PageInformation[2] = O_Count           
			else:
				PageInformation[0] = 1
				PageInformation[2] = (offset2 - (offset2%10))+11
		else:
			PageInformation[0] = 1
			PageInformation[2] = O_Count
		
		#해당 페이지에 출력할 데이터들 갯수 정하는 기능
		PageFirst = (offset2-1)*2
		PageLast = (offset2-1)*2+2
		OtherCourse = Course_Evaluation.objects.filter(Course = Lecture.objects.get(id = offset)).order_by('-id')[PageFirst:PageLast]
		
		OtherCourseBoard = []
		#접속한 아이디와 중복되는 경우 제거
		for Board in OtherCourse:
			if Board.CreatedID == UserProfile:
					pass
			else:
				OtherCourseBoard.append(Board)


		if (PageInformation[1]/10) >= O_Count/10:
			OtherCount = range(PageInformation[1]-(PageInformation[1]%10)+1,O_Count+1)
		else:
			OtherCount = range(PageInformation[1]-(PageInformation[1]%10)+1,PageInformation[1]-(PageInformation[1]%10)+11)

		return render_to_response("course.html",
                                          {'user':request.user,
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