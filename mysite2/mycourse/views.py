# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from mycourse.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime

def MyCourse(request):
	#여기 디비 그냥 날려버릴까 ... 빡치네 ㅋㅋㅋㅋ 이미 하고있엇어 ㅋㅋㅋㅋ
        if request.user.username =="":
                return HttpResponseRedirect("/mysite2")
        else:
			MyProfile = Profile.objects.get(User=request.user)
			PageInformation1 = [1,1,1]
			PageInformation2 = [1,1,1]
			RecommendPage=[]
			LikePage=[]
			
			Recommend = Course_Evaluation.objects.filter(CreatedID = MyProfile)[0:5]
			R_Count = Course_Evaluation.objects.filter(CreatedID = MyProfile).count()/6+1
			RecommendPage = []
			for Board in Recommend:
				try :
					RecommendData = Total_Evaluation.objects.get(CourseName=Board.Course)
				except:
					RecommendData = Total_Evaluation(CourseName=Board.Course, Total_Speedy=5, Total_Helper =5, Total_Homework=5, Total_Reliance =5, Total_Question=5, Total_Exam=5)
				RecommendPage.append(RecommendData)




			Like=Like_Course.objects.filter(CreatedID = MyProfile)[0:5]
			L_Count=Like_Course.objects.filter(CreatedID = MyProfile).count()/6+1
			LikePage = []

			for Board2 in Like:
					try :
					     	LikeData=Total_Evaluation.objects.get(CourseName=Board2.Course)
					except:
							LikeData=Total_Evaluation(CourseName = Board2.Course)
							LikeData.Total_Speedy=5
							LikeData.Total_Reliance =5
							LikeData.Total_Question=5
							LikeData.Total_Helper=5
							LikeData.Total_Exam =5
							LikeData.Total_Homework = 5
					LikePage.append(LikeData) 
			if R_Count>11:
				PageInformation1[0] = 1
				PageInformation1[2] = 11
			else :
				PageInformation1[0] = 1
				PageInformation1[2] = R_Count
			if L_Count>11:
				PageInformation2[0] =1
				PageInformation2[2] =11
			else:
				PageInformation2[0]= 1
				PageInformation2[2]= L_Count




			return render_to_response("mycourses.html", {'user':request.user, 
														'RecommendPage':RecommendPage,
														'LikePage':Like,
														'PageInformation1' : PageInformation1,
														'PageInformation2' : PageInformation2,
														'R_Count' : range(1,R_Count+1),
														'L_Count' : range(1,L_Count+1),
														})
#def MyCoursePage(request, offset)




# Create your views here.
