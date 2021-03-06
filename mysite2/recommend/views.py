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
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

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
	try:
		
		RecommendData=Recommend_Course.objects.filter(Course__Course__CourseName=LectureData.CourseName,Course__Course__Code = LectureData.Code, Course__Course__Professor__contains=renew_professor,CreatedID =UserProfile).count()
		
	except:
			RecommendData=None
	


	if RecommendData >0:
		if request.flavour =='full':
			return HttpResponseRedirect('/NotEmptyRecommend')
		else:
			return  HttpResponseRedirect("/NotEmptyRecommend")

	else:
		renew_professor= LectureData.Professor.split("외")[0] != None and LectureData.Professor.split("외")[0] or LectureData.Professor
		SemesterData = Lecture.objects.filter(Code = LectureData.Code, CourseName=LectureData.CourseName, Professor__contains=renew_professor).order_by('-Semester')
		SemesterList=list()
		for semester in SemesterData:
			if semester.Semester not in SemesterList:
				SemesterList.append(semester.Semester)

		CourseBoard = Lecture.objects.get(id=offset) #DB 고유 ID로 접근해서 검색	
		CourseBoard.Professor = renew_professor	
		request.session['Recommend_ID'] = offset #offset 미리 저장
		dic = {'user':request.user,
              'BestBoard':BestBoardView(),
               'CourseBoard':CourseBoard,
               'Recommend':RecommendData,
               'SemesterData':SemesterList,
               'TotalCountBoard':TotalEvalutionCount(),
               
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
		new_CourseComment=request.POST['CourseComment']
		new_Check = request.POST['ButtonCheck'] =="True" and True or False
		new_Satisfy = float(request.POST['StarValue'])
		new_Answer_list = request.POST.getlist('mytext[]')
		new_Who = request.POST['who']
		new_paper_value= request.POST.getlist('paper_value[]')
		new_course_value= request.POST.getlist('course_value[]')
		total_paper_value=0
		total_course_value=0
		renew_professor= Professor.split("외")[0] != None and Professor.split("외")[0] or Professor

		try:
			RecommendData=Recommend_Course.objects.filter(Course__CourseName=CourseName,Course__Code = CourseCode, Course__Professor__contains=renew_professor,CreatedID =UserProfile).count() 

			if(RecommendData > 0):
				return HttpResponseRedirect('/NotEmptyRecommend')
		except:
			RecommendData=None
		
		
		new_Homework= (request.POST['sl2'] !="" and int(request.POST['sl2']) or 5)
		
		new_Level_Difficulty=(request.POST['sl3'] !="" and int(request.POST['sl3']) or 5)
		
#			
		
		
		
		
		is_recommend = ( request.POST['ButtonCheck'] == "True" )
		if is_recommend:
			recommend_cnt = 1
		else:
			recommend_cnt = 0
		
		
		new_Course=Lecture.objects.filter(Semester=Semester ,Code=CourseCode, CourseName = CourseName, Professor__contains=renew_professor).order_by("Semester")[0]
		new_CreatedID = Profile.objects.get(User= request.user)
		CTable = CountTable.objects.all()[0]

		for new_Answer in new_Answer_list:#서술형 답변
			if new_Answer =="":
				continue
			temp=Description_Answer(CreatedID=new_CreatedID,Answer = new_Answer,Course=new_Course)
			temp.save()
	
		

		try:
			T_Eval=Total_Evaluation.objects.filter(Course__Code=CourseCode, Course__CourseName = CourseName, Course__Professor__contains=renew_professor)[0]
			#위에서 부른 강의 정보를 바탕으로 해당 강의의 총 평가 Data 불러옴
		except:
			T_Eval =None 

		UserData = Profile.objects.get(User = request.user)
		UserData.RecommendCount = Course_Evaluation.objects.filter(CreatedID=new_CreatedID).count()
		UserData.save()
		new_Course=Lecture.objects.filter(Semester=Semester,Code=CourseCode, CourseName = CourseName, Professor__contains=renew_professor).order_by("Semester")[0]
		if T_Eval is None: #데이터 없을시 Table 생성
			T_Eval = Total_Evaluation(
				Course = new_Course,
				Total_Homework = new_Homework, Total_Level_Difficulty = new_Level_Difficulty,  Total_Count = 1,
				Total_StarPoint = new_Satisfy, Total_Recommend = recommend_cnt, Total_Mix=0, Total_Short_Answer=0, Total_Long_Answer=0,Total_Book_Like=0, Total_Ppt_Like=0, Total_Practice_Like=0
			)
			for new_paper_item in new_paper_value:
				new_paper=int(new_paper_item)
				if new_paper==1:
					T_Eval.Total_Long_Answer+=1
				elif new_paper ==2:
					T_Eval.Total_Short_Answer+=1
				elif new_paper ==3:
					T_Eval.Total_Mix+=1
				elif new_paper ==4:
					T_Eval.Total_Unknown_Answer+=1
			for new_course_item in new_course_value:
				new_course=int(new_course_item)
				if new_course==1:
					T_Eval.Total_Book_Like+=1
				elif new_course==2:
					T_Eval.Total_Ppt_Like+=1
				elif new_course==3:
					T_Eval.Total_Practice_Like+=1
			T_Eval.save()
		else: #update
			#T_Eval.Total_Helper += int(new_Helper)
			T_Eval.Total_Homework += int(new_Homework)
			#T_Eval.Total_Exam += int(new_Question)
			T_Eval.Total_Level_Difficulty += int(new_Level_Difficulty)
			T_Eval.Total_StarPoint += float(new_Satisfy)
			T_Eval.Total_Count += 1
			T_Eval.Total_Recommend += recommend_cnt
			for new_paper_item in new_paper_value:
				new_paper=int(new_paper_item)
				if new_paper_item==1000:
					T_Eval.Total_Long_Answer+=1
				elif new_paper_item ==100:
					T_Eval.Total_Short_Answer+=1
				elif new_paper_item ==10:
					T_Eval.Total_Mix+=1
				elif new_paper_item ==1:
					T_Eval.Total_Unknown_Answer+=1
				total_paper_value+=new_paper
			for new_course_item in new_course_value:
				new_course=int(new_course_item)			
				if new_course_item==100:
					T_Eval.Total_Book_Like+=1
				elif new_course_item==10:
					T_Eval.Total_Ppt_Like+=1
				elif new_course_item==1:
					T_Eval.Total_Practice_Like+=1
				total_course_value += new_course
			T_Eval.save()
		try:
			Group_Total = Group_Total_Evaluation.objects.get(CourseName=new_Course.Coursename,Code = new_Course.Code)
		except:
			Group_Total=None
		if Group_Total is None:
			Group_Total = Group_Total_Evaluation(CourseName = new_Course.CourseName, Code = new_Course.Code, GroupTotalCount=1)	
		else:
			Group_Total.GroupTotalCount+=1
			Group_Total.save()	

		new_Eval = Course_Evaluation(Course = new_Course, CreatedID = new_CreatedID, Homework = new_Homework, Level_Difficulty = new_Level_Difficulty,
			CourseComment=new_CourseComment,Check =new_Check,StarPoint=new_Satisfy,What_Answer=total_paper_value,Who_Answer=new_Who,Course_Answer=total_course_value)
		
		CTable.TotalCount+=1

		Code = new_Course.Code[0:3]
		if Code == "ENG" or Code == "GEK" or Code == "GCS" or Code == "PCO" or Code == "ISL" or Code == "PST":
			CTable.GLS+=1 
		elif Code =="ISE":
			CTable.ISL += 1
		elif Code =="GMP" or Code == "MEC":
			CTable.ME += 1
		elif Code =="LAW" or Code == "UIL":
			CTable.SOF +=1
		elif Code =="CCC":
			CTable.SOCAS += 1
		elif Code =="CUE":
			CTable.SESE +=1
		elif Code =="HMM":
			CTable.MCE += 1
		elif Code =="IID":
			CTable.CCD +=1
		elif Code =="BFT":
			CTable.LS += 1
		elif Code =="ECE" or Code =="ITP":
			CTable.CSEE+=1
		elif Code =="CSW":
			CTable.CPSW +=1
		elif Code =="SIE":
			CTable.ICT +=1
		elif Code =="SIE":
			CTable.SCEE+=1
		CTable.save()

		new_Eval.Total_Course_id=T_Eval.id
		new_Eval.save()
		UserData.RecommendCount+=1
		UserData.save()
		new_Recommend = Recommend_Course(Course = new_Eval, CreatedID = new_CreatedID)
		new_Recommend.save()
		
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
		