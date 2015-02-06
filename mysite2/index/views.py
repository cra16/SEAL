from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q
def MyPage(request):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("sealmypage.html", {'user':request.user})

def About(request):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("about.html",{'user':request.user})

def Schedule(request):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("schedule.html",{'user':request.user})

def Judgement(request):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_report.html",{'user':request.user})

def Recommend(request):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("recommend.html",{'user':request.user})

@csrf_exempt
def QnAMain(request):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :
		if request.method =="POST":
			new_Text=request.POST['msg-body-txtarea']		
			new_TextWriter = request.user.username
			new_TextName = request.POST['msg-title-input']
			new_QnA = QnA_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
			new_QnA.save()

		count=QnA_Board.objects.count()

		TotalCount = (count/8)+1

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

def QnA(request,offset): 
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		PageFirst = (offset-1)*6
		PageLast = (offset-1)*6 + 6
		PageBoard = QnA_Board.objects.order_by('-id')[PageFirst:PageLast]
	
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
	
def QnAWrite(request):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		return render_to_response("subscribe_faq.html",{'user':request.user})

def QnARead(request, offset):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = QnA_Board.objects.filter(id=offset).get()
	
	
		return render_to_response("qna-contents.html", {'user':request.user, 'Board':Current})

def Course(request, offset):

	

	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except:
			raise Http404()


		if request.method =="POST":
				new_Text=request.POST['msg-body-:txtarea']
				new_TextWriter = request.user.username
				new_TextName = request.POST['msg-title-input']
				new_QnA = QnA_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
				new_QnA.save()
		else:
			CourseParent = Course_Evaluation.objects.filter(id=offset)
			CourseBoard = CourseParent.objects.order_by('created')[0:5]


			
			

				

def NoticeMain(request):
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

def Notice(request,offset):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		PageFirst = (offset-1)*6
		PageLast = (offset-1)*6 + 6
		PageBoard = Notice_Board.objects.order_by('-id')[PageFirst:PageLast]
	
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

def Notice_Read(request, offset):
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = Notice_Board.objects.filter(id=offset).get()
	
	
		return render_to_response("notice-contents.html", {'user':request.user, 'Board':Current})

def Main(request, offset):
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:

				try:
					offset = int(offset)
				except ValueError:
					raise Http404()
		

	
				
				
				PageInformation1 = request.session['PageInformation1']
				PageInformation2 = request.session['PageInformation2']
				PageInformation3 = request.session['PageInformation3']
				
				Active = ["","",""]

				URL_Path = request.path

				if URL_Path.find("FirstMajorPage") != -1 :
					PageInformation1[1] = offset
					Active[0] = "active"
				elif URL_Path.find("SecondMajorPage") != -1:
					PageInformation2[1] = offset
					Active[1] = "active"
				else:
					PageInformation3[1] = offset
					Active[2] = "active"

			

				PageBoard1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP"))[(PageInformation1[1]-1)*6:(PageInformation1[1]-1)*6+6]
				PageBoard2 = Lecture.objects.filter(Code__contains = "SIE")[(PageInformation2[1]-1)*6:(PageInformation2[1]-1)*6+6]
				PageBoard3 = Lecture.objects.order_by('-id')[(PageInformation3[1]-1)*6:(PageInformation3[1]-1)*6+6]
			
				TotalCount1 = Lecture.objects.filter(Q(Code__contains = "ECE") | Q(Code__contains ="ITP")).count()
				TotalCount2 =  Lecture.objects.filter(Code__contains = "SIE").count()
				TotalCount3 =  Lecture.objects.count()

				
			

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
