from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from login.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q
def MyPage(request):	#MyPage template �θ��� ���
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("sealmypage.html", {'user':request.user}) 

def About(request): #About template �θ��� ���
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("about.html",{'user':request.user})

def Schedule(request): #Schedule template �θ��� ���
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("schedule.html",{'user':request.user})

def Judgement(request): # �Ű� template �θ��� ���
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_report.html",{'user':request.user})

def Recommend(request, offset): #���� ��õ ��ũ�� �Է� template ������
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except:
			raise Http404()


		
		CourseBoard = Lecture.objects.get(id=offset) #���ǿ� �ο��� ���� ID �������� DB ȣ��, ���� ���� �����ֱ����� 
		request.session['Recommend_ID'] = offset #��õ ���� offset�� ���ư��� session�� ������
		return render_to_response("recommend.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                         #  'TotalCount' : range(0,TotalCount)
											})
@csrf_exempt
def Recommend_Write(request): #���� ��õ DB �Է� ���
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


                        L_Eval = Lecture.objects.get(id=request.session['Recommend_ID'])#���� ������ session�� ������ offset�� �̿��ؼ� �ش� ���� ���� ����

                        try:
                                T_Eval=Total_Evaluation.objects.get(CourseName=L_Eval)#���� L_Eval�� ���� �� ���������� ������ �˻��ؼ� ���̺� ���� ����

                        except:
                                T_Eval =None 


                        if T_Eval is None: #Table�� ������ ������ ������ ���� �� ����
                                Total_Eval = Total_Evaluation(CourseName = new_Course, Total_Speedy = new_Speedy, Total_Reliance = new_Reliance, Total_Helper = new_Helper, Total_Question = new_Question,Total_Exam = new_Exam,  Total_Homework = new_Homework, Total_Count =1)
                                Total_Eval.save()
                        else: #������Ʈ
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
def QnAMain(request): #Q&A ���� �κ� �� DB ���� �ϴ� ��
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :
		if request.method =="POST":
			new_Text=request.POST['msg-body-txtarea']		
			new_TextWriter = request.user.username
			new_TextName = request.POST['msg-title-input']
			new_QnA = QnA_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
			new_QnA.save()#QnA�Է� �� ���� �������� �ϰ������� ó�� �ϱ� ���� ��

		count=QnA_Board.objects.count()
		TotalCount = (count/8)+1 #�� ������ �� 

		if TotalCount ==1:
			Next = 1
		else:
			Next =TotalCount
		Previous=1
	
		PageBoard = QnA_Board.objects.order_by('-id')[0:7] #�ش� ���������� ������ ������ � �����ִ� ����	
		return render_to_response("QnA.html",
					  {'user':request.user,
					   'PageBoard':PageBoard, 
					   'TotalCount' : range(0,TotalCount), 
					   'Previous' : Previous, 
					   'Next' : Next,
					   })

def QnA(request,offset): #������ �Ѿ���� ���� ������ ������ �����ֱ� ���� �Լ�
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		PageFirst = (offset-1)*6 
		PageLast = (offset-1)*6 + 6
		PageBoard = QnA_Board.objects.order_by('-id')[PageFirst:PageLast] #�� ���������� ��������� �������� ǥ��
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
       #������� ������ �ѱ�� �� ������ 
		return render_to_response("QnA.html",
					  {'user':request.user, 
					   'PageBoard':PageBoard, # ������ ����
					   'TotalCount' : range(0,TotalCount), #������ �� ����
	       			   'Previous' : Previous, 
					   'Next' : Next} )
	
def QnAWrite(request): #������ ���� ���
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_faq.html",{'user':request.user})

def QnARead(request, offset): #������ �б� ���
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = QnA_Board.objects.filter(id=offset).get() #id �������� ȣ��
	
	
		return render_to_response("qna-contents.html", {'user':request.user, 'Board':Current})

def Course(request, offset): #�ش� ���� ��ü ���� ��õ ��� �� ������ �� ���� ������

		#���� ���� ��õ���� �� ���� �ִ� ���� ����


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




			
			

				

def NoticeMain(request):#�������� ��� ��κ� ������������ ���� ����ϱ⶧���� �ּ� ����
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

def Notice(request,offset): #�������� ������ �ѱ�� ���
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		PageFirst = (offset-1)*6
		PageLast = (offset-1)*6 + 6
		PageBoard = Notice_Board.objects.order_by('-id')[PageFirst:PageLast] #������ ���� ��� ���
	
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
			Next = offset +1 #������� ������ �ѱ�� ���
       
		return render_to_response("notice.html",
					  {'user':request.user, 
					   'PageBoard':PageBoard,
					   'TotalCount' : range(0,TotalCount), 
	       			   'Previous' : Previous, 
					   'Next' : Next} )

def Notice_Read(request, offset): #�������� �б� ���
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = Notice_Board.objects.filter(id=offset).get()
		
	
		return render_to_response("notice-contents.html", {'user':request.user, 'Board':Current})

def Main(request, offset): #�����Դϴ�.
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:

				try:
					offset = int(offset)
				except ValueError:
					raise Http404()
		

	
				
				
				PageInformation1 = request.session['PageInformation1'] #1���� ������ DB
				PageInformation2 = request.session['PageInformation2'] #2���� ������ DB
				PageInformation3 = request.session['PageInformation3'] #all ������ DB
				

				Active = ["","",""] #�������� �ִ� �ڹٽ�ũ��Ʈ on�Ұ����� �Ϸ��� ���� ����Ʈ

				URL_Path = request.path #������ �Ѱ��� �� �ش� �������� �����ֱ� ���� �����
				###
				if URL_Path.find("FirstMajorPage") != -1 :
					PageInformation1[1] = offset
					Active[0] = "active" #index.html�� ���� �� ������ �̿��ؼ� �ڹٽ�ũ��Ʈ ����
				elif URL_Path.find("SecondMajorPage") != -1:
					PageInformation2[1] = offset
					Active[1] = "active"
				else:
					PageInformation3[1] = offset
					Active[2] = "active"
				###������� �ڹٽ�ũ��Ʈ ���� �ϴ� ��
			
				##
				PageBoard1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP"))[(PageInformation1[1]-1)*6:(PageInformation1[1]-1)*6+6]
				PageBoard2 = Lecture.objects.filter(Code__contains = "SIE")[(PageInformation2[1]-1)*6:(PageInformation2[1]-1)*6+6]
				PageBoard3 = Lecture.objects.order_by('-id')[(PageInformation3[1]-1)*6:(PageInformation3[1]-1)*6+6]
				
				TotalCount1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP")).count()
				TotalCount2 =  Lecture.objects.filter(Code__contains = "SIE").count()
				TotalCount3 =  Lecture.objects.count()
				
				
			
				##���� ���� �� 
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
