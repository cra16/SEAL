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

#현재 내가 추천한 강의 보여주는 함수
def MyCourse(request):
		if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")
        
		Mobile = request.flavour
		Data=MyCoursePage(request,1,Mobile)
		if request.flavour =='full':
			return render_to_response('html/mycourses.html',Data)
		else:
			return render_to_response("m_skins/m_html/mycourses.html", Data)
#위의 함수 세부함수
def MyCoursePage(request,Page,Mobile):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	try:
			PageFirst=5*(int(Page)-1)
			PageLast =5*(int(Page)-1)+5
	except:
		raise Http404()
	
	MyProfile = Profile.objects.get(User=request.user)
	

	RecommendPage=[]
	LikePage=[]
	
	Recommend = Recommend_Course.objects.filter(CreatedID = MyProfile)[PageFirst:PageLast]			
	
	for Board in Recommend:
		try :
			RecommendData = Total_Evaluation.objects.get(Course=Board.Course.Course)
		except:
			RecommendData = None
		if RecommendData.Total_Count==0:
			RecommendPage.append(RecommendData)
			break
		RecommendData.Total_Speedy=RecommendData.Total_Speedy/RecommendData.Total_Count
		RecommendData.Total_Reliance =RecommendData.Total_Reliance/RecommendData.Total_Count
		RecommendData.Total_Question=RecommendData.Total_Question/RecommendData.Total_Count
		RecommendData.Total_Helper=RecommendData.Total_Helper/RecommendData.Total_Count
		RecommendData.Total_Exam = RecommendData.Total_Exam/RecommendData.Total_Count
		RecommendData.Total_Homework = RecommendData.Total_Homework/RecommendData.Total_Count
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
			if LikeData.Total_Count==0:
				LikePage.append(LikeData)
				break
	
			LikeData.Total_Speedy=LikeData.Total_Speedy/LikeData.Total_Count
			LikeData.Total_Reliance =LikeData.Total_Reliance/LikeData.Total_Count
			LikeData.Total_Question=LikeData.Total_Question/LikeData.Total_Count
			LikeData.Total_Helper=LikeData.Total_Helper/LikeData.Total_Count
			LikeData.Total_Exam = LikeData.Total_Exam/LikeData.Total_Count
			LikeData.Total_Homework = LikeData.Total_Homework/LikeData.Total_Count
			LikePage.append(LikeData)
	Count = [[],[]]
	DBCount=Course_Evaluation.objects.filter(CreatedID = MyProfile).count()
	Count[0] = DataCount(5,DBCount)
	DBCount=Like_Course.objects.filter(CreatedID = MyProfile).count()
	Count[1]=DataCount(5,DBCount)
	
	PageInformation=list()
	TotalCount=list()
	if Mobile == "full":

		for i in range(0,2):
			PageInformation.append(CurrentPageView(Count[i],Page))									
			TotalCount.append(PageTotalCount(Count[i],PageInformation[i]))
	else:
		for i in range(0,2):
			PageInformation.append(MobileCurrentPageView(Count[i],Page))									
			TotalCount.append(MobilePageTotalCount(Count[i],PageInformation[i]))

	MyCoursePageData=dict()
	MyCoursePageData={'user':request.user, 
						'BestBoard':BestBoardView(),
						'RecommendPage':RecommendPage,
						'LikePage':LikePage,
						'PageInformation' : PageInformation,
						'TotalCount':TotalCount,
						'Page':Page
						}
	return MyCoursePageData
#MyCourse쪽 비동기식 구현
@csrf_exempt
def MyCoursePageNation(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")


	if request.method =="POST":
		Page = int(request.POST['Page'])
		CurrentPage = request.POST['CurrentPage']
	CheckingLogin(request.user.username)
	Data=MyCoursePage(request,Page,request.flavour)
	if CurrentPage == "RecommendPageNation":
		template="RecommendPage.html"
	else:
		template ="LikePage.html"
	if request.flavour =='full':
			return render_to_response('html/'+template,Data)
	else:
			return render_to_response('m_skins/m_html/'+template, Data)



# Create your views here.
