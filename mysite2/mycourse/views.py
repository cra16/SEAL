# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from mycourse.models import *
from django.views.decorators.csrf import csrf_exempt
from functionhelper.views import *
import datetime
def MyCourse(request):
        
		CheckingLogin(request.user.username)
		Data=MyCoursePage(request,1)
		return render_to_response("mycourses.html", Data)

def MyCoursePage(request,Page):
	CheckingLogin(request.user.username)
	MyProfile = Profile.objects.get(User=request.user)
	
	PageFirst=5*(int(Page)-1)
	PageLast =5*(int(Page)-1)+5

	RecommendPage=[]
	LikePage=[]
	
	Recommend = Recommend_Course.objects.filter(CreatedID = MyProfile)[PageFirst:PageLast]			
	
	for Board in Recommend:
		try :
			RecommendData = Total_Evaluation.objects.get(Course=Board.Course.Course)
		except:
			RecommendData = None
		RecommendPage.append(RecommendData)	

	Like=Like_Course.objects.filter(CreatedID = MyProfile)[PageFirst:PageLast]

	for Board2 in Like:
			try :
					LikeData=Total_Evaluation.objects.get(Course=Board2.Course)
			except:
					LikeData = Total_Evaluation(Course =Board2.Course)
					LikeData.Total_Speedy=5
					LikeData.Total_Reliance =5
					LikeData.Total_Question=5
					LikeData.Total_Helper=5
					LikeData.Total_Exam =5
					LikeData.Total_Homework = 5

			LikePage.append(LikeData)
	Count = [[],[]]
	DBCount=Course_Evaluation.objects.filter(CreatedID = MyProfile).count()
	Count[0] = DataCount(5,DBCount)
	DBCount=Like_Course.objects.filter(CreatedID = MyProfile).count()
	Count[1]=DataCount(5,DBCount)
	
	PageInformation=list()
	TotalCount=list()
	for i in range(0,2):
		PageInformation.append(FirstPageView(Count[i]))									
		TotalCount.append(PageTotalCount(Count[i],PageInformation[i]))

	MyCoursePageData=dict()
	MyCoursePageData={'user':request.user, 
						'BestBoard':BestBoardView(),
						'RecommendPage':RecommendPage,
						'LikePage':LikePage,
						'PageInformation' : PageInformation,
						'TotalCount':TotalCount
						}
	return MyCoursePageData
@csrf_exempt
def MyCoursePageNation(request):
	CheckingLogin(request.user.username)


	if request.method =="POST":
		Page = int(request.POST['Page'])
		CurrentPage = request.POST['CurrentPage']
	CheckingLogin(request.user.username)
	Data=MyCoursePage(request,Page)
	if CurrentPage == "RecommendPageNation":
		template="RecommendPage.html"
	else:
		template ="LikePage.html"
	return render_to_response(template, Data)



# Create your views here.
