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

#메인페이지 ajax 구현해서 만든 함수 PAge는 다 똑같아서 하나로 줄일까 생각중
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

def SubScript(request): #아직 뭐하는 기능인지 모르겠음
	CheckingLogin(request.user.username)
	return render_to_response("subscribe_improve.html", {'user':request.user})

def SiteMap(request): #사이트 맵
	CheckingLogin(request.user.username)
	return render_to_response("sitemap.html", {'user':request.user})

def MyCourse(request): #내가 추천한 목록 보여주는 페이지로 감
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
def Search(request): #과목 검색 기능
	CheckingLogin(request.user.username)

	if request.method =="POST":
		SearchData = request.POST['search']
		SearchData.upper()
		#여기 문제
		LectureData = [[]]
		try:
			LectureData[0]=Lecture.objects.filter(CourseName__icontains=SearchData).order_by('-Semester')[0:5]
		except:
			LectureData[0]=None

		DBCount = Lecture.objects.filter(CourseName__icontains=SearchData).count()
		SearchCount=DataCount(5,DBCount)
		if DBCount != 0 : 
			L_Data=PageView(LectureData)
		else:
			L_Data=[[]]
			L_Data[0]=None
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
@csrf_exempt
def SearchPage(request):#Search부분 ajax pagenation을 위해 만든 부분
	CheckingLogin(request.user.username)

	if request.POST['Page'] !="0":
		cur_page = int(request.POST['Page'])
	else:
		cur_page = 1
		Current = request.POST['Current']

	SearchData = request.session['SearchValue']
	
	PageInformation = request.session['SearchPageInformation']
	PageInformation[1] = cur_page
	LectureData = [[]]
	LectureData[0]=Lecture.objects.filter(CourseName__icontains=SearchData).order_by('-Semester')[(PageInformation[1]-1)*5:(PageInformation[1]-1)*5+5]
	
	
	DBCount = Lecture.objects.filter(CourseName__icontains=SearchData).count()
	SearchCount = DataCount(5,DBCount)

	L_Data=PageView(LectureData)
	
	PageInformation = CurrentPageView(SearchCount,cur_page)
	T_Count=PageTotalCount(SearchCount,PageInformation)
	

	request.session['SearchPageInformation'] = PageInformation
	return render_to_response('SearchPage.html', {
										'user':request.user,
										'BestBoard':BestBoardView(),
										'Search' : L_Data,
										'PageInformation' : PageInformation,
										'T_Count' : T_Count,
									})


                                                                  


# Create your views here
