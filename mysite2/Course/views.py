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

		if request.user.username =="":
				return  HttpResponseRedirect("/mysite2")
		else:
				try:
						offset = int(offset)
				except:
						raise Http404()

				 #해당 강의 전체 추천한 Data DB 불러오기
				try:
						CourseBoard = Total_Evaluation.objects.get(CourseName = Lecture.objects.get(id = offset))
						CourseBoard.Total_Speedy = CourseBoard.Total_Speedy/CourseBoard.Total_Count
						CourseBoard.Total_Reliance = CourseBoard.Total_Reliance/CourseBoard.Total_Count
						CourseBoard.Total_Helper = CourseBoard.Total_Helper/CourseBoard.Total_Count
						CourseBoard.Total_Question = CourseBoard.Total_Question/CourseBoard.Total_Count
						CourseBoard.Total_Exam = CourseBoard.Total_Exam/CourseBoard.Total_Count
						CourseBoard.Total_Homework = CourseBoard.Total_Homework/CourseBoard.Total_Count
				except:
						CourseBoard = Total_Evaluation(CourseName =Lecture.objects.get(id=offset))
						CourseBoard.Total_Speedy=5
						CourseBoard.Total_Reliance =5
						CourseBoard.Total_Question=5
						CourseBoard.Total_Helper=5
						CourseBoard.Total_Exam =5
						CourseBoard.Total_Homework = 5

				

				
				

				#현재 접속한 사람이 추천한 자료 보여주는 기능(하지 않았을 시 default 5로 함)
				try:
						MyCourseBoard = Course_Evaluation.objects.get(CreatedID = Profile.objects.get(User=request.user))
                                #자신 이외 다른사람이 추천한 정보 보여줌
				except:
						MyCourseBoard = Course_Evaluation(CreatedID = Profile.objects.get(User=request.user))


				OtherCourseBoard = Course_Evaluation.objects.filter(Course = Lecture.objects.get(id = offset)).order_by('-id')[0:3]

				return render_to_response("course.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                           'MyCourseBoard':MyCourseBoard,
                                           'OtherCourseBoard':OtherCourseBoard,
                                          
                                        

                                           })

# Create your views here.
