from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from login.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q
def MyPage(request):	#MyPage template 부르는 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("sealmypage.html", {'user':request.user}) 

def About(request): #About template 부르는 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("about.html",{'user':request.user})

def Schedule(request): #Schedule template 부르는 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("schedule.html",{'user':request.user})

def Judgement(request): # 신고 template 부르는 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_report.html",{'user':request.user})

def Recommend(request, offset): #강의 추천 스크롤 입력 template 보여줌
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except:
			raise Http404()


		
		CourseBoard = Lecture.objects.get(id=offset) #강의에 부여된 고유 ID 기준으로 DB 호출, 강의 정보 보여주기위함 
		request.session['Recommend_ID'] = offset #추천 이후 offset이 날아가서 session에 저장함
		return render_to_response("recommend.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                         #  'TotalCount' : range(0,TotalCount)
											})
@csrf_exempt
def Recommend_Write(request): #강의 추천 DB 입력 기능
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


                        L_Eval = Lecture.objects.get(id=request.session['Recommend_ID'])#강의 정보를 session에 저장한 offset을 이용해서 해당 강의 정보 저장

                        try:
                                T_Eval=Total_Evaluation.objects.get(CourseName=L_Eval)#위의 L_Eval을 통해 총 강의정보가 있으면 검색해서 테이블 정보 넣음

                        except:
                                T_Eval =None 


                        if T_Eval is None: #Table에 데이터 없을시 데이터 생성 및 저장
                                Total_Eval = Total_Evaluation(CourseName = new_Course, Total_Speedy = new_Speedy, Total_Reliance = new_Reliance, Total_Helper = new_Helper, Total_Question = new_Question,Total_Exam = new_Exam,  Total_Homework = new_Homework, Total_Count =1)
                                Total_Eval.save()
                        else: #업데이트
                                T_Eval.Total_Speedy += int(new_Speedy)
                                T_Eval.Total_Reliance += int(new_Reliance)
                                T_Eval.Total_Helper += int(new_Helper)
                                T_Eval.Total_Question += int(new_Question)
                                T_Eval.Total_Exam += int(new_Question)
                                T_Eval.Total_Homework += int(new_Homework)
                                T_Eval.Total_Count += int(new_Homework)
                                T_Eval.save()
                        return HttpResponseRedirect("/mysite2")

                else:
                        return HttpResponseRedirect("/mysite2")


		


@csrf_exempt
def QnAMain(request): #Q&A 메인 부분 및 DB 조작 하는 곳
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :
		if request.method =="POST":
			new_Text=request.POST['msg-body-txtarea']		
			new_TextWriter = request.user.username
			new_TextName = request.POST['msg-title-input']
			new_QnA = QnA_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
			new_QnA.save()#QnA입력 후 나온 정보들을 일괄적으로 처리 하기 위해 함

		count=QnA_Board.objects.count()
		TotalCount = (count/8)+1 #총 페이지 수 

		if TotalCount ==1:
			Next = 1
		else:
			Next =TotalCount
		Previous=1
	
		PageBoard = QnA_Board.objects.order_by('-id')[0:7] #해당 페이지에서 보여줄 정보를 몇개 보여주는 역할	
		return render_to_response("QnA.html",
					  {'user':request.user,
					   'PageBoard':PageBoard, 
					   'TotalCount' : range(0,TotalCount), 
					   'Previous' : Previous, 
					   'Next' : Next,
					   })

def QnA(request,offset): #페이지 넘어갔을때 현재 페이지 정보를 보여주기 위한 함수
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		PageFirst = (offset-1)*6 
		PageLast = (offset-1)*6 + 6
		PageBoard = QnA_Board.objects.order_by('-id')[PageFirst:PageLast] #이 페이지에서 보여줘야할 정보들을 표현
		#######	
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
       #여기까지 페이지 넘기는 거 구현함 
		return render_to_response("QnA.html",
					  {'user':request.user, 
					   'PageBoard':PageBoard, # 페이지 정보
					   'TotalCount' : range(0,TotalCount), #페이지 총 갯수
	       			   'Previous' : Previous, 
					   'Next' : Next} )
	
def QnAWrite(request): #페이지 쓰기 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_faq.html",{'user':request.user})

def QnARead(request, offset): #페이지 읽기 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = QnA_Board.objects.filter(id=offset).get() #id 기준으로 호출
	
	
		return render_to_response("qna-contents.html", {'user':request.user, 'Board':Current})

def Course(request, offset): #해당 과목 전체 강의 추천 평균 및 개인이 한 것을 보여줌

		#아직 강의 추천했을 시 볼수 있는 권한 안줌


	 if request.user.username =="":
                return  HttpResponseRedirect("/mysite2")
        else:
                try:
                        offset = int(offset)
                except:
                        raise Http404()



				CourseBoard = Total_Evaluation.objects.get(CourseName = Lecture.objects.get(id = offset))
                CourseBoard.Total_Speedy = CourseBoard.Total_Speedy/CourseBoard.Total_Count
                CourseBoard.Total_Reliance = CourseBoard.Total_Reliance/CourseBoard.Total_Count
                CourseBoard.Total_Helper = CourseBoard.Total_Helper/CourseBoard.Total_Count
                CourseBoard.Total_Question = CourseBoard.Total_Question/CourseBoard.Total_Count
                CourseBoard.Total_Exam = CourseBoard.Total_Exam/CourseBoard.Total_Count
                CourseBoard.Total_Homework = CourseBoard.Total_Homework/CourseBoard.Total_Count

                MyCourseBoard = Course_Evaluation.objects.get(CreatedID = request.user.username)
                OtherCourseBoard = Course_Evaluation.objects.order_by('-id')[0:3]
                Other_ID_Information = [0,0,0]
                for i in range(0,3):
                        Other_ID_Information[i] = Profile.objects.get(User = OtherCourseBoard[i])
                return render_to_response("course.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                           'MyCourseBoard':MyCourseBoard,
                                           'OtherCourseBoard':OtherCourseBoard,
                                           'Other_ID_Information':Other_ID_Information
                                         #  'TotalCount' : range(0,TotalCount),

                                           })




			
			

				

def NoticeMain(request):#공지사항 기능 대부분 메인페이지는 거의 비슷하기때문에 주석 생략
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		count=QnA_Board.objects.count()

		TotalCount = (count/8)+1

		if TotalCount ==1:
			Next = 1
		else:
			Next = 2
		Previous=1
	
		PageBoard = QnA_Board.objects.order_by('-id')[0:7]	
		return render_to_response("notice.html",
					  {'user':request.user,
					   'PageBoard':PageBoard, 
					   'TotalCount' : range(0,TotalCount), 
					   'Previous' : Previous, 
					   'Next' : Next,
					   })

def Notice(request,offset): #공지사항 페이지 넘기는 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		PageFirst = (offset-1)*6
		PageLast = (offset-1)*6 + 6
		PageBoard = Notice_Board.objects.order_by('-id')[PageFirst:PageLast] #페이지 정보 출력 기능
	
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
			Next = offset +1 #여기까지 페이지 넘기는 기능
       
		return render_to_response("notice.html",
					  {'user':request.user, 
					   'PageBoard':PageBoard,
					   'TotalCount' : range(0,TotalCount), 
	       			   'Previous' : Previous, 
					   'Next' : Next} )

def Notice_Read(request, offset): #공지사항 읽기 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = Notice_Board.objects.filter(id=offset).get()
		
	
		return render_to_response("notice-contents.html", {'user':request.user, 'Board':Current})

def Main(request, offset): #메인입니다.
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:

				try:
					offset = int(offset)
				except ValueError:
					raise Http404()
		

	
				
				
				PageInformation1 = request.session['PageInformation1'] #1전공 페이지 DB
				PageInformation2 = request.session['PageInformation2'] #2전공 페이지 DB
				PageInformation3 = request.session['PageInformation3'] #all 페이지 DB
				

				Active = ["","",""] #페이지에 있는 자바스크립트 on할것인지 하려고 만든 리스트

				URL_Path = request.path #페이지 넘겼을 때 해당 페이지를 보여주기 위해 써야함
				###
				if URL_Path.find("FirstMajorPage") != -1 :
					PageInformation1[1] = offset
					Active[0] = "active" #index.html에 보면 이 변수를 이용해서 자바스크립트 조작
				elif URL_Path.find("SecondMajorPage") != -1:
					PageInformation2[1] = offset
					Active[1] = "active"
				else:
					PageInformation3[1] = offset
					Active[2] = "active"
				###여기까지 자바스크립트 조작 하는 곳
			
				##
				PageBoard1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP"))[(PageInformation1[1]-1)*6:(PageInformation1[1]-1)*6+6]
				PageBoard2 = Lecture.objects.filter(Code__contains = "SIE")[(PageInformation2[1]-1)*6:(PageInformation2[1]-1)*6+6]
				PageBoard3 = Lecture.objects.order_by('-id')[(PageInformation3[1]-1)*6:(PageInformation3[1]-1)*6+6]
				
				TotalCount1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP")).count()
				TotalCount2 =  Lecture.objects.filter(Code__contains = "SIE").count()
				TotalCount3 =  Lecture.objects.count()
				
				
			
				##세션 저장 후 
				request.session['PageInformation1'] = PageInformation1
				request.session['PageInformation2'] = PageInformation2
				request.session['PageInformation3'] = PageInformation3
				
				
				return render_to_response("index.html",
					  {'user':request.user,
					   'PageBoard1':PageBoard1,
					   'PageBoard2':PageBoard2,
					   'PageBoard3':PageBoard3,
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
