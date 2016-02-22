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
def CourseUpdate(request):
	if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")
	if request.method == "POST":
		LectureData=Lecture.objects.get(id=1)
		UserData = Profile.objects.get(User = request.user)
		UpdateCourseEval=Course_Evaluation.objects.get(Course=LectureData, CreatedID=UserData)
		UpdateTotalEval = Total_Evaluation.objects.get(Course=LectureData)
		
		UpdateTotalEval.Total_Speedy -= UpdateCourseEval.Speedy
		UpdateTotalEval.Total_Homework -= UpdateCourseEval.Homework
		UpdateTotalEval.Total_Level_Difficulty -= UpdateCourseEval.Level_Difficulty
		UpdateTotalEval.Total_StarPoint -= UpdateCourseEval.StarPoint

		UpdateCourseEval.Speedy = request.POST['Speedy']
		UpdateCourseEval.Homework = request.POST['Homework']
		UpdateCourseEval.Level_Difficulty = request.POST['Level_Difficulty']
		UpdateCourseEval.StarPoint =request.POST['StarPoint']

		UpdeateTotalEval.update()
		UpdateCourseEval.update()

# Create your views here.
