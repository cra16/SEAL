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
		new_QnA = QnABoard(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
		new_QnA.save()

	count=QnABoard.objects.count()

	TotalCount = (count/8)+1
	
	PageBoard = QnABoard.objects.order_by('-id')[0:7]
	return render_to_response("QnA.html",{'user':request.user,'PageBoard':PageBoard, 'TotalCount' : range(0,TotalCount)})

def QnA(request,offset): 
	
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	PageFirst = (offset-1)*6+1
        PageLast = (offset-1)*6 + 7	
  	PageBoard = QnABoard.objects.order_by('-id')[PageFirst:PageLast]
	
	count = QnABoard.objects.count()
	TotalCount = (count/8)+1	

 	return render_to_response("QnA.html",{'user':request.user, 'PageBoard':PageBoard,'TotalCount' : range(0,TotalCount)} )

def QnAWrite(request):
  	return render_to_response("subscribe_faq.html",{'user':request.user})


# Create your views here.
