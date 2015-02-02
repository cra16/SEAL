from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
def MyPage(request):
 # if request.user.username =="":
 #	return  HttpResponseRedirect("/mysite2")

  return render_to_response("sealmypage.html", {'user':request.user})

def About(request):
 
 return render_to_response("about.html",{'user':request.user})

def Schedule(request):
   
  return render_to_response("schedule.html",{'user':request.user})

def Judgement(request):
  return render_to_response("subscribe_report.html",{'user':request.user})

def Recommend(request):
  return render_to_response("recommend.html",{'user':request.user})

@csrf_exempt
def QnAMain(request):

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
  	return render_to_response("subscribe_faq.html",{'user':request.user})

def QnARead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	Current = QnA_Board.objects.filter(id=offset).get()
	
	
	return render_to_response("qna-contents.html", {'user':request.user, 'Board':Current})

def Course(request):
	
	return render_to_response("course.html", {'user':request.user})

def NoticeMain(request):
	if request.method =="POST":
		new_Text=request.POST['msg-body-txtarea']		
		new_TextWriter = request.user.username
		new_TextName = request.POST['msg-title-input']
		new_QnA = Notice_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
		new_QnA.save()

	count=Notice_Board.objects.count()

	TotalCount = (count/8)+1

	if TotalCount ==1:
		Next = 1
	else:
		Next =TotalCount
	Previous=1
	
	PageBoard = Notice_Board.objects.order_by('-id')[0:7]
	return render_to_response("notice.html",
				  {'user':request.user,
				   'PageBoard':PageBoard, 
				   'TotalCount' : range(0,TotalCount), 
				   'Previous' : Previous, 
				   'Next' : Next,
					})


def Notice(request, offset):
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
       
	return render_to_response("QnA.html",
				  {'user':request.user, 
				   'PageBoard':PageBoard,
				   'TotalCount' : range(0,TotalCount), 
				   'Previous' : Previous, 
				   'Next' : Next} )

def Notice_Read(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	Current = Notice_Board.objects.filter(id=offset).get()



	return render_to_response("notice-contents.html", {'user':request.user, 'Board':Current})


# Create your views here.
