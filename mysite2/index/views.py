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
	return render_to_response("sealmypage.html", {'user':request.user,'BestBoard':BestBoardView()}) 

def About(request): #About template 루트
	CheckingLogin(request.user.username)
	return render_to_response("about.html",{'user':request.user, 'BestBoard':BestBoardView()})

def Schedule(request): #Schedule template 기능
	CheckingLogin(request.user.username)
	return render_to_response("schedule.html",{'user':request.user,'BestBoard':BestBoardView()})

def Judgement(request): # 신고 게시판 기능
	CheckingLogin(request.user.username)
	return render_to_response("subscribe_report.html",{'user':request.user,'BestBoard':BestBoardView()})

@csrf_exempt
def Page(request): #Main 기능
	CheckingLogin(request.user.username)	

	try:
			if request.POST['Page'] !="0":
					cur_page = int(request.POST['Page'])
			else:
					cur_page = 1
			Current = request.POST['Current']
	except ValueError:
			raise Http404() 

	target = TargetTemplate(Current)
	template = MainPageView(request.user, request.session['PageInformation'],cur_page,int(target[1]))
	request.session['PageInformation'] = template['PageInformation']
	
	return render_to_response(target[0],template)
@csrf_exempt
def FirstPage(request):
	CheckingLogin(request.user.username)	

	try:
			if request.POST['Page'] !="0":
					cur_page = int(request.POST['Page'])
			else:
					cur_page = 1
			Current = request.POST['Current']
	except ValueError:
			raise Http404() 

	target = TargetTemplate(Current)
	template = MainPageView(request.user, request.session['PageInformation'],cur_page,int(target[1]))
	request.session['PageInformation'] = template['PageInformation']
	
	return render_to_response(target[0],template)
@csrf_exempt
def SecondPage(request):
	CheckingLogin(request.user.username)	

	try:
			if request.POST['Page'] !="0":
					cur_page = int(request.POST['Page'])
			else:
					cur_page = 1
			Current = request.POST['Current']
	except ValueError:
			raise Http404() 

	target = TargetTemplate(Current)
	template = MainPageView(request.user, request.session['PageInformation'],cur_page,int(target[1]))
	request.session['PageInformation'] = template['PageInformation']
	
	return render_to_response(target[0],template)

@csrf_exempt
def ThirdPage(request):
	CheckingLogin(request.user.username)	

	try:
			if request.POST['Page'] !="0":
					cur_page = int(request.POST['Page'])
			else:
					cur_page = 1
			Current = request.POST['Current']
	except ValueError:
			raise Http404() 

	target = TargetTemplate(Current)
	template = MainPageView(request.user, request.session['PageInformation'],cur_page,int(target[1]))
	request.session['PageInformation'] = template['PageInformation']
	
	return render_to_response(target[0],template)

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


		return render_to_response("mycourses.html", {'user':request.user, 
								  					'RecommendPage':RecommendPage,
								  					'BestBoard':BestBoardView()})
@csrf_exempt
def Search(request): #전체 검색 기능
	CheckingLogin(request.user.username)

	if request.method =="POST":
		SearchData = request.POST['search']
		#여기 문제
		LectureData = [[]]
		LectureData[0]=Lecture.objects.filter(CourseName__contains=SearchData).order_by('Code')[0:5]
		

		DBCount = Lecture.objects.filter(CourseName__contains=SearchData).count()
		SearchCount=DataCount(5,DBCount)


		L_Data=PageView(LectureData)
		PageInformation =[1,1,1]

		PageInformation=FirstPageView(SearchCount)

		T_Count = PageTotalCount(SearchCount,PageInformation)

		request.session['SearchPageInformation'] = PageInformation
		request.session['SearchValue'] = SearchData
		return render_to_response('index.html', {
											'user':request.user,
											'BestBoard':BestBoardView(),
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
	
	
	DBCount = Lecture.objects.filter(CourseName__contains=SearchData).count()
	SearchCount = DataCount(5,DBCount)

	L_Data=PageView(LectureData)
	
	PageInformation = CurrentPageView(SearchCount,offset)
	T_Count=PageTotalCount(SearchCount,PageInformation)
	

	request.session['SearchPageInformation'] = PageInformation
	return render_to_response('index.html', {
										'user':request.user,
										'BestBoard':BestBoardView(),
										'Search' : L_Data,
										'PageInformation' : PageInformation,
										'T_Count' : T_Count,
									})


                                                                  


# Create your views here
