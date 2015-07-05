# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from mycourse.models import *
from django.views.decorators.csrf import csrf_exempt
from functionhelper.views import CheckingLogin, FirstPageView
import datetime
def MyCourse(request):
        
		CheckingLogin(request.user.username)
		Data=MyCoursePage(request)
		return render_to_response("mycourses.html", Data)

def MyCoursePage(request):
	MyProfile = Profile.objects.get(User=request.user)
	PageInformation = [[1,1,1],[1,1,1]]
	RecommendPage=[]
	LikePage=[]
	
	Recommend = Course_Evaluation.objects.filter(CreatedID = MyProfile)[0:5]			
	
	for Board in Recommend:
		try :
			RecommendData = Total_Evaluation.objects.get(Course=Board.Course)
		except:
			RecommendData = Total_Evaluation(Course=Board.Course, Total_Speedy=5, Total_Helper =5, Total_Homework=5, Total_Reliance =5, Total_Question=5, Total_Exam=5)
		RecommendPage.append(RecommendData)

	Like=Like_Course.objects.filter(CreatedID = MyProfile)[0:5]

	for Board2 in Like:
			try :
					LikeData=Total_Evaluation.objects.get(Course=Board2.Course)
			except:
					LikeData=Total_Evaluation(Course = Board2.Course)
					LikeData.Total_Speedy=5
					LikeData.Total_Reliance =5
					LikeData.Total_Question=5
					LikeData.Total_Helper=5
					LikeData.Total_Exam =5
					LikeData.Total_Homework = 5
			LikePage.append(LikeData)
	Count = [[],[]]
	Count[0] = Course_Evaluation.objects.filter(CreatedID = MyProfile).count()/6+1
	Count[1]=Like_Course.objects.filter(CreatedID = MyProfile).count()/6+1
	
	for i in range(0,2):
		FirstPageView(Count)												

	MyCoursePageData=dict()
	MyCoursePageData={'user':request.user, 
						'RecommendPage':RecommendPage,
						'LikePage':Like,
						'PageInformation' : PageInformation,
						'R_Count' : range(1,Count[0]+1),
						'L_Count' : range(1,Count[1]+1),
						}
	return MyCoursePageData
			



# Create your views here.
