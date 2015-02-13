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
@csrf_exempt
def Recommend(request, offset): #강의 추천 스크롤 기능

	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except:
			raise Http404()


		

		CourseBoard = Lecture.objects.get(id=offset) #DB 고유 ID로 접근해서 검색		
		request.session['Recommend_ID'] = offset #offset 미리 저장

		return render_to_response("recommend.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                         #  'TotalCount' : range(0,TotalCount)
											})
@csrf_exempt
def Recommend_Write(request): #추천 강의 DB입력

        if request.user.username=="":
                return HttpResponseRedirect("/mysite2")
        else:
					#form 가져오기
					if request.method =="POST":
						new_Course=Lecture.objects.get(id=request.session['Recommend_ID'])
						new_CreatedID = Profile.objects.get(User= request.user)
						new_Speedy=request.POST['sl1']
						new_Reliance=request.POST['sl2']
						new_Helper=request.POST['sl3']
						new_Question=request.POST['sl4']
						new_Exam=request.POST['sl5']
						new_Homework=request.POST['sl6']
						new_Eval = Course_Evaluation(Course = new_Course, CreatedID = new_CreatedID, Speedy = new_Speedy, Reliance = new_Reliance, Helper = new_Helper, Question = new_Question, Exam = new_Exam, Homework=new_Homework)
						new_Eval.save()



						L_Eval = Lecture.objects.get(id=request.session['Recommend_ID'])#해당 강의 정보를 일단 DB에서 불러옴

						try:
								T_Eval=Total_Evaluation.objects.get(CourseName=L_Eval)#위에서 부른 강의 정보를 바탕으로 해당 강의의 총 평가 Data 불러옴

						except:
								T_Eval =None 



						if T_Eval is None: #데이터 없을시 Table 생성

								Total_Eval = Total_Evaluation(CourseName = new_Course, Total_Speedy = new_Speedy, Total_Reliance = new_Reliance, Total_Helper = new_Helper, Total_Question = new_Question,Total_Exam = new_Exam,  Total_Homework = new_Homework, Total_Count =1)
								UserData = Profile.objects.get(User = request.user)
								UserData.RecommendCount+=1
								UserData.save()
								Total_Eval.save()
						else: #update
								T_Eval.Total_Speedy += int(new_Speedy)
								T_Eval.Total_Reliance += int(new_Reliance)
								T_Eval.Total_Helper += int(new_Helper)
								T_Eval.Total_Question += int(new_Question)
								T_Eval.Total_Exam += int(new_Question)
								T_Eval.Total_Homework += int(new_Homework)
								T_Eval.Total_Count += 1
								T_Eval.save()
						
						URL = "/mysite2/Course/"+str(request.session['Recommend_ID'])
						return render_to_response("course.html",{'user':request.user,})

					else:
						return HttpResponseRedirect("/mysite2")


# Create your views here.
