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
		if request.method =="POST":
			PostDic = dict()
			for key in request.POST.keys(): #현재 ajax에서 받아온 post값들 key를 비교해서 dictionary로 표현해서 씀
				Data=request.POST[key]	
				PostDic[key] =request.POST[key]
			if 'Course' in request.POST.keys(): 
				if request.POST['Course']!="": # 강의 이름이 입력 되었을 때 해당 강의이름의 code까지 얻어 오기 위함
					if 'Code' not in request.POST.keys():
						A=Lecture.objects.filter(CourseName =PostDic['Course'])[0]
						PostDic['Code']= A.Code
			else:
				PostDic['Course']= ""
			if 'ProSelect' not in request.POST.keys():
				PostDic['ProSelect'] = 0
			
	except ValueError:
			raise Http404() 
	if PostDic['Current'] =="FirstPage" or PostDic['Current'] =="FirstPageNation":
		Page = "0"
	elif PostDic['Current'] =="SecondPage" or PostDic['Current'] =="SecondPageNation":
		Page ="1"
	elif PostDic['Current'] =="ThirdPage" or PostDic['Current'] =="ThirdPageNation":
		Page="2"
	else:
		Page ="0" #어디쪽에 뿌릴지 결정함

	PostDic['Page']= PostDic['Page'] !="0" and PostDic['Page'] or "1" #페이지 위치에 따른 값 결정
	
	if PostDic['Course'] == "": #그냥 전체강의에서 pagenation 하는 경우
		#웹에 뿌려줄 template 종류 정하는 함수(functionhelper 참고)
		target = TargetTemplate(PostDic['Current'])
		#메인에다가 강의 정보 뿌려주는 함수(functionhelper 참고)
		template = MainPageView(request.user, request.session['PageInformation'],int(PostDic['Page']),int(Page))
	elif PostDic['ProSelect'] == "1":
		target = TargetTemplate(PostDic['Current'])
		#메인에다가 강의 정보 뿌려주는 함수(functionhelper 참고)
		template =  SelectProfessorView(request.user,  request.session['PageInformation'],int(PostDic['Page']),int(Page),PostDic)

	else: #반대의 경우
		target = TargetTemplate(PostDic['Current'])
		template = SelectPageView(request.user,  request.session['PageInformation'],int(PostDic['Page']),int(Page),PostDic)
	
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
		TotalAdd=[]
		j=0
		try: 
			"""
			밑의 알고리즘은 현재 DB에 등록 되어있는 강의 이름을 토대로 group by로 묶어서 중복되는 강의이름을 하나로 묶어 버린후에
			그 강의이름 정보를 토대로 다시 DB에서 호출하는데 그 강의중 중복되는 정보만 추출하면 되는 거라 하나씩 불러서 그 부른 강의들을
			list화 시킴. 그리고 나서 그 list화 시킨 강의 정보를 다시 전체 평가 한 강의 부분 DB에서 다시 호출해 강의마다 평가된 
			평가 갯수를 다 더해서 함
			ps)물론 DB하나 더 만들면 더 간단한 알고리즘이 되겠지만 어차피 DB에서 한번더 불러야 하는건 마찬가지라 속도가 비슷할 거같아서
			안만듬
			"""
			temp=Lecture.objects.values('CourseName').annotate(Count('CourseName')).filter(CourseName__icontains=SearchData).order_by('-Semester')[0:10]
			for lec in temp:

					A=Lecture.objects.filter(CourseName=lec['CourseName'])		
					LectureData[0].append(Lecture.objects.filter(CourseName=lec['CourseName'])[0])
					total=0
					for tolec in A:
						try:
								Eval=Total_Evaluation.objects.get(Course=tolec)
								total += Eval.Total_Count
						except:
							continue
					TotalAdd.append(total)
	
		except:
			LectureData[0]=None

		DBCount = Lecture.objects.values('CourseName').annotate(Count('CourseName')).filter(CourseName__icontains=SearchData).count()
		SearchCount=DataCount(10,DBCount)
		
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
				'TotalCount':T_Count,
				'TotalAdd':TotalAdd
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


	DBCount = Lecture.objects.values('CourseName').annotate(Count('CourseName')).filter(CourseName__icontains=SearchData).count()
	SearchCount = DataCount(10,DBCount)
	PageInformation = CurrentPageView(SearchCount,cur_page)
	PageInformation[1]=cur_page

	
	LectureData = [[]]
	TotalAdd=[]
	j=0
	temp=Lecture.objects.values('CourseName').annotate(Count('CourseName')).filter(CourseName__icontains=SearchData).order_by('-Semester')[(PageInformation[1]-1)*10:(PageInformation[1]-1)*10+10]
	for lec in temp:
				if lec['CourseName'] not in LectureData[0]:		
					A=Lecture.objects.filter(CourseName=lec['CourseName'])		
					LectureData[0].append(Lecture.objects.filter(CourseName=lec['CourseName'])[0])
					total=0
					for tolec in A:
						try:
							Eval=Total_Evaluation.objects.get(Course=tolec)
							total += Eval.Total_Count  
						except:
							continue
					TotalAdd.append(total)
	

	L_Data=PageView(LectureData)
	
	
	T_Count=PageTotalCount(SearchCount,PageInformation)
		

	request.session['SearchPageInformation'] = PageInformation
	
	dic = {
				'user':request.user,
				'BestBoard':BestBoardView(),
				'Search' : L_Data,
				'PageInformation' : PageInformation,
				'TotalCount' : T_Count,
				'TotalAdd':TotalAdd,
				
				
			}
	if request.flavour =='full':
			return render_to_response('html/SearchPage.html',dic)
	else:
			return render_to_response('m_skins/m_html/SearchPage.html',dic )


# Create your views here
