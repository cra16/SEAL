# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from login.models import *
from mycourse.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q
from functionhelper.views import *
@csrf_exempt
def Recommend(request, offset): #강의 추천 스크롤 기능
			
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	try:
			offset = int(offset)
	except:
			raise Http404()

	UserProfile=Profile.objects.get(User = request.user)
	LectureData= Lecture.objects.get(id=offset)
	#try:
		
		#RecommendData=Recommend_Course.objects.get(Course = Course_Evaluation.objects.get(Course =LectureData, CreatedID = UserProfile),CreatedID =UserProfile) 
		

		#return HttpResponseRedirect('/NotEmptyRecommend')
	#except:
	RecommendData=None
	SemesterData = Lecture.objects.filter(Code = LectureData.Code, CourseName=LectureData.CourseName, Professor=LectureData.Professor).order_by('-Semester')
	SemesterList=list()
	for semester in SemesterData:
		if semester.Semester not in SemesterList:
			SemesterList.append(semester.Semester)



	if RecommendData != None:
		if request.flavour =='full':
			return HttpResponseRedirect('/NotEmptyRecommend')
		else:
			return  HttpResponseRedirect("/NotEmptyRecommend")
	else:
		CourseBoard = Lecture.objects.get(id=offset) #DB 고유 ID로 접근해서 검색		
		request.session['Recommend_ID'] = offset #offset 미리 저장
		dic = {'user':request.user,
              'BestBoard':BestBoardView(),
               'CourseBoard':CourseBoard,
               'Recommend':RecommendData,
               'SemesterData':SemesterList
				}
		if request.flavour =='full':
			return render_to_response('html/recommend.html',dic)
		else:
			return render_to_response("m_skins/m_html/recommend.html",dic)
def Recommend_NotEmpty(request):
	if request.flavour =='full':
			return render_to_response('html/Not_Empty_Recommend.html')
	else:
			return render_to_response("m_skins/m_html/Not_Empty_Recommend.html")
@csrf_exempt
def Recommend_Write(request): #추천 강의 DB입력

	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	ID=request.session['Recommend_ID']
	UserProfile=Profile.objects.get(User = request.user)
	

	#form 가져오기
	if request.method =="POST":
		CourseName=request.POST['HCourseName']
		CourseCode=request.POST['HCourseCode']
		Semester=request.POST['HSemester']
		Professor=request.POST['HCourseProfessor']


		try:
			RecommendData=Course_Evaluation.objects.get(Course =Lecture.objects.filter(Semester=Semester ,Code=CourseCode, CourseName = CourseName, Professor=Professor)[0],CreatedID = UserProfile)
			if(RecommendData != None):
				return HttpResponseRedirect('/NotEmptyRecommend')
		except:
			RecommendData=None
		
		try:
			new_Speedy= (request.POST['sl1'] !="" and int(request.POST['sl1']) or 5)
			new_Reliance= (request.POST['sl2'] !="" and int(request.POST['sl2']) or 5)
			#new_Helper= (request.POST['sl3'] !="" and int(request.POST['sl3']) or 5)
			new_Question=(request.POST['sl3'] !="" and int(request.POST['sl3']) or 5)
			#new_Exam=(request.POST['sl4'] !="" and int(request.POST['sl4']) or 5)
#			new_Homework=int(request.POST['sl6'])
			new_CourseComment=request.POST['CourseComment']
			new_Check = request.POST['ButtonCheck'] =="True" and True or False
			new_Satisfy = float(request.POST['StarValue'])
			new_Answer_list = request.POST.getlist('mytext[]')
			new_Who = request.POST['who']
			new_Url = request.POST['url']
			new_paper_value= int(request.POST['paper_value'])
		except:
			CourseName=request.POST['HCourseName']
			CourseCode=request.POST['HCourseCode']
			Semester=request.POST['HSemester']
		
			new_CourseComment=request.POST['CourseComment']
			new_Speedy=5
			new_Reliance=5
			#new_Helper=5
			new_Question=5
			new_Exam=5
			new_Check = request.POST['ButtonCheck'] == "True" and True or False
			new_Satisfy = float(request.POST['StarValue'])
			new_Answer_list = request.POST.getlist('Answer[]')
			new_paper_value= int(request.POST['paper_value'])
		# 추천 여부에 따라 1 or 0
		is_recommend = ( request.POST['ButtonCheck'] == "True" )
		if is_recommend:
			recommend_cnt = 1
		else:
			recommend_cnt = 0
			
#			new_Homework=5
		
		new_Course=Lecture.objects.filter(Semester=Semester ,Code=CourseCode, CourseName = CourseName, Professor=Professor)[0]
		new_CreatedID = Profile.objects.get(User= request.user)
		for new_Answer in new_Answer_list:#서술형 답변
			temp=Description_Answer(CreatedID=new_CreatedID,Answer = new_Answer,Course=new_Course)
		
		new_Eval = Course_Evaluation(Course = new_Course, CreatedID = new_CreatedID, 
			Speedy = new_Speedy, Reliance = new_Reliance, Question = new_Question,
			CourseComment=new_CourseComment,Check =new_Check,StarPoint=new_Satisfy,What_Answer=new_paper_value,Who_Answer=new_Who,Url_Answer=new_Url)
		new_Recommend = Recommend_Course(Course = new_Eval, CreatedID = new_CreatedID).objects.create()

		L_Eval = Lecture.objects.get(id=request.session['Recommend_ID'])#해당 강의 정보를 일단 DB에서 불러옴

		try:
			T_Eval=Total_Evaluation.objects.get(Course=L_Eval)#위에서 부른 강의 정보를 바탕으로 해당 강의의 총 평가 Data 불러옴
		except:
			T_Eval =None 

		UserData = Profile.objects.get(User = request.user)
		UserData.RecommendCount = Course_Evaluation.objects.filter(CreatedID=new_CreatedID).count()
		UserData.save()
		if T_Eval is None: #데이터 없을시 Table 생성
			Total_Eval = Total_Evaluation(
				Course = new_Course,Total_Speedy = new_Speedy,
				Total_Reliance = new_Reliance, Total_Question = new_Question,  Total_Count = 1,
				Total_StarPoint = new_Satisfy, Total_Recommend = recommend_cnt, Total_Mix=0, Total_Short_Answer=0, Total_Long_Answer=0
			)
			if new_paper_value==1:
				Total_Eval.Total_Long_Answer+=1
			elif new_paper_value ==2:
				Total_Eval.Total_Short_Answer+=1
			elif new_paper_value ==3:
				Total_Eval.Total_Mix+=1

			Total_Eval.save()
		else: #update
			T_Eval.Total_Speedy += int(new_Speedy)
			T_Eval.Total_Reliance += int(new_Reliance)
			#T_Eval.Total_Helper += int(new_Helper)
			T_Eval.Total_Question += int(new_Question)
			#T_Eval.Total_Exam += int(new_Question)
			#T_Eval.Total_Homework += int(new_Homework)
			T_Eval.Total_StarPoint += float(new_Satisfy)
			T_Eval.Total_Count += 1
			T_Eval.Total_Recommend += recommend_cnt
			if new_paper_value==1:
				T_Eval.Total_Long_Answer+=1
			elif new_paper_value ==2:
				T_Eval.Total_Short_Answer+=1
			elif new_paper_value ==3:
				T_Eval.Total_Mix+=1
			
			T_Eval.save()
	
		URL = "/CourseProfessor/"+str(new_Course.id)
		return HttpResponseRedirect(URL)

	else:
		return HttpResponseRedirect("/")
@csrf_exempt
def Like(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")


	if request.method=="POST":
		page = int(request.POST['Page'])
		LectureID= page
		LectureID = int(LectureID)
		
	
	try :
		UserData=Profile.objects.get(User=request.user)
	except:
		pass

	try:
		LikeData=Like_Course.objects.get(Course = Lecture.objects.get(id=LectureID),CreatedID = UserData)
	except:
		LikeData=None

	if LikeData != None:
		if request.flavour =='full':
			raise Exception
		else:
			raise Exception
	else:
		CourseLecture = Lecture.objects.get(id = LectureID)
		new_Like=Like_Course(Course = CourseLecture, CreatedID = UserData)
		new_Like.save()
		UserData.LikeCount= Like_Course.objects.filter(CreatedID=UserData).count()
		UserData.save()
		

		
		URL = "/CourseProfessor/"+str(LectureID)
		return HttpResponseRedirect(URL)
		