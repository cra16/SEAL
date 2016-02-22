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
			PageFirst=10*(int(Page)-1)
			PageLast =10*(int(Page)-1)+10
	except:
		raise Http404()
	
	MyProfile = Profile.objects.get(User=request.user)
	

	RecommendPage=[]
	LikePage=[]
	
	Recommend = Recommend_Course.objects.filter(CreatedID = MyProfile)[PageFirst:PageLast]			
	
	for Board in Recommend:
			RecommendData = Total_Evaluation.objects.get(Course__CourseName=Board.Course.Course.CourseName,Course__Professor = Board.Course.Course.Professor, Course__Code = Board.Course.Course.Code)
			RecommendData.Total_Speedy=RecommendData.Total_Speedy/RecommendData.Total_Count
			RecommendData.Total_Homework =RecommendData.Total_Homework/RecommendData.Total_Count
			RecommendData.Total_Level_Difficulty=RecommendData.Total_Level_Difficulty/RecommendData.Total_Count
			RecommendData.Total_StarPoint = RecommendData.Total_StarPoint/RecommendData.Total_Count 
			RecommendPage.append(RecommendData)	
			
	Like=Like_Course.objects.filter(CreatedID = MyProfile)[PageFirst:PageLast]

	for Board2 in Like:
			try :
					LikeData=Total_Evaluation.objects.get(Course=Board2.Course)
			except:
					LikeData = Total_Evaluation(Course =Board2.Course)
					LikeData.Total_Speedy=5
					LikeData.Total_Homework =5
					LikeData.Total_Level_Difficulty=5
				
			if LikeData.Total_Count==0:
				LikePage.append(LikeData)
				break
	
			LikeData.Total_Speedy=LikeData.Total_Speedy/LikeData.Total_Count
			LikeData.Total_Homework =LikeData.Total_Homework/LikeData.Total_Count
			LikeData.Total_Level_Difficulty=LikeData.Total_Level_Difficulty/LikeData.Total_Count
			LikeData.Total_StarPoint = LikeData.Total_StarPoint/LikeData.Total_Count
			LikePage.append(LikeData)
	Count = [[],[]]
	DBCount=Course_Evaluation.objects.filter(CreatedID = MyProfile).count()
	Count[0] = DataCount(10,DBCount)
	DBCount=Like_Course.objects.filter(CreatedID = MyProfile).count()
	Count[1]=DataCount(10,DBCount)
	
	PageInformation=list()
	TotalCount=list()
	if Mobile == "full":

		for i in range(0,2):
			PageInformation.append(CurrentPageView(Count[i],Page))									
			TotalCount.append(PageTotalCount(Count[i],PageInformation[i]))
	else:
		for i in range(0,2):
			PageInformation.append(MobileCurrentPageView(Count[i],Page))									
			TotalCount.append(MobilePageTotalCount(Count[i],PageInformation[i],3))

	MyCoursePageData=dict()
	MyCoursePageData={'user':request.user, 
						'BestBoard':BestBoardView(),
						'RecommendPage':RecommendPage,
						'LikePage':LikePage,
						'PageInformation' : PageInformation,
						'TotalCount':TotalCount,
						'Page':Page,
						'Recommend':Recommend
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


@csrf_exempt
def CourseDelete(request):
	Mobile = request.flavour
	if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")

	if request.method == "POST":
		Code = request.POST['Code']
		Professor = request.POST['Professor']
		Period = request.POST['Period']
		Semster= request.POST['Semester']
		CourseName = request.POST['CourseName']
		Page = request.POST['CurrentPage']
		Page= int(Page)
		PageFirst=10*(int(Page)-1)
		PageLast =10*(int(Page)-1)+10

		LectureData=Lecture.objects.filter(Code = Code, CourseName=CourseName, Professor = Professor, Semester =Semster)[0]
		UserData = Profile.objects.get(User = request.user)
		DeleteData=Course_Evaluation.objects.filter(Course__CourseName=CourseName, Course__Code = Code, Course__Professor=Professor, CreatedID=UserData)[0]
		
		Delete_Dis = Description_Answer.objects.filter(Course__CourseName=CourseName, Course__Code = Code, Course__Professor=Professor,Course__Semester =Semster,CreatedID=UserData)
		UpdateData=Total_Evaluation.objects.get(Course=LectureData)

		
		
			
		UpdateData.Total_Speedy -= DeleteData.Speedy
		UpdateData.Total_Homework -= DeleteData.Homework
		UpdateData.Total_Level_Difficulty -= DeleteData.Level_Difficulty
		UpdateData.Total_StarPoint -= DeleteData.StarPoint

		
		UpdateData.Total_Count -=1
		if UpdateData.Total_Count ==0:
			UpdateData.delete()
			Delete_Dis.delete()
			DeleteData.delete()
		else:
			UpdateData.save()
			Delete_Dis.delete()
			DeleteData.delete()
		Recommend = Recommend_Course.objects.filter(CreatedID = UserData)[PageFirst:PageLast]			
		RecommendPage =[]
		for Board in Recommend:
			RecommendData = Total_Evaluation.objects.get(Course__CourseName=Board.Course.Course.CourseName,Course__Professor = Board.Course.Course.Professor, Course__Code = Board.Course.Course.Code)
			RecommendData.Total_Speedy=RecommendData.Total_Speedy/RecommendData.Total_Count
			RecommendData.Total_Homework =RecommendData.Total_Homework/RecommendData.Total_Count
			RecommendData.Total_Level_Difficulty=RecommendData.Total_Level_Difficulty/RecommendData.Total_Count
			RecommendData.Total_StarPoint = RecommendData.Total_StarPoint/RecommendData.Total_Count 
			RecommendData.Total_Recommend = RecommendData.Total_Recommend/RecommendData.Total_Count
			RecommendPage.append(RecommendData)
		Count = [[],[]]
		DBCount=Course_Evaluation.objects.filter(CreatedID = UserData).count()
		Count[0] = DataCount(10,DBCount)
		DBCount=Like_Course.objects.filter(CreatedID = UserData).count()
		Count[1]=DataCount(10,DBCount)
		PageInformation=list()
		TotalCount=list()
		if Mobile == "full":

			for i in range(0,2):
				PageInformation.append(CurrentPageView(Count[i],Page))									
				TotalCount.append(PageTotalCount(Count[i],PageInformation[i]))
		else:
			for i in range(0,2):
				PageInformation.append(MobileCurrentPageView(Count[i],Page))									
				TotalCount.append(MobilePageTotalCount(Count[i],PageInformation[i],3))
	
		UserData = Profile.objects.get(User = request.user)
		UserData.RecommendCount = Course_Evaluation.objects.filter(CreatedID=UserData).count()
		UserData.save()
		Data={

		'User':UserData,
		"RecommendPage":RecommendPage,
		'PageInformation' : PageInformation,
		'TotalCount':TotalCount,
		'Page':Page
		}

		return render_to_response('html/RecommendPage.html',Data)
@csrf_exempt
def UpdateRedirect(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	if request.method =="POST":
		CourseName=request.POST['CourseName']
		CourseCode=request.POST['Code']
		Semester=request.POST['Semester']
		Professor=request.POST['Professor']
	UserProfile=Profile.objects.get(User = request.user)
	LectureData= Lecture.objects.filter(Code = CourseCode, CourseName=CourseName, Professor=Professor,Semester=Semester)[0]
	LectureData2= Lecture.objects.filter(Code = CourseCode, CourseName=CourseName, Professor=Professor)
	SemesterData = Lecture.objects.filter(Code = CourseCode, CourseName=CourseName, Professor=Professor).order_by('-Semester')
	SemesterList=list()
	for semester in SemesterData:
		if semester.Semester not in SemesterList:
			SemesterList.append(semester.Semester)

	CourseBoard = Course_Evaluation.objects.get(Course=LectureData) #DB 고유 ID로 접근해서 검색		
	
	totalcount=0
	MyCourseBoard = None
	
	Description=Description_Answer.objects.filter(Course=LectureData,CreatedID=UserProfile)
			
	dic = {'user':request.user,
          'BestBoard':BestBoardView(),
           'CourseBoard':CourseBoard,
    	   'Description':Description,
           'SemesterData':SemesterList
			}
	if request.flavour =='full':
		return render_to_response('html/update.html',dic)
	else:
		return render_to_response("m_skins/m_html/update.html",dic)
@csrf_exempt
def CourseUpdate(request):
	if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")
	if request.method == "POST":
		new_Speedy= (request.POST['sl1'] !="" and int(request.POST['sl1']) or 5)
		new_Homework= (request.POST['sl2'] !="" and int(request.POST['sl2']) or 5)
		
		new_Level_Difficulty=(request.POST['sl3'] !="" and int(request.POST['sl3']) or 5)
		
#			
		new_CourseComment=request.POST['CourseComment']
		new_Check = request.POST['ButtonCheck'] =="True" and True or False
		new_Satisfy = float(request.POST['StarValue'])
		new_Answer_list = request.POST.getlist('mytext[]')
		new_Who = request.POST['who']
		new_Url = request.POST['url']
		new_paper_value= int(request.POST['paper_value'])
		CourseName=request.POST['HCourseName']
		Code=request.POST['HCourseCode']
		Semester=request.POST['HSemester']
		Professor=request.POST['HCourseProfessor']

		LectureData=Lecture.objects.filter(Code = Code, CourseName=CourseName, Professor = Professor, Semester =Semester)[0]
		UserData = Profile.objects.get(User = request.user)
		UpdateCourseEval=Course_Evaluation.objects.get(Course__CourseName=CourseName, Course__Code = Code, Course__Professor=Professor,Course__Semester =Semester, CreatedID=UserData)
		UpdateTotalEval = Total_Evaluation.objects.get(Course=LectureData)
		Update_Dis = Description_Answer.objects.filter(Course__CourseName=CourseName, Course__Code = Code, Course__Professor=Professor,Course__Semester =Semester,CreatedID=UserData)

		UpdateTotalEval.Total_Speedy -= UpdateCourseEval.Speedy
		UpdateTotalEval.Total_Homework -= UpdateCourseEval.Homework
		UpdateTotalEval.Total_Level_Difficulty -= UpdateCourseEval.Level_Difficulty
		UpdateTotalEval.Total_StarPoint -= UpdateCourseEval.StarPoint
		if UpdateCourseEval.What_Answer == 1:
			UpdateTotalEval.Total_Mix -= 1
		elif UpdateCourseEval.What_Answer ==2:
			UpdateTotalEval.Total_Short_Answer-=1
		elif UpdateCourseEval.What_Answer ==3:
			UpdateTotalEval.Total_Long_Answer -=1
		elif UpdateCourseEval.What_Answer ==4:
			UpdateTotalEval.Total_Unknown_Answer -=1

		UpdateCourseEval.Speedy = new_Speedy
		UpdateCourseEval.Homework =new_Homework
		UpdateCourseEval.Level_Difficulty = new_Level_Difficulty
		UpdateCourseEval.StarPoint =new_Satisfy
		UpdateCourseEval.Check = new_Check
		UpdateCourseEval.StarPoint = new_Satisfy
		UpdateCourseEval.What_Answer = new_paper_value
		UpdateCourseEval.Who_Answer = new_Who
		UpdateCourseEval.Url_Answer = new_Url
		UpdateCourseEval.CourseComment = new_CourseComment
		
		if UpdateCourseEval.What_Answer == 1:
			UpdateTotalEval.Total_Mix += 1
		elif UpdateCourseEval.What_Answer ==2:
			UpdateTotalEval.Total_Short_Answer +=1
		elif UpdateCourseEval.What_Answer ==3:
			UpdateTotalEval.Total_Long_Answer +=1
		elif UpdateCourseEval.What_Answer ==4:
			UpdateTotalEval.Total_Unknown_Answer +=1

		UpdateTotalEval.Total_Speedy += UpdateCourseEval.Speedy
		UpdateTotalEval.Total_Homework += UpdateCourseEval.Homework
		UpdateTotalEval.Total_Level_Difficulty += UpdateCourseEval.Level_Difficulty
		UpdateTotalEval.Total_StarPoint += UpdateCourseEval.StarPoint

		Update_Dis.delete()
		for new_Answer in new_Answer_list:#서술형 답변
			if new_Answer =="":
				continue
			temp=Description_Answer(CreatedID=UserData,Answer = new_Answer,Course=LectureData)
			temp.save()
		
		UpdateTotalEval.save()
		UpdateCourseEval.save()
		return HttpResponseRedirect("/MyCourse")

# Create your views here.
