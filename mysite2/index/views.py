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
def MyPage(request):	#MyPage 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("sealmypage.html", {'user':request.user}) 

def About(request): #About template ·çÆ®
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("about.html",{'user':request.user})

def Schedule(request): #Schedule template ·çÆ®
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("schedule.html",{'user':request.user})

def Judgement(request): # »ç¿ëÀÚ ½Å°í template ·çÆ®
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_report.html",{'user':request.user})

@csrf_exempt
def Recommend(request, offset): #ÃßÃµ °­ÀÇ ½ºÅ©·Ñ template º¸¿©ÁÖ´Â ·çÆ®
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except:
			raise Http404()


		
		CourseBoard = Lecture.objects.get(id=offset) #DB °íÀ¯ ID·Î Á¢±ÙÇØ¼­ °Ë»ö		
		request.session['Recommend_ID'] = offset #offset ¹Ì¸® ÀúÀå
		return render_to_response("recommend.html",
                                          {'user':request.user,
                                           'CourseBoard':CourseBoard,
                                         #  'TotalCount' : range(0,TotalCount)
											})
@csrf_exempt
def Recommend_Write(request): #ÃßÃµ °­ÀÇ DBÀÔ·Â
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


                        L_Eval = Lecture.objects.get(id=request.session['Recommend_ID'])#session¿¡ ÀúÀåµÈ ID¸¦ ÅëÇØ °­ÀÇ Á¤º¸ °®°í¿À±â

                        try:
                                T_Eval=Total_Evaluation.objects.get(CourseName=L_Eval)#°­ÀÇ Á¤º¸ DB·Î °£Á¢ Á¢±ÙÇØ¼­ Total °ª °Ë»ö

                        except:
                                T_Eval =None 


                        if T_Eval is None: #µ¥ÀÌÅÍ ¾øÀ»½Ã Table »ý¼º
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
def QnAMain(request): #Q&A ºÎºÐ Á¶ÀÛ(Á» ¼ÕºÁ¾ßÇÔ)
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :
		#¹ÞÀº Á¤º¸ ÀúÀå(ÀÌ°Íµµ ¿Å±æ ¿¹Á¤ ´Ù³¡³ª¸é..)
		if request.method =="POST":
			new_Text=request.POST['msg-body-txtarea']		
			new_TextWriter = request.user.username
			new_TextName = request.POST['msg-title-input']
			new_QnA = QnA_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
			new_QnA.save()
		#ÆäÀÌÁö ³Ñ±â´Â ±â´É
		count=QnA_Board.objects.count()
		TotalCount = (count/8)+1 #ÆäÀÌÁö ¼ö

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

def QnA(request,offset): #ÆäÀÌÁö ÀÌµ¿½Ã Á¤º¸ º¸¿©ÁÖ´Â °÷
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		#ÆäÀÌÁö ¼ö Á¤º¸
		PageFirst = (offset-1)*6 
		PageLast = (offset-1)*6 + 6
		PageBoard = QnA_Board.objects.order_by('-id')[PageFirst:PageLast]
		#######	ÆäÀÌÁö ³Ñ±â´Â ±â´É
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
	
def QnAWrite(request): #Q&A Write ±â´É
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_faq.html",{'user':request.user})

def QnARead(request, offset): #Q&A read ±â´É
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = QnA_Board.objects.filter(id=offset).get() #id¸¦ ±âÁØÀ¸·Î È£ÃâÇÔ
	
	
		return render_to_response("qna-contents.html", {'user':request.user, 'Board':Current})

def Course(request, offset): #¼±ÅÃµÈ °­ÀÇ ÃßÃµ ÀüÃ¼ ¸ñ·Ï ±â´É

	#°­ÀÇ ÃßÃµ½Ã ±ÇÇÑ ¾ÆÁ÷ ¾ÈÁÜ

	if request.user.username =="":
                return  HttpResponseRedirect("/mysite2")
        else:
                try:
                        offset = int(offset)
                except:
                        raise Http404()

				
				#ÇØ´ç °­ÀÇ ÀüÃ¼ ÃßÃµ Æò±Õ ½ºÅ©·Ñ º¸¿©ÁÖ´Â ±â´É
				CourseBoard = Total_Evaluation.objects.get(CourseName = Lecture.objects.get(id = offset))
                CourseBoard.Total_Speedy = CourseBoard.Total_Speedy/CourseBoard.Total_Count
                CourseBoard.Total_Reliance = CourseBoard.Total_Reliance/CourseBoard.Total_Count
                CourseBoard.Total_Helper = CourseBoard.Total_Helper/CourseBoard.Total_Count
                CourseBoard.Total_Question = CourseBoard.Total_Question/CourseBoard.Total_Count
                CourseBoard.Total_Exam = CourseBoard.Total_Exam/CourseBoard.Total_Count
                CourseBoard.Total_Homework = CourseBoard.Total_Homework/CourseBoard.Total_Count
				
				#·Î±×ÀÎ ´ç»çÀÚ°¡ ÃßÃµ ÇÑ ½ºÅ©·Ñ º¸¿©ÁÖ´Â ±â´É
                MyCourseBoard = Course_Evaluation.objects.get(CreatedID = Profile.objects.get(User=request.user))
				#´Ù¸¥ »ç¶÷µéÀÌ ÇØ³õÀº °Í ½Ã°£¼øÀ¸·Î º¸¿©ÁØ ±â´É
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





			
			

				

def NoticeMain(request):#Notice ¸ÞÀÎ ±â´É
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

def Notice(request,offset): #Notice Page ³Ñ±â±â ±â´É
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		#ÆäÀÌÁö ¼ö Á¤º¸
		PageFirst = (offset-1)*6
		PageLast = (offset-1)*6 + 6
		PageBoard = Notice_Board.objects.order_by('-id')[PageFirst:PageLast] 
		#ÆäÀÌÁö ³Ñ±â´Â ±â´É
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

def Notice_Read(request, offset): #Notice Read ±â´É
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = Notice_Board.objects.filter(id=offset).get()
		
	
		return render_to_response("notice-contents.html", {'user':request.user, 'Board':Current})

def Main(request, offset): #Main ±â´É
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
				

				#main ÀÚ¹Ù½ºÅ©¸³Æ® Á¶ÀÛ ÇÏ±â À§ÇÑ ±â´É
				Active = ["","",""]

				URL_Path = request.path	#ÇöÀç ÆäÀÌÁö URL ±Ü¾î¿À±â
				
				if URL_Path.find("FirstMajorPage") != -1 :
					PageInformation1[1] = offset
					Active[0] = "active" #
				elif URL_Path.find("SecondMajorPage") != -1:
					PageInformation2[1] = offset
					Active[1] = "active"
				else:
					PageInformation3[1] = offset
					Active[2] = "active"
			
				##°­ÀÇ DB¿¡ ÀúÀåµÈ ÀÚ·áµéÀ» ÄÚµå·Î ÇÊÅÍ¸¦ ÇØ¼­ Total Page¸¦ ¸¸µê
				##±×¸®°í ³ª¼­ °­ÀÇÃßÃµµÈ °­ÀÇµé¸¸ µû·Î ¶Ç ÇÊÅÍÇØ¼­ µ¥ÀÌÅÍ ³Ö´Â °úÁ¤ÀÓ
				##´Ù¸¥ °³¹ßÀÚºÐÀÌ Á» ¾Ë°í¸®Áò ÀßÂ¥¼­ ´õ ÃÖÀûÈ­ÇØÁÖ¼¼¿ä..(¹ßÀûÈ­ÀÓ..))
				PageBoard1 =[]
				PageBoard2 =[]
				
				TotalBoard1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP"))[(PageInformation1[1]-1)*6:(PageInformation1[1]-1)*6+6]
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
						PageBoard1.append(Board1)
					else:
						Board1 = Total_Evaluation(CourseName=Board)
						Board1.Total_Speedy =5
						Board1.Total_Reliance =5
						Board1.Total_Helper = 5
						Board1.Total_Question = 5
						Board1.Total_Exam = 5
						Board1.Total_Homework = 5
						Board1.Total_Count =1
						PageBoard1.append(Board1)
				TotalBoard2 = Lecture.objects.filter(Code__contains = "SIE")[(PageInformation2[1]-1)*6:(PageInformation2[1]-1)*6+6]
				for Board in TotalBoard2:
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
						PageBoard1.append(Board1)
					else:
						Board1 = Total_Evaluation(CourseName=Board)
						Board1.Total_Speedy =5
						Board1.Total_Reliance =5
						Board1.Total_Helper = 5
						Board1.Total_Question = 5
						Board1.Total_Exam = 5
						Board1.Total_Homework = 5
						Board1.Total_Count =1
						PageBoard1.append(Board1)
                PageBoard3 = Lecture.objects.order_by('-id')[(PageInformation3[1]-1)*6:(PageInformation3[1]-1)*6+6]

				
				
			
				##Session Save
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
