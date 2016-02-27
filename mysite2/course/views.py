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

from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q
from functionhelper.views import *
from itertools import chain, islice
'''
def Course(request, offset): #해당 수업에 대한 강의 추천 모두 불러옴

		if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")
		Mobile = request.flavour
		#현재 접속한 아이디 정보 받아옴
		try:
			UserData = Profile.objects.get(User = request.user)
		except :
			UserData =None


		#강의 추천 1번이상 안했을 시 정보 안 보여줌
		if UserData.RecommendCount <1:
			if UserData.User.username[1:3]=="16":
				pass
			elif request.flavour =='full':
				return render_to_response("html/Course_error.html",dic)
			else:
				return render_to_response("m_skins/m_html/Course_error.html",dic)

		try:
			offset = int(offset)
		except:
			raise Http404()
		#보려는 강의 정보 
		LectureInformation=Lecture.objects.get(id=offset)

		CourseBoard=TotalCourse(offset)#해당 강의 전체 추천한 Data DB 불러오기
		
		
		#자신이 햇을 경우 자신이 평가한 정보를 보여주는 기능
		
		
		#한 페이지에 뿌리는 기능
		PageFirst = 3*(1-1)
		PageLast = 3*(1-1)+3
		MergeCourse=None
		count=0
		totalcount=0
		Description=[]
		t= Lecture.objects.filter(CourseName = LectureInformation.CourseName, Professor=LectureInformation.Professor,Code =LectureInformation.Code)
		
		MyCourseBoard = None
		for TempData in t:
			try:
				Description.append(Description_Answer.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code,CreatedID=UserData))
			except:
				pass
			if MyCourseBoard == None:
				try:
					MyCourseBoard = Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code, CreatedID = UserData)
				except:
					MyCourseBoard = None
			
			if count==0:
				OtherCourse=Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code).order_by('-id')

				totalcount += OtherCourse.count()
			elif count>=1:
				TempCourse= Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code).order_by('-id')
				totalcount += TempCourse.count()
				MergeCourse=chain(TempCourse,OtherCourse)
				OtherCourse = MergeCourse
			count+=1
		OtherCourse=islice(OtherCourse,PageFirst,PageLast)
		OtherCourseBoard = []

		#접속한 아이디와 중복되는 경우 제거
		for Board in OtherCourse:
			if Board.CreatedID == UserData:
					pass
			else:
				OtherCourseBoard.append(Board)

		
		#pageNation과 관련된 기능
		#DBCount =Course_Evaluation.objects.filter(Course=LectureInformation).count()
		O_Count = DataCount(3,len(OtherCourseBoard))
		
				
		#전체 페이지가 11페이지 이상인 것을 기준으로 정의
		if Mobile == 'full':
				PageInformation=FirstPageView(O_Count)
				OtherCount=PageTotalCount(O_Count,PageInformation)
		else:
				PageInformation = MobileFirstPageView(O_Count)
				OtherCount=MobilePageTotalCount(O_Count,PageInformation,3)
		#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
		
		dic ={'user':request.user,
			'BestBoard':BestBoardView(),
			'CourseBoard':CourseBoard,
			'MyCourseBoard':MyCourseBoard,
			'OtherCourseBoard':OtherCourseBoard,
			'OtherCount':OtherCount,
			'PageInformation':PageInformation,
			'Answer_Dis' : Description,
			
			
			}
		if request.flavour =='full':
			return render_to_response('html/course.html',dic)
		else:
			return render_to_response("m_skins/m_html/course.html",dic)
'''
#페이지 넘겼을 때 작동되는 함수9
@csrf_exempt
def CoursePage(request, offset): #해당 수업에 대한 강의 추천 모두 불러옴(페이지 넘긴후)
	
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")
	Mobile = request.flavour
	try:
		offset = int(offset)
		if request.method=="POST":
			offset2 =int(request.POST["Page"]) 
		UserData=Profile.objects.get(User=request.user)
	except:
		raise Http404()
		
	#현 페이지에 대한 강의 정보
	LectureInformation = Lecture.objects.get(id = offset)

	CourseBoard = TotalCourse(offset)
	try:
			MergeCourse=None
			count=0
			TempData= Lecture.objects.filter(CourseName = LectureInformation.CourseName, Professor=LectureInformation.Professor,Code =LectureInformation.Code)[0]
			totalcount=0
			MyCourseBoard = None
			Description=[]
			Description.append(Description_Answer.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code,CreatedID=UserData))
			if count==0:
				MyCourse =  Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code = LectureInformation.Code, CreatedID = UserData)
				OtherCourse=Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code = LectureInformation.Code).order_by('-id')

				totalcount += OtherCourse.count()
				
			if count>=1:
				TempCourse= Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code).order_by('-id')
				totalcount += TempCourse.count()
				MergeCourse=chain(TempCourse,OtherCourse)
				OtherCourse = MergeCourse
				TempCourse = Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code, CreatedID = UserData)
				MergeCourse = chain(TempCourse,MyCourse)
				MyCourse = MergeCourse
			count+=1


			#DBCount = Course_Evaluation.objects.filter(Course = LectureInformation).count()
			
	except:
			DBCount = 0

	
	#이전페이지 다음페이지 기능 구현

	
	
	

	
	#해당 페이지에 출력할 데이터들 갯수 정하는 기능
	PageFirst = (offset2-1)*3
	PageLast = (offset2-1)*3+3
	
	try:
			pass
					
	except:
		OtherCourse=None
	OtherCourseBoard = []
	#접속한 아이디와 중복되는 경우 제거
	MyCourseBoard = []
	for Board in MyCourse:
		MyCourseBoard.append(Board)


	for Board in OtherCourse:
		if Board.CreatedID == UserData:
				pass
		else:
			OtherCourseBoard.append(Board)
	O_Count = DataCount(3,len(OtherCourseBoard))
	if Mobile =="full":
		PageInformation=CurrentPageView(O_Count,offset2)
		PageInformation[1]=offset2
		OtherCount=PageTotalCount(O_Count,PageInformation)
	else:
		PageInformation=MobileCurrentPageView(O_Count,offset2)
		PageInformation[1]=offset2
		OtherCount=MobilePageTotalCount(O_Count,PageInformation,3)
	OtherCourseBoard=OtherCourseBoard[PageFirst:PageLast]
	dic ={'user':request.user,
			'BestBoard':BestBoardView(),
			'CourseBoard':CourseBoard,
			'MyCourseBoard':MyCourseBoard,
			'OtherCourseBoard':OtherCourseBoard,
			'PageInformation':PageInformation,
			'OtherCount':OtherCount,
			'Count':totalcount		
			}
	if request.flavour =='full':
		return render_to_response('html/coursepage.html',dic)
	else:
		return render_to_response("m_skins/m_html/coursepage.html",dic )

# Create your views here.
def CourseProfessor(request, offset): #해당 수업에 대한 강의 추천 모두 불러옴
		if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")

		#현재 접속한 아이디 정보 받아옴
		Mobile=request.flavour
		try:
			UserData = Profile.objects.get(User = request.user)
		except :
			UserData =None
		
		#강의 추천 1번이상 안했을 시 정보 안 보여줌
		if UserData.RecommendCount <1:
			if UserData.User.username[1:3]=="16":
				pass
			elif request.flavour =='full':
				return render_to_response("html/Course_error.html")
			else:
				return render_to_response("m_skins/m_html/Course_error.html")

		
		try:
			offset = int(offset)
		except:
			raise Http404()
		#보려는 강의 정보 
		LectureInformation=Lecture.objects.get(id=offset)

		CourseBoard=TotalCourseProfessor(LectureInformation.CourseName,LectureInformation.Professor,LectureInformation.Code)#해당 강의 전체 추천한 Data DB 불러오기
		
		
		#자신이 햇을 경우 자신이 평가한 정보를 보여주는 기능
	
		#한 페이지에 뿌리는 기능
		PageFirst = 3*(1-1)
		PageLast = 3*(1-1)+3
		MergeCourse=None
		count=0
		MyCourseBoard = None
		Description=[]
		try:
			MergeCourse=None
			count=0
			TempData= Lecture.objects.filter(CourseName = LectureInformation.CourseName, Professor=LectureInformation.Professor,Code =LectureInformation.Code)[0]
			totalcount=0
			MyCourseBoard = None
	
			Description.append(Description_Answer.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code,CreatedID=UserData))
			
			if count==0:
				MyCourse =  Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code = LectureInformation.Code, CreatedID = UserData)
				OtherCourse=Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code = LectureInformation.Code).order_by('-id')

				totalcount += OtherCourse.count()
				
			if count>=1:
				TempCourse= Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code).order_by('-id')
				totalcount += TempCourse.count()
				MergeCourse=chain(TempCourse,OtherCourse)
				OtherCourse = MergeCourse
				TempCourse = Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code, CreatedID = UserData)
				MergeCourse = chain(TempCourse,MyCourse)
				MyCourse = MergeCourse
			count+=1

			#DBCount = Course_Evaluation.objects.filter(Course = LectureInformation).count()
			
		except:
			DBCount = 0

		
		OtherCourseBoard = []
		#접속한 아이디와 중복되는 경우 제거
		MyCourseBoard = []
		for Board in MyCourse:
			MyCourseBoard.append(Board)

		for Board in OtherCourse:
			if Board.CreatedID == UserData:
					pass
			else:
				OtherCourseBoard.append(Board)

		
		#pageNation과 관련된 기능
		#DBCount =Course_Evaluation.objects.filter(Course=LectureInformation).count()
		O_Count = DataCount(3,len(OtherCourseBoard))
		tempLecture=Lecture.objects.filter(Code=LectureInformation.Code,CourseName = LectureInformation.CourseName, Professor=LectureInformation.Professor)
		
		#전체 페이지가 11페이지 이상인 것을 기준으로 정의
		if Mobile == "full":
			PageInformation=FirstPageView(O_Count)
			OtherCount=PageTotalCount(O_Count,PageInformation)
		else:
			PageInformation=MobileFirstPageView(O_Count)
			OtherCount=MobilePageTotalCount(O_Count,PageInformation,3)
		OtherCourseBoard=OtherCourseBoard[PageFirst:PageLast]
		MyCourseBoard= VacationSemesterChange(MyCourseBoard)
		OtherCourseBoard= VacationSemesterChange(OtherCourseBoard)
		
		#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
		dic ={'user':request.user,
			'BestBoard':BestBoardView(),
			'CourseBoard':CourseBoard,
			'MyCourseBoard':MyCourseBoard,
			'OtherCourseBoard':OtherCourseBoard,
			'OtherCount':OtherCount,
			'PageInformation':PageInformation,
			'Answer_Dis' : Description,
			
			
			}
		if request.flavour =='full':
			return render_to_response('html/course.html',dic)
		else:
			return render_to_response("m_skins/m_html/course.html",dic)
'''
def PeriodCourse(request,offset): #학기별로 나뉘어진 강의 눌렀을 때 나오는 강의 추천 결과(처음 눌럿을때 )
		if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")
		Mobile=request.flavour
		#현재 접속한 아이디 정보 받아옴
		try:
			
			UserData = Profile.objects.get(User = request.user)
		except :
			UserData =None
		
		#강의 추천 1번이상 안했을 시 정보 안 보여줌
		if UserData.RecommendCount <1:
			if request.flavour =='full':
					return render_to_response("html/Course_error.html")
			else:
				return render_to_response("m_skins/m_html/Course_error.html")
		else:
				try:
					offset = int(offset)
				except:
					raise Http404()
				#보려는 강의 정보 
				LectureInformation=Lecture.objects.get(id=offset)

				CourseBoard=TotalCourseProfessor(LectureInformation.CourseName,LectureInformation.Professor,LectureInformation.Code)#해당 강의 전체 추천한 Data DB 불러오기
				
				
				#자신이 햇을 경우 자신이 평가한 정보를 보여주는 기능
				try:
					MyCourseBoard = Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code, CreatedID = UserData)
				except:
					MyCourseBoard = None
				
				#한 페이지에 뿌리는 기능
				PageFirst = 3*(1-1)
				PageLast = 3*(1-1)+3
				MergeCourse=None
			
				
				OtherCourse=Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code).order_by('-id')
					

		
				OtherCourseBoard = []
				#접속한 아이디와 중복되는 경우 제거
				for Board in OtherCourse:
					if Board.CreatedID == UserData:
							pass
					else:
						OtherCourseBoard.append(Board)

				
				#pageNation과 관련된 기능
				DBCount =Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code).count()
				O_Count = DataCount(3,DBCount)
				
				if Mobile =="full":					
					#전체 페이지가 11페이지 이상인 것을 기준으로 정의
					PageInformation=FirstPageView(O_Count)
					#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
					OtherCount=PageTotalCount(O_Count,PageInformation)
				else:
					PageInformation=MobileFirstPageView(O_Count)
					#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
					OtherCount=MobilePageTotalCount(O_Count,PageInformation,3)
				dic ={'user':request.user,
					'BestBoard':BestBoardView(),
					'CourseBoard':CourseBoard,
					'MyCourseBoard':MyCourseBoard,
					'OtherCourseBoard':OtherCourseBoard,
					'OtherCount':OtherCount,
					'PageInformation':PageInformation
					}
				if request.flavour =='full':
					return render_to_response('html/course.html',dic)
				else:
					return render_to_response("m_skins/m_html/course.html",dic)

@csrf_exempt
def PeriodCoursePage(request,offset): #학기별로 나뉘어진 강의 눌렀을 때 나오는 강의 추천 결과(페이지 번호 눌렀을때)
		
		if CheckingLogin(request.user.username):
			return HttpResponseRedirect("/")
		Mobile = request.flavour
		#현재 접속한 아이디 정보 받아옴
		try:
			if request.method =="POST":
				offset2 =int(request.POST["Page"]) 
			UserData = Profile.objects.get(User = request.user)
		except :
			UserData =None
			raise Http404()
		
		#강의 추천 1번이상 안했을 시 정보 안 보여줌
		if UserData.RecommendCount <1:
			if request.flavour =='full':
					return render_to_response("html/Course_error.html")
			else:
				return render_to_response("m_skins/m_html/Course_error.html")
		else:
				try:
					offset = int(offset[6:])
				except:
					raise Http404()
				#보려는 강의 정보 
				LectureInformation=Lecture.objects.get(id=offset)

				CourseBoard=TotalCourseProfessor(LectureInformation.CourseName,LectureInformation.Professor,LectureInformation.Code)#해당 강의 전체 추천한 Data DB 불러오기
				
				
				#자신이 햇을 경우 자신이 평가한 정보를 보여주는 기능
				try:
					MyCourseBoard = Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code, CreatedID = UserData)
				except:
					MyCourseBoard = 1
				
				#한 페이지에 뿌리는 기능
				PageFirst = (offset2-1)*3
				PageLast = (offset2-1)*3+3
				OtherCourse=Course_Evaluation.objects.filter(Course__CourseName = LectureInformation.CourseName, Course__Professor=LectureInformation.Professor,Course__Code =LectureInformation.Code).order_by('-id')
					

		
				OtherCourseBoard = []
				#접속한 아이디와 중복되는 경우 제거
				for Board in OtherCourse:
					if Board.CreatedID == UserData:
							pass
					else:
						OtherCourseBoard.append(Board)

				
				#pageNation과 관련된 기능
				DBCount =Course_Evaluation.objects.filter(Course=LectureInformation).count()
				O_Count = DataCount(3,DBCount)
				
				#전체 페이지가 11페이지 이상인 것을 기준으로 정의
				if Mobile =="full":
					PageInformation=FirstPageView(O_Count)
					#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
					OtherCount=PageTotalCount(O_Count,PageInformation)
				else:
					PageInformation=MobileFirstPageView(O_Count)
					#총 데이터수와 page 넘길때 번호랑 호환되게 하기 위해 함	
					OtherCount=MobilePageTotalCount(O_Count,PageInformation,3)

				dic ={'user':request.user,
					'BestBoard':BestBoardView(),
					'CourseBoard':CourseBoard,
					'MyCourseBoard':MyCourseBoard,
					'OtherCourseBoard':OtherCourseBoard,
					'OtherCount':OtherCount,
					'PageInformation':PageInformation
					}
				if request.flavour =='full':
					return render_to_response('html/coursepage.html',dic)
				else:
					return render_to_response("m_skins/m_html/coursepage.html",dic)
'''
#해당 강의 총 평가 데이터 모음을 구현 하기 위한 함수
def TotalCourse(offset):
	LectureInformation=Lecture.objects.get(id = offset)
	try:
		CourseBoard = Total_Evaluation.objects.get(Course__Code =LectureInformation.Code,Course__CourseName=LectureInformation.CourseName, Course__Professor=LectureInformation.Professor)
		CourseBoard.Total_Speedy = CourseBoard.Total_Speedy/CourseBoard.Total_Count
		CourseBoard.Total_Homework = CourseBoard.Total_Homework/CourseBoard.Total_Count
		CourseBoard.Total_Level_Difficulty = CourseBoard.Total_Level_Difficulty/CourseBoard.Total_Count
		CourseBoard.Total_StarPoint = CourseBoard.Total_StarPoint/CourseBoard.Total_Count

	except:
		CourseBoard = Total_Evaluation(Course =Lecture.objects.get(id=offset))
		CourseBoard.Total_Speedy=5
		CourseBoard.Total_Homework =5
		CourseBoard.Total_Level_Difficulty=5
		CourseBoard.Total_StarPoint=0

	return CourseBoard
def TotalCourseProfessor(CourseName,Professor,Code):
		try:
			CourseBoard = Total_Evaluation.objects.filter(Course__Code =Code,Course__CourseName=CourseName,Course__Professor=Professor)[0]
		except:
			pass
		if CourseBoard.Total_Count!=0:
			CourseBoard.Total_Speedy = CourseBoard.Total_Speedy/CourseBoard.Total_Count
			CourseBoard.Total_Homework = CourseBoard.Total_Homework/CourseBoard.Total_Count
			CourseBoard.Total_Level_Difficulty = CourseBoard.Total_Level_Difficulty/CourseBoard.Total_Count
			CourseBoard.Total_StarPoint = CourseBoard.Total_StarPoint/CourseBoard.Total_Count

		'''
		try:
			CourseBoard = Total_Evaluation(Course=Course[0].Course)
		except:
			CourseBoard = Total_Evaluation(Course=Lecture.objects.filter(CourseName=CourseName,Professor=Professor,Code =Code).order_by('Semester')[0])
			CourseBoard.Total_Speedy = 5
			CourseBoard.Total_Homework = 5
			CourseBoard.Total_Level_Difficulty = 5
			CourseBoard.Total_Count = 0
			CourseBoard.Total_StarPoint=0

		for CourseList in Course:
			CourseBoard.Total_Count +=CourseList.Total_Count
			CourseBoard.Total_Speedy += CourseList.Total_Speedy
			CourseBoard.Total_Homework += CourseList.Total_Homework
			CourseBoard.Total_Level_Difficulty += CourseList.Total_Level_Difficulty
			CourseBoard.Total_StarPoint+= CourseList.Total_StarPoint
			CourseBoard.Total_Mix += CourseList.Total_Mix
			CourseBoard.Total_Short_Answer += CourseList.Total_Short_Answer
			CourseBoard.Total_Long_Answer += CourseList.Total_Long_Answer
			CourseBoard.Total_Unknown_Answer += CourseList.Total_Unknown_Answer
		if CourseBoard.Total_Count!=0:
			CourseBoard.Total_Speedy = CourseBoard.Total_Speedy/CourseBoard.Total_Count
			CourseBoard.Total_Homework = CourseBoard.Total_Homework/CourseBoard.Total_Count
			CourseBoard.Total_Level_Difficulty = CourseBoard.Total_Level_Difficulty/CourseBoard.Total_Count
			CourseBoard.Total_StarPoint = CourseBoard.Total_StarPoint/CourseBoard.Total_Count
		
		return CourseBoard
		'''
		return CourseBoard