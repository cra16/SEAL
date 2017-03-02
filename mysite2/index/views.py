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
		return HttpResponseRedirect("/")
	dic = {'user':request.user,'BestBoard':BestBoardView()}
		
	if request.flavour =='full':
			return render_to_response('html/sealmypage.html',dic)
	else:	
			return render_to_response("m_skins/m_html/sealmypage.html", dic) 

def About(request): #About template 루트
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")

	dic = {'user':request.user, 'BestBoard':BestBoardView()}
	
	if request.flavour =='full':
			return render_to_response('html/about.html',dic)
	else:	
			return render_to_response("m_skins/m_html/about.html",dic)

def Schedule(request): #Schedule template 기능
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	
	dic={'user':request.user,'BestBoard':BestBoardView()}

	if request.flavour =='full':
		return render_to_response('html/schedule.html',dic)
	else:
		return render_to_response("m_skins/m_html/schedule.html", dic)

def Judgement(request): # 신고 게시판 기능

	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	dic = {'user':request.user,'BestBoard':BestBoardView()}
	if request.flavour =='full':
		return render_to_response('html/subscribe_report.html',dic)
	else:
		return render_to_response("m_skins/m_html/subscribe_report.html",dic)


@csrf_exempt
def Page(request): #Main Page를 보여주는 함수 
	mobile = request.flavour
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
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
	elif PostDic['Current'] =="SugangPage" or PostDic['Current'] =="SugangPageNation":
		Page="3"
	elif PostDic['Current'] =="LikeSugangPage" or PostDic['Current'] =="LikeSugangPageNation":
		Page="4"
	else:
		Page ="0" #어디쪽에 뿌릴지 결정함

	PostDic['Page']= PostDic['Page'] !="0" and PostDic['Page'] or "1" #페이지 위치에 따른 값 결정
	
	if PostDic['Course'] == "": #그냥 전체강의에서 pagenation 하는 경우
		#웹에 뿌려줄 template 종류 정하는 함수(functionhelper 참고)
		target = TargetTemplate(PostDic['Current'])
		#메인에다가 강의 정보 뿌려주는 함수(functionhelper 참고)
		template = MainPageView(request.user, request.session['PageInformation'],int(PostDic['Page']),int(Page),mobile)
	elif PostDic['ProSelect'] == "1":
		target = TargetTemplate(PostDic['Current'])
		#메인에다가 강의 정보 뿌려주는 함수(functionhelper 참고)
		template =  SelectProfessorView(request.user,  request.session['PageInformation'],int(PostDic['Page']),int(Page),PostDic,mobile)

	else: #반대의 경우
		target = TargetTemplate(PostDic['Current'])
		#template = SelectPageView(request.user,  request.session['PageInformation'],int(PostDic['Page']),int(Page),PostDic,mobile)
	
	#왜 했는지 기억안남...
	request.session['PageInformation'] = template['PageInformation']
	if request.flavour =='full':
		return render_to_response('html/'+target[0],template)
	else:
		return render_to_response('m_skins/m_html/'+target[0],template)

def SubScript(request): #아직 뭐하는 기능인지 모르겠음
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")

	dic = {'user':request.user,'BestBoard':BestBoardView()}

	if request.flavour =='full':
		return render_to_response('html/subscribe_improve.html',dic)
	else:
		return render_to_response("m_skins/m_html/subscribe_improve.html",dic)

def SiteMap(request): #사이트 맵
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	dic = {'user':request.user}

	if request.flavour =='full':
		return render_to_response('html/sitemap.html',dic)
	else:
		return render_to_response("m_skins/m_html/sitemap.html",dic )

def MyCourse(request): #내가 추천한 목록 보여주는 페이지로 감
		if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")
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
		return HttpResponseRedirect("/")
	Mobile = request.flavour
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
			if Mobile == "full":
				temp=Lecture.objects.filter(Q(CourseName__icontains=SearchData) | Q(Professor__icontains=SearchData)).values("Code").distinct()[0:10]
			else:
				temp=Lecture.objects.filter(Q(CourseName__icontains=SearchData) | Q(Professor__icontains=SearchData)).values("Code").distinct()[0:5]
			LecList = []
			for lec in temp:
						A=Lecture.objects.filter(Code=lec['Code'])
						LectureData[0].append(A[0])
						
						total=0	
						
						try:
								Eval=Total_Evaluation.objects.filter(Course__Code=lec['Code'])
								for Ev in Eval:
									total += Ev.Total_Count  
						except:
							pass
						TotalAdd.append(total)
	
		except:
			LectureData[0]=None
		if Mobile == "full":
			DBCount = Lecture.objects.filter(Q(CourseName__icontains=SearchData) | Q(Professor__icontains=SearchData)).values("Code").distinct().count()
			SearchCount=DataCount(10,DBCount)
		else:
			DBCount = Lecture.objects.filter(Q(CourseName__icontains=SearchData) | Q(Professor__icontains=SearchData)).values("Code").distinct().count()
			SearchCount=DataCount(5,DBCount)
		
		if DBCount != 0 : 
			L_Data=PageView(LectureData)
		else:
			L_Data=[[]]
			L_Data[0]=None
		PageInformation =[1,1,1]

		if Mobile =="full":
			PageInformation=FirstPageView(SearchCount)
			T_Count = PageTotalCount(SearchCount,PageInformation)
		else:
			PageInformation=MobileFirstPageView(SearchCount)
			T_Count = MobilePageTotalCount(SearchCount,PageInformation,3)

		request.session['SearchPageInformation'] = PageInformation
		request.session['SearchValue'] = SearchData

		dic = {
				'user':request.user,
				'BestBoard':BestBoardView(),
				'Search' : L_Data,
				'PageInformation' : PageInformation,
				'TotalCount':T_Count,
				'TotalAdd':TotalAdd,


			}
		if request.flavour =='full':
			return render_to_response('html/index.html',dic)
		else:
			return render_to_response('m_skins/m_html/index.html', dic)
	else:
		return HttpResponseRedirect("/")
@csrf_exempt
def SearchPage(request):#Search부분 ajax pagenation을 위해 만든 부분
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	Mobile = request.flavour
	if request.POST['Page'] !="0":
		cur_page = int(request.POST['Page'])
	else:
		cur_page = 1
		Current = request.POST['Current']

	SearchData = request.session['SearchValue']
	
	PageInformation = request.session['SearchPageInformation']

	if Mobile == 'full':
		DBCount = Lecture.objects.filter(Q(CourseName__icontains=SearchData) | Q(Professor__icontains=SearchData)).values("Code").distinct().distinct().count()
		SearchCount = DataCount(10,DBCount)
	else :
		DBCount = Lecture.objects.filter(Q(CourseName__icontains=SearchData) | Q(Professor__icontains=SearchData)).values("Code").distinct().count()
		SearchCount = DataCount(5,DBCount)
	
	if Mobile == 'full':
		PageInformation = CurrentPageView(SearchCount,cur_page)
		PageInformation[1]=cur_page
	else:
		PageInformation = MobileCurrentPageView(SearchCount,cur_page)
		PageInformation[1]=cur_page
	
	LectureData = [[]]
	TotalAdd=[]
	if Mobile == 'full':
		temp=Lecture.objects.filter(Q(CourseName__icontains=SearchData) | Q(Professor__icontains=SearchData)).values("Code").distinct()[(PageInformation[1]-1)*10:(PageInformation[1]-1)*10+10]
	else:
		temp=Lecture.objects.filter(Q(CourseName__icontains=SearchData) | Q(Professor__icontains=SearchData)).values("Code").distinct()[(PageInformation[1]-1)*5:(PageInformation[1]-1)*5+5]
	LecList=[]
	for lec in temp:
				A=Lecture.objects.filter(Code=lec['Code'])
				LectureData[0].append(A[0])
				
				total=0	
				
				try:
						Eval=Total_Evaluation.objects.filter(Course__Code=lec['Code'])
						for Ev in Eval:
							total += Ev.Total_Count  
				except:
					pass
				TotalAdd.append(total)

	L_Data=PageView(LectureData)
	
	if Mobile == 'full':
		T_Count=PageTotalCount(SearchCount,PageInformation)
	else:
		T_Count=MobilePageTotalCount(SearchCount,PageInformation,3)

	request.session['SearchPageInformation'] = PageInformation
	
	dic = {
				'user':request.user,
				'BestBoard':BestBoardView(),
				'Search' : L_Data,
				'PageInformation' : PageInformation,
				'TotalCount' : T_Count,
				'TotalAdd':TotalAdd,
				'Test':Total_Evaluation.objects.filter(Course__Code="GEK10041")
			}
	if request.flavour =='full':
			return render_to_response('html/SearchPage.html',dic)
	else:
			return render_to_response('m_skins/m_html/SearchPage.html',dic )

@csrf_exempt
def category_system(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	category_number = request.GET['category_number']

	if category_number == '1':
		category_name="학부"
		category_list =['국제어문','언론정보','경영경제','법학부','상담심리','생명과학','전산전자','콘텐츠융합디자인','기계제어','공간환경','ICT창업','창의융합교육원(인문사회)','창의융합교육원(이공)']
		subject_list = Lecture.objects.filter(Major__icontains='국제어문').values("Code","CourseName").distinct()
	elif category_number =='2':
		category_name="일반기초교양"
		category_list = ['신앙1','인성1','세계관1','세계관2','신앙3','예술','전공기초','사회과학','자연과학','리더십및문제해결','스포츠','기독교신앙기초1','기독교신앙기초2','영어1','영어2']
		subject_list = Lecture.objects.filter(CategoryDetail__icontains='신앙1').values("Code","CourseName").distinct()
	elif category_number =='3':
		category_name="글로벌"
		category_list = ['제2외국어','한국어','소통','융복합','프로그래밍기초','소프트웨어활용','ICT입문','특론및개별연구']
		subject_list=Lecture.objects.filter(CategoryDetail__icontains='제2외국어').values("Code","CourseName").distinct()
	else:
		pass
	dic = {
		'category_list':category_list,
		'category_name':category_name,
		'subject_list':subject_list
	}
	if request.flavour =='full':
			return render_to_response('html/category_list.html',dic)
	else:
			return render_to_response('m_skins/m_html/category_list.html',dic )
def select_subject_list(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")

	category_number = request.GET['category_number']
	category_select_name = request.GET['category_name']

	if category_number == '1':
		category_name="학부"
		category_list =['국제어문','언론정보','경영경제','법학부','상담심리','생명과학','전산전자','콘텐츠융합디자인','기계제어','공간환경','ICT창업','창의융합교육원(인문사회)','창의융합교육원(이공)']
		subject_list = Lecture.objects.filter(Major__icontains=category_select_name).values("Code","CourseName").distinct()
	elif category_number =='2':
		category_name="일반기초교양"
		category_list = ['신앙1','인성1','세계관1','세계관2','신앙3','예술','전공기초','사회과학','자연과학','리더십및문제해결','스포츠','기독교신앙기초1','기독교신앙기초2','영어1','영어2']
		subject_list = Lecture.objects.filter(CategoryDetail__icontains=category_select_name).values("Code","CourseName").distinct()
	elif category_number =='3':
		category_name="글로벌"
		category_list = ['제2외국어','한국어','소통','융복합','프로그래밍기초','소프트웨어활용','ICT입문','특론및개별연구']
		subject_list=Lecture.objects.filter(CategoryDetail__icontains=category_select_name).values("Code","CourseName").distinct()
	else:
		pass
	dic = {
		'category_list':category_list,
		'category_name':category_name,
		'subject_list':subject_list
	}
	if request.flavour =='full':
			return render_to_response('html/category_list.html',dic)
	else:
			return render_to_response('m_skins/m_html/category_list.html',dic )
# Create your views here
def search_subject_list(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	Mobile = request.flavour
	subject_code = request.GET['subject_category']
	subject = subject_code.split('-')
	TotalAdd=[]

	"""
	밑의 알고리즘은 현재 DB에 등록 되어있는 강의 이름을 토대로 group by로 묶어서 중복되는 강의이름을 하나로 묶어 버린후에
	그 강의이름 정보를 토대로 다시 DB에서 호출하는데 그 강의중 중복되는 정보만 추출하면 되는 거라 하나씩 불러서 그 부른 강의들을
	list화 시킴. 그리고 나서 그 list화 시킨 강의 정보를 다시 전체 평가 한 강의 부분 DB에서 다시 호출해 강의마다 평가된 
	평가 갯수를 다 더해서 함
	ps)물론 DB하나 더 만들면 더 간단한 알고리즘이 되겠지만 어차피 DB에서 한번더 불러야 하는건 마찬가지라 속도가 비슷할 거같아서
	안만듬
	"""
			
			
	LectureData=[[]]
	SearchResult = Lecture.objects.filter(Code=subject[0], CourseName=subject[1]).values("Code").distinct()[0:10]
	for lec in SearchResult:
						A=Lecture.objects.filter(Code=lec['Code'])
						LectureData[0].append(A[0])
						
						total=0	
						
						try:
								Eval=Total_Evaluation.objects.filter(Course__Code=lec['Code'])
								for Ev in Eval:
									total += Ev.Total_Count  
						except:
							continue
						TotalAdd.append(total)
	if Mobile == "full":
		DBCount = Lecture.objects.filter(Q(Code=subject[0]) | Q(CourseName=subject[1])).values("Code").distinct().count()
		SearchCount=DataCount(10,DBCount)
	else:
		DBCount = Lecture.objects.filter(Q(Code=subject[0]) | Q(CourseName=subject[1])).values("Code").distinct().count()
		SearchCount=DataCount(5,DBCount)
	
	if DBCount != 0 : 
		L_Data=PageView(LectureData)
	else:
		L_Data=[[]]
		L_Data[0]=None
	PageInformation =[1,1,1]

	if Mobile =="full":
		PageInformation=FirstPageView(SearchCount)
		T_Count = PageTotalCount(SearchCount,PageInformation)
	else:
		PageInformation=MobileFirstPageView(SearchCount)
		T_Count = MobilePageTotalCount(SearchCount,PageInformation,3)

	request.session['SearchPageInformation'] = PageInformation

	dic = {

				'PageInformation' : PageInformation,
				'user':request.user,
				'SubjectList':L_Data,
				'TotalAdd':TotalAdd,
				'TotalCount':T_Count
			}
	if request.flavour =='full':
		return render_to_response('html/Search_Category_Page.html',dic)
	else:
		return render_to_response('m_skins/m_html/earch_Category_Page.html',dic)
def search_subject_page(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	Mobile = request.flavour
	if request.GET['Page'] !="0":
		cur_page = int(request.GET['Page'])
	else:
		cur_page = 1
		Current = request.GET['Current']

	Course = request.GET['Course']
	
	PageInformation = request.session['SearchPageInformation']

	if Mobile == 'full':
		DBCount = Lecture.objects.filter(Q(CourseName__icontains=Course)).values("Code").distinct().distinct().count()
		SearchCount = DataCount(10,DBCount)
	else :
		DBCount = Lecture.objects.filter(Q(CourseName__icontains=Course)).values("Code").distinct().count()
		SearchCount = DataCount(5,DBCount)
	
	if Mobile == 'full':
		PageInformation = CurrentPageView(SearchCount,cur_page)
		PageInformation[1]=cur_page
	else:
		PageInformation = MobileCurrentPageView(SearchCount,cur_page)
		PageInformation[1]=cur_page
	
	LectureData = [[]]
	TotalAdd=[]
	if Mobile == 'full':
		temp=Lecture.objects.filter(Q(CourseName__icontains=Course)).values("Code").distinct()[(PageInformation[1]-1)*10:(PageInformation[1]-1)*10+10]
	else:
		temp=Lecture.objects.filter(Q(CourseName__icontains=Course)).values("Code").distinct()[(PageInformation[1]-1)*5:(PageInformation[1]-1)*5+5]
	LecList=[]
	for lec in temp:
				A=Lecture.objects.filter(Code=lec['Code'])
				LectureData[0].append(A[0])
				
				total=0	
				
				try:
						Eval=Total_Evaluation.objects.filter(Course__Code=lec['Code'])
						for Ev in Eval:
							total += Ev.Total_Count  
				except:
					continue
				TotalAdd.append(total)

	L_Data=PageView(LectureData)
	
	if Mobile == 'full':
		T_Count=PageTotalCount(SearchCount,PageInformation)
	else:
		T_Count=MobilePageTotalCount(SearchCount,PageInformation,3)

	request.session['SearchPageInformation'] = PageInformation
	
	dic = {
				'user':request.user,
				'BestBoard':BestBoardView(),
				'Search' : L_Data,
				'PageInformation' : PageInformation,
				'TotalCount' : T_Count,
				'TotalAdd':TotalAdd,
				'temp':Lecture.objects.filter(Q(CourseName__icontains=Course)).values("Code").distinct()[(PageInformation[1]-1)*5:(PageInformation[1]-1)*5+5]
			}
	if request.flavour =='full':
			return render_to_response('html/SearchPage.html',dic)
	else:
			return render_to_response('m_skins/m_html/SearchPage.html',dic )

def GroupTotalCountRenew(request):
	if not request.user.username=='admin_seal':
		return HttpResponseRedirect('/')

	Total_Eval_List = Total_Evaluation.objects.all()
	Group_Total_Evaluation.objects.all().delete()
	for Total_Eval in Total_Eval_List:
		try:
			Group_Total = Group_Total_Evaluation.objects.get(CourseName = Total_Eval.Course.CourseName,Code = Total_Eval.Course.Code)
		except:
			Group_Total=None
		if Group_Total is None:
			Group_Total = Group_Total_Evaluation(CourseName = Total_Eval.Course.CourseName,
				Code = Total_Eval.Course.Code,GroupTotalCount=Total_Eval.Total_Count)
		else:
			Group_Total.GroupTotalCount +=Total_Eval.Total_Count
		Group_Total.save()
	return HttpResponseRedirect("/")

def renewDB(request):
	#이건 되도록 쓰지마세요
	if not request.user.username=='admin_seal':
		return HttpResponseRedirect('/')

	Course_EvalList = Course_Evaluation.objects.all()
	for Course_Eval in Course_EvalList:
		if Course_Eval.What_Answer == 1:
			Course_Eval.What_Answer =1000
		elif Course_Eval.What_Answer == 2:
			Course_Eval.What_Answer = 100
		elif Course_Eval.What_Answer ==3 :
			Course_Eval.What_Answer=10
		elif Course_Eval.What_Answer ==4 :
			Course_Eval.What_Answer =5
		if Course_Eval.Course_Answer == 1:
			Course_Eval.Course_Answer =100
		elif Course_Eval.Course_Answer == 2:
			Course_Eval.Course_Answer = 10
		elif Course_Eval.Course_Answer ==3 :
			Course_Eval.Course_Answer=5
		Course_Eval.save()
	Lecture_List = Lecture.objects.all().order_by("Semester")
	Total_Eval_List = Total_Evaluation.objects.all().delete()
	for lec in Lecture_List:
		pro = lec.Professor.split(" 외")!=None and lec.Professor.split(" 외")[0] or lec.Professor
		pro = pro.split("외")!=None and pro.split("외")[0] or pro

		lec.save()
		temp_total= Total_Evaluation.objects.filter(Course__Code=lec.Code,Course__CourseName=lec.CourseName,Course__Professor__contains=pro).count()
		if(temp_total ==0):
			Total_Evaluation(Course=lec).save()

	'''
	for Course_Eval in Course_EvalList:
		Course_Professor = Course_Eval.Course.Professor.split("외")[0] !=None and Course_Eval.Course.Professor.split("외")[0] or Course_Eval.Course.Professor
		Course_Code = Course_Eval.Course.Code
		Course_CourseName = Course_Eval.Course.CourseName
		LectureObject=Lecture.objects.filter(Code=Course_Code, Professor__contains=Course_Professor, CourseName=Course_CourseName).order_by("Semester")[0]
		Course_Eval.Course = LectureObject
		Course_Eval.save()
	'''
	
	for Course_Eval in Course_EvalList:
		temp_pro=Course_Eval.Course.Professor.split(" 외")[0] != None and Course_Eval.Course.Professor.split(" 외")[0] or Course_Eval.Course.Professor
		Course_Professor = temp_pro.split("외")[0] != None and temp_pro.split("외")[0] or temp_pro
		
		Total_Eval = Total_Evaluation.objects.get(Course__Code=Course_Eval.Course.Code, Course__Professor__contains=Course_Professor,Course__CourseName=Course_Eval.Course.CourseName)
		
	
		Total_Professor = Total_Eval.Course.Professor.split("외")[0] != None and Total_Eval.Course.Professor.split("외")[0] or Total_Eval.Course.Professor
		if Total_Eval.Course.CourseName ==Course_Eval.Course.CourseName and Total_Eval.Course.Code ==Course_Eval.Course.Code and Total_Professor == Course_Professor:
			Total_Eval.Total_Homework+=Course_Eval.Homework
			Total_Eval.Total_Level_Difficulty+=Course_Eval.Level_Difficulty
			Total_Eval.Total_Count += 1
			Total_Eval.Total_StarPoint+=Course_Eval.StarPoint
			if Course_Eval.Check ==True:
				Total_Eval.Total_Recommend +=1

			if Course_Eval.What_Answer-1000 >=0:
				Total_Eval.Total_Long_Answer +=1				
			elif Course_Eval.What_Answer%1000-100 >=0:
				Total_Eval.Total_Short_Answer+=1
			elif Course_Eval.What_Answer%100-10 >=0:
				Total_Eval.Total_Mix+=1
			elif Course_Eval.What_Answer%10-1 >=0:
				Total_Eval.Total_Unknown_Answer+=1
			
			if Course_Eval.Course_Answer%1000-100>=0:
				Total_Eval.Total_Book_Like+=1
			elif Course_Eval.Course_Answer%100-10 >=0:
				Total_Eval.Total_Ppt_Like+=1
			elif Course_Eval.Course_Answer%10-1>=0:
				Total_Eval.Total_Practice_Like+=1
		
		Total_Eval.save()
		Course_Eval.Total_Course_id=Total_Eval.id
		Course_Eval.save() 



	
	return HttpResponseRedirect("/")