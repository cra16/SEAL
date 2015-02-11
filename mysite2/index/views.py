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
def MyPage(request):	#MyPage 루트
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("sealmypage.html", {'user':request.user}) 

def About(request): #About template 루트
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("about.html",{'user':request.user})

def Schedule(request): #Schedule template 루트
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("schedule.html",{'user':request.user})

def Judgement(request): # 사용자 신고 template 루트
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_report.html",{'user':request.user})

@csrf_exempt
def Recommend(request, offset): #추천 강의 스크롤 template 보여주는 루트
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except:
			raise Http404()


		
		CourseBoard = Lecture.objects.get(id=offset) #DB 고유 ID로 접근해서 검색		
		request.session['Recommend_ID'] = offset #offset 미리 저장
		return render_to_response("recommend.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                         #  'TotalCount' : range(0,TotalCount)
											})
@csrf_exempt
def Recommend_Write(request): #추천 강의 DB입력
        if request.user.username=="":
                return HttpResponseRedirect("/mysite2")
        else:

                if request.method =="POST":
                        new_Course=Lecture.objects.get(id=request.session['Recommend_ID'])
                        new_CreatedID = Profile.objects.get(User= request.user)
                        new_Speedy=request.POST['sl1']
                        new_Reliance=request.POST['sl2']
                        new_Helper=request.POST['sl3']
                        new_Question=request.POST['sl4']
                        new_Exam=request.POST['sl5']
                        new_Homework=request.POST['sl6']
                        new_Eval = Course_Evaluation(Course = new_Course, CreatedID = new_CreatedID, Speedy = new_Speedy, Reliance = new_Reliance, Helper = new_Helper, Question = new_Question, Exam = new_Exam, Homework=new_Homework)
                        new_Eval.save()


                        L_Eval = Lecture.objects.get(id=request.session['Recommend_ID'])#session에 저장된 ID를 통해 강의 정보 갖고오기

                        try:
                                T_Eval=Total_Evaluation.objects.get(CourseName=L_Eval)#강의 정보 DB로 간접 접근해서 Total 값 검색

                        except:
                                T_Eval =None 


                        if T_Eval is None: #데이터 없을시 Table 생성
                                Total_Eval = Total_Evaluation(CourseName = new_Course, Total_Speedy = new_Speedy, Total_Reliance = new_Reliance, Total_Helper = new_Helper, Total_Question = new_Question,Total_Exam = new_Exam,  Total_Homework = new_Homework, Total_Count =1)
                                Total_Eval.save()
                        else: #update
                                T_Eval.Total_Speedy += int(new_Speedy)
                                T_Eval.Total_Reliance += int(new_Reliance)
                                T_Eval.Total_Helper += int(new_Helper)
                                T_Eval.Total_Question += int(new_Question)
                                T_Eval.Total_Exam += int(new_Question)
                                T_Eval.Total_Homework += int(new_Homework)
                                T_Eval.Total_Count += int(new_Homework)
                                T_Eval.save()
                        return render_to_response("course.html",{'user':request.user,})

                else:
                        return HttpResponseRedirect("/mysite2")


		


@csrf_exempt
def QnAMain(request): #Q&A 부분 조작(좀 손봐야함)
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :
		#받은 정보 저장(이것도 옮길 예정 다끝나면..)
		if request.method =="POST":
			new_Text=request.POST['msg-body-txtarea']		
			new_TextWriter = request.user.username
			new_TextName = request.POST['msg-title-input']
			new_QnA = QnA_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
			new_QnA.save()
		#페이지 넘기는 기능
		count=QnA_Board.objects.count()
		TotalCount = (count/8)+1 #페이지 수

		if TotalCount ==1:
			Next = 1
		else:
			Next =TotalCount
		Previous=1
		
		PageBoard = QnA_Board.objects.order_by('-id')[0:7]
		return render_to_response("QnA.html",
					  {'user':request.user,
					   'PageBoard':PageBoard, 
					   'TotalCount' : range(0,TotalCount), 
					   'Previous' : Previous, 
					   'Next' : Next,
					   })

def QnA(request,offset): #페이지 이동시 정보 보여주는 곳
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		#페이지 수 정보
		PageFirst = (offset-1)*6 
		PageLast = (offset-1)*6 + 6
		PageBoard = QnA_Board.objects.order_by('-id')[PageFirst:PageLast]
		#######	페이지 넘기는 기능
		Page = dict()
		count = QnA_Board.objects.count()
		TotalCount = (count/8)+1
		if offset == 1:
			if TotalCount ==1:
				Next = offset
			else : 
				Next =offset +1
			Previous=1
		elif offset ==TotalCount:
			Previous=offset-1
			Next = TotalCount
		else:
			Previous = offset-1
			Next = offset +1
        
		return render_to_response("QnA.html",
					  {'user':request.user, 
					   'PageBoard':PageBoard, 	
					   'TotalCount' : range(0,TotalCount), 
	       			   'Previous' : Previous, 
					   'Next' : Next} )
	
def QnAWrite(request): #Q&A Write 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_faq.html",{'user':request.user})

def QnARead(request, offset): #Q&A read 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = QnA_Board.objects.filter(id=offset).get() #id를 기준으로 호출함
	
	
		return render_to_response("qna-contents.html", {'user':request.user, 'Board':Current})

def Course(request, offset): #선택된 강의 추천 전체 목록 기능

	#강의 추천시 권한 아직 안줌

	if request.user.username =="":
                return  HttpResponseRedirect("/mysite2")
        else:
                try:
                        offset = int(offset)
                except:
                        raise Http404()

				
				#해당 강의 전체 추천 평균 스크롤 보여주는 기능
				CourseBoard = Total_Evaluation.objects.get(CourseName = Lecture.objects.get(id = offset))
				CourseBoard.Total_Speedy = CourseBoard.Total_Speedy/CourseBoard.Total_Count
				CourseBoard.Total_Reliance = CourseBoard.Total_Reliance/CourseBoard.Total_Count
				CourseBoard.Total_Helper = CourseBoard.Total_Helper/CourseBoard.Total_Count
				CourseBoard.Total_Question = CourseBoard.Total_Question/CourseBoard.Total_Count
				CourseBoard.Total_Exam = CourseBoard.Total_Exam/CourseBoard.Total_Count
				CourseBoard.Total_Homework = CourseBoard.Total_Homework/CourseBoard.Total_Count
				
				#로그인 당사자가 추천 한 스크롤 보여주는 기능
                MyCourseBoard = Course_Evaluation.objects.get(CreatedID = Profile.objects.get(User=request.user))
				#다른 사람들이 해놓은 것 시간순으로 보여준 기능
                OtherCourseBoard = Course_Evaluation.objects.order_by('-id')[0:3]
                Other_ID_Information = [0,0,0]
                for i in range(0,3):
                        try:
                                Other_ID_Information[i] = Profile.objects.get(User = OtherCourseBoard[i])
                        except:
                                break

                return render_to_response("course.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                           'MyCourseBoard':MyCourseBoard,
                                           'OtherCourseBoard':OtherCourseBoard,
                                           'Other_ID_Information':Other_ID_Information
                                         #  'TotalCount' : range(0,TotalCount),

                                           })





			
			

				

def NoticeMain(request):#Notice 메인 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		count=Notice_Board.objects.count()

		TotalCount = (count/8)+1

		if TotalCount ==1:
			Next = 1
		else:
			Next = 2
		Previous=1
	
		PageBoard = Notice_Board.objects.order_by('-id')[0:7]	
		return render_to_response("notice.html",
					  {'user':request.user,
					   'PageBoard':PageBoard, 
					   'TotalCount' : range(0,TotalCount), 
					   'Previous' : Previous, 
					   'Next' : Next,
					   })

def Notice(request,offset): #Notice Page 넘기기 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		#페이지 수 정보
		PageFirst = (offset-1)*6
		PageLast = (offset-1)*6 + 6
		PageBoard = Notice_Board.objects.order_by('-id')[PageFirst:PageLast] 
		#페이지 넘기는 기능
		Page = dict()
		count = Notice_Board.objects.count()
		TotalCount = (count/8)+1
		if offset == 1:
			if TotalCount ==1:
				Next = offset
			else : 
				Next =offset +1
			Previous=1
		elif offset ==TotalCount:
			Previous=offset-1
			Next = TotalCount
		else:
			Previous = offset-1
			Next = offset +1 
       
		return render_to_response("notice.html",
					  {'user':request.user, 
					   'PageBoard':PageBoard,
					   'TotalCount' : range(0,TotalCount), 
	       			   'Previous' : Previous, 
					   'Next' : Next} )

def Notice_Read(request, offset): #Notice Read 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = Notice_Board.objects.filter(id=offset).get()
		
	
		return render_to_response("notice-contents.html", {'user':request.user, 'Board':Current})

def Main(request, offset): #Main 기능
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:

				try:
					offset = int(offset)
				except ValueError:
					raise Http404()
								
				PageInformation1 = request.session['PageInformation1'] #First Major Page DB
				PageInformation2 = request.session['PageInformation2'] #Second Major Page DB
				PageInformation3 = request.session['PageInformation3'] #all Page DB
				

				#main 자바스크립트 조작 하기 위한 기능
				Active = ["","",""]

				URL_Path = request.path	#현재 페이지 URL 긁어오기
			
			
				##강의 DB에 저장된 자료들을 코드로 필터를 해서 Total Page를 만듦
				##그리고 나서 강의추천된 강의들만 따로 또 필터해서 데이터 넣는 과정임
				##다른 개발자분이 좀 알고리즘 잘짜서 더 최적화해주세요..(발적화임..))
				
				TotalBoard1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP"))[(PageInformation1[1]-1)*6:(PageInformation1[1]-1)*6+6]
				TotalBoard2 = Lecture.objects.filter(Code__contains = "SIE")[(PageInformation2[1]-1)*6:(PageInformation2[1]-1)*6+6]
				TotalBoard3 = Lecture.objects.order_by('-id')[(PageInformation3[1]-1)*6:(PageInformation3[1]-1)*6+6]
				
				T_Count1 = Lecture.objects.filter(Q(Code__contains="ECE") | Q(Code__contains="ITP")).count()
				T_Count2 = Lecture.objects.filter(Code__contains ="SIE").count()
				T_Count3=Lecture.objects.count()
				
				PageBoard = PageView(TotalBoard1,TotalBoard2,TotalBoard3)
				
				if URL_Path.find("FirstMajorPage") != -1 :
					PageInformation1[1] = offset
					if T_Count1 >11:
						if offset>11:
							PageInformation1[0] = (offset -(offset%10))-9
							PageInformation1[2] = (offset -(offset%10))+11
						else:
							PageInformation1[0] = 1
							PageInformation1[2] = (offset - (offset%10))+11
					else:
						PageInformation[0] = 1
						PageInformation[2] = T_Count1

					Active[0] = "active" #

				elif URL_Path.find("SecondMajorPage") != -1:
					PageInformation2[1] = offset

					if T_Count1 >11:
						if offset>11:
							PageInformation2[0] = (offset -(offset%10))-9
							PageInformation2[2] = (offset -(offset%10))+11
						else:
							PageInformation1[0] = 1
							PageInformation1[2] = (offset - (offset%10))+11
					else:
						PageInformation[0] = 1
						PageInformation[2] = T_Count1
					Active[1] = "active"
				else:
					PageInformation3[1] = offset
					if T_Count1 >11:
						if offset>11:
							PageInformation3[0] = (offset -(offset%10))-9
							PageInformation3[2] = (offset -(offset%10))+11
						else:
							PageInformation1[0] = 1
							PageInformation1[2] = (offset - (offset%10))+11
					else:
						PageInformation[0] = 1
						PageInformation[2] = T_Count1
					Active[2] = "active"


			
				##Session Save
				request.session['PageInformation1'] = PageInformation1
				request.session['PageInformation2'] = PageInformation2
				request.session['PageInformation3'] = PageInformation3
				
				
				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard':PageBoard,
					   'TotalCount1' : range(PageInformation1[1]-(PageInformation1[1]%10)+1,PageInformation1[1]-(PageInformation1[1]%10)+11),
					   'TotalCount2' : range(PageInformation2[1]-(PageInformation2[1]%10)+1,PageInformation2[1]-(PageInformation2[1]%10)+11),
					   'TotalCount3' : range(PageInformation3[1]-(PageInformation3[1]%10)+1,PageInformation3[1]-(PageInformation3[1]%10)+11),
					   'PageInformation1' : PageInformation1,
					   'PageInformation2' : PageInformation2,
					   'PageInformation3' : PageInformation3,
					   'Path':URL_Path,
					   'Active':Active,
					   })

def SubScript(request):
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_improve.html", {'user':request.user})

def SiteMap(request):
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("sitemap.html", {'user':request.user})

# Create your views here


def PageView(TotalBoard1,TotalBoard2,TotalBoard3):
				PageBoard =[[],[],[]]
				for Board in TotalBoard1:
					try:
						Board1 = Total_Evaluation.objects.get(CourseName=Board)
					except :
						Board1 = None
					if Board1 is not None:
						Board1.Total_Speedy = Board1.Total_Speedy/Board1.Total_Count
						Board1.Total_Reliance = Board1.Total_Reliance/Board1.Total_Count
						Board1.Total_Helper = Board1.Total_Helper/Board1.Total_Count
						Board1.Total_Question = Board1.Total_Question/Board1.Total_Count
						Board1.Total_Exam = Board1.Total_Exam/Board1.Total_Count
						Board1.Total_Homework = Board1.Total_Homework/Board1.Total_Count
						PageBoard[0].append(Board1)
					else:
						Board1 = Total_Evaluation(CourseName=Board)
						Board1.Total_Speedy =5
						Board1.Total_Reliance =5
						Board1.Total_Helper = 5
						Board1.Total_Question = 5
						Board1.Total_Exam = 5
						Board1.Total_Homework = 5
						Board1.Total_Count =1
						PageBoard[0].append(Board1)
				
				for Board in TotalBoard2:
					try:		
						Board2 = Total_Evaluation.objects.get(CourseName=Board)
					except :
						Board2 = None
					if Board2 is not None:
						Board2.Total_Speedy = Board2.Total_Speedy/Board2.Total_Count
						Board2.Total_Reliance = Board2.Total_Reliance/Board2.Total_Count
						Board2.Total_Helper = Board2.Total_Helper/Board2.Total_Count
						Board2.Total_Question = Board2.Total_Question/Board2.Total_Count
						Board2.Total_Exam = Board2.Total_Exam/Board2.Total_Count
						Board2.Total_Homework = Board2.Total_Homework/Board2.Total_Count
						PageBoard[1].append(Board2)
					else:
						Board2 = Total_Evaluation(CourseName=Board)
						Board2.Total_Speedy =5
						Board2.Total_Reliance =5
						Board2.Total_Helper = 5
						Board2.Total_Question = 5
						Board2.Total_Exam = 5
						Board2.Total_Homework = 5
						Board2.Total_Count =1
						PageBoard[1].append(Board2)		
				
				for Board in TotalBoard3:
					try:
						Board3 = Total_Evaluation.objects.get(CourseName=Board)
					except :
						Board3 = None
					if Board3 is not None:
						Board3.Total_Speedy = Board3.Total_Speedy/Board3.Total_Count
						Board3.Total_Reliance = Board3.Total_Reliance/Board3.Total_Count
						Board3.Total_Helper = Board3.Total_Helper/Board3.Total_Count
						Board3.Total_Question = Board3.Total_Question/Board3.Total_Count
						Board3.Total_Exam = Board3.Total_Exam/Board3.Total_Count
						Board3.Total_Homework = Board3.Total_Homework/Board3.Total_Count
						PageBoard[2].append(Board3)
					else:
						Board3 = Total_Evaluation(CourseName=Board)
						Board3.Total_Speedy =5
						Board3.Total_Reliance =5
						Board3.Total_Helper = 5
						Board3.Total_Question = 5
						Board3.Total_Exam = 5
						Board3.Total_Homework = 5
						Board3.Total_Count =1
						PageBoard[2].append(Board3)
				return PageBoard