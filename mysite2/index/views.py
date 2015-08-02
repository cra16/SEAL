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
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	dic = {'user':request.user,'BestBoard':BestBoardView()}
		
	if request.flavour =='full':
			return render_to_response('html/sealmypage.html',dic)
	else:	
			return render_to_response("m_skins/m_html/sealmypage.html", dic) 

def About(request): #About template 루트
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")

	dic = {'user':request.user, 'BestBoard':BestBoardView()}
	
	if request.flavour =='full':
			return render_to_response('html/about.html',dic)
	else:	
			return render_to_response("m_skins/m_html/about.html",dic)

def Schedule(request): #Schedule template 기능
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	
	dic={'user':request.user,'BestBoard':BestBoardView()}

	if request.flavour =='full':
		return render_to_response('html/schedule.html',dic)
	else:
		return render_to_response("m_skins/m_html/schedule.html", dic)

def Judgement(request): # 신고 게시판 기능

	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	dic = {'user':request.user,'BestBoard':BestBoardView()}
	if request.flavour =='full':
		return render_to_response('html/subscribe_report.html',dic)
	else:
		return render_to_response("m_skins/m_html/subscribe_report.html",dic)


@csrf_exempt
def Page(request): #Main Page를 보여주는 함수 
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	try:
			if request.POST['Page'] !="0":
					cur_page = int(request.POST['Page'])
			else:
					cur_page = 1
			Current = request.POST['Current']
			if request.POST['Course'] !="null":
				CourseName = request.POST['Course']
			else:
				CourseName = None

	except ValueError:
			raise Http404() 
	if Current =="FirstPage" or Current =="FirstPageNation":
		Page = "0"
	elif Current =="SecondPage" or Current =="SecondPageNation":
		Page ="1"
	elif Current =="AllPage" or Current =="AllPageNation":
		Page="2"

	
	if CourseName == None:
		#웹에 뿌려줄 template 종류 정하는 함수(functionhelper 참고)
		target = TargetTemplate(Current)
		#메인에다가 강의 정보 뿌려주는 함수(functionhelper 참고)
		template = MainPageView(request.user, request.session['PageInformation'],cur_page,int(target[1]))
	else:
		target = TargetTemplate(Current)

		template = SelectPageView(request.user, request.session['PageInformation'],cur_page,int(Page),CourseName)
	
	#왜 했는지 기억안남...
	request.session['PageInformation'] = template['PageInformation']
	if request.flavour =='full':
		return render_to_response('html/'+target[0],template)
	else:
		return render_to_response('m_skins/m_html/'+target[0],template)

def SubScript(request): #아직 뭐하는 기능인지 모르겠음
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")

	dic = {'user':request.user}

	if request.flavour =='full':
		return render_to_response('html/subscribe_improve.html',dic)
	else:
		return render_to_response("m_skins/m_html/subscribe_improve.html",dic)

def SiteMap(request): #사이트 맵
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	dic = {'user':request.user}

	if request.flavour =='full':
		return render_to_response('html/sitemap.html',dic)
	else:
		return render_to_response("m_skins/m_html/sitemap.html",dic )

def MyCourse(request): #내가 추천한 목록 보여주는 페이지로 감
		if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/mysite2")
		MyProfile = Profile.objects.get(User=request.user)
		
		LikePage=LikePage_Course.objects.filter(CreatedID= MyProfile)
		RecommendPage= Recommend_Course.objects.filter(CreatedID = MyProfile)
		
		dic = {'user':request.user, 
				'RecommendPage':RecommendPage,
				'LikePage':LikePage,
				'BestBoard':BestBoardView()}
		if request.flavour =='full':
			return render_to_response('html/mycourses.html',dic)
		else:
			return render_to_response("m_skins/m_html/mycourses.html", dic)
@csrf_exempt
def Search(request): #과목 검색 기능
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")

	if request.method =="POST":
		SearchData = request.POST['search']
		SearchData.upper()
		#여기 문제
		LectureData = [[]]
		
		try:
			temp=Lecture.objects.values('CourseName').annotate(Count('CourseName')).filter(CourseName__icontains=SearchData).order_by('-Semester')[0:5]
			for lec in temp:
				if lec['CourseName'] not in LectureData[0]:		
					LectureData[0].append(Lecture.objects.filter(CourseName=lec['CourseName'])[0])
	
		except:
			LectureData[0]=None

		DBCount = Lecture.objects.values('CourseName').annotate(Count('CourseName')).filter(CourseName__icontains=SearchData).count()
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

		dic = {
				'user':request.user,
				'BestBoard':BestBoardView(),
				'Search' : L_Data,
				'PageInformation' : PageInformation,
				'T_Count':T_Count,
			}
		if request.flavour =='full':
			return render_to_response('html/index.html',dic)
		else:
			return render_to_response('m_skins/m_html/index.html', dic)
	else:
		return HttpResponseRedirect("/mysite2")
@csrf_exempt
def SearchPage(request):#Search부분 ajax pagenation을 위해 만든 부분
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")

	if request.POST['Page'] !="0":
		cur_page = int(request.POST['Page'])
	else:
		cur_page = 1
		Current = request.POST['Current']

	SearchData = request.session['SearchValue']
	
	PageInformation = request.session['SearchPageInformation']
	PageInformation[1] = cur_page
	LectureData = [[]]
	temp=Lecture.objects.values('CourseName').annotate(Count('CourseName')).filter(CourseName__icontains=SearchData).order_by('-Semester')[(PageInformation[1]-1)*5:(PageInformation[1]-1)*5+5]
	for lec in temp:
				if lec['CourseName'] not in LectureData[0]:		
					LectureData[0].append(Lecture.objects.filter(CourseName=lec['CourseName'])[0])
	
	DBCount = Lecture.objects.filter(CourseName__icontains=SearchData).count()
	SearchCount = DataCount(5,DBCount)

	L_Data=PageView(LectureData)
	
	PageInformation = CurrentPageView(SearchCount,cur_page)
	T_Count=PageTotalCount(SearchCount,PageInformation)
	

	request.session['SearchPageInformation'] = PageInformation
	
	dic = {
				'user':request.user,
				'BestBoard':BestBoardView(),
				'Search' : L_Data,
				'PageInformation' : PageInformation,
				'T_Count' : T_Count,
			}
	if request.flavour =='full':
			return render_to_response('html/SearchPage.html',dic)
	else:
			return render_to_response('m_skins/m_html/SearchPage.html',dic )


# Create your views here
