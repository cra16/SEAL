from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from login.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q
def QnAMain(request): #Q&A 메인 
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :
		if request.method =="POST":
			new_Text=request.POST['msg-body-txtarea']		
			new_TextWriter = request.user.username
			new_TextName = request.POST['msg-title-input']
			new_QnA = QnA_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
			new_QnA.save()
		#페이지 넘기는 기능
		count=QnA_Board.objects.count()

		TotalCount = (count/8)+1 #총 페이지수(아마 고쳐야할듯)

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


def QnA(request,offset): #Q&A 페이지로 넘겼을때 나오는 기능

	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else :	
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		#페이지 총 수
		PageFirst = (offset-1)*6 
		PageLast = (offset-1)*6 + 6
		PageBoard = QnA_Board.objects.order_by('-id')[PageFirst:PageLast]
		#######	게시판 페이지 넘기는 기능

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


		Current = QnA_Board.objects.filter(id=offset).get() #고유 id로 글 정렬

	
		return render_to_response("qna-contents.html", {'user':request.user, 'Board':Current})

# Create your views here.
