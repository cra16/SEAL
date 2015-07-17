# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from login.models import *
from qna.models import *	
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models import Q
from functionhelper.views import *


def QnAMain(request): #Q&A 메인 
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	count=QnA_Board.objects.count()

	PageFirst=0
	PageLast =8
	
	T_Count = DataCount(8,count)#총 페이지수(아마 고쳐야할듯)
	
	PageInformation=(FirstPageView(T_Count))

	TotalCount=PageTotalCount(T_Count,PageInformation)

	Today = datetime.datetime.today()
	
	PageBoard=(QnA_Board.objects.order_by('-id')[PageFirst:PageLast])
	
	Reply_Board=[]#reply DB 저장할 공간

	for Board in PageBoard:
			#QnA 글에 맞춰서 reply 글도 그 QnA 고유 ID기준으로 reply 데이터 불러옴
			Reply_Board.append(Reply.objects.filter(QuestionID = int(Board.id)))
		#except:
		#Reply_Board=None
	return render_to_response("QnA.html",
				  {'user':request.user,
				  'BestBoard':BestBoardView(),
				   'PageBoard':PageBoard,
				   'ReplyBoard':Reply_Board,
				   'TotalCount' : TotalCount, 
				   'PageInformation' : PageInformation,
				   'Today' : Today,
				   })

@csrf_exempt		
def QnA(request): #Q&A 페이지로 넘겼을때 나오는 기능

	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	try:
		offset = int(request.POST['Page'])
	except ValueError:
		raise Http404()

	#페이지 총 수
	PageFirst = (offset-1)*8
	PageLast = (offset-1)*8 + 8
	PageBoard = QnA_Board.objects.order_by('-id')[PageFirst:PageLast]
	#######	게시판 페이지 넘기는 기능

	count = QnA_Board.objects.count()
	
	T_Count=DataCount(8,count)
	#PageInformation = list()
    
	PageInformation=CurrentPageView(T_Count,offset)


	TotalCount=PageTotalCount(T_Count,PageInformation)

	Today =datetime.date.today()

	for Board in PageBoard:
			#QnA 글에 맞춰서 reply 글도 그 QnA 고유 ID기준으로 reply 데이터 불러옴
			Reply_Board=Reply.objects.filter(QuestionID = int(Board.id))

	return render_to_response("QnAList.html",
				  {'user':request.user, 
				  'BestBoard':BestBoardView(),
				   'PageBoard':PageBoard, 	
				   'TotalCount' : TotalCount, 
       			   'PageInformation' : PageInformation,
					'Today' : Today,
					'ReplyBoard':Reply_Board,
				   } )
	
def QnAWrite(request): #Q&A Write 기능
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	return render_to_response("subscribe_faq.html",{'user':request.user, 'BestBoard':BestBoardView()})
@csrf_exempt
def QnA_Writing(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	if request.method =="POST":
		new_Text=request.POST['msg-body-txtarea']		
		new_TextWriter = Profile.objects.get(User=request.user)
		new_TextName = request.POST['msg-title-input']
		created = datetime.datetime.now()
		new_QnA = QnA_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
		new_QnA.save()
	return HttpResponseRedirect("/mysite2/QnA")
def QnARead(request, offset): #Q&A read 기능
		if CheckingLogin(request.user.username):
				return HttpResponseRedirect("/mysite2")
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()


		Current = QnA_Board.objects.filter().get(id=offset) #고유 id로 글 정렬
		Current.ClickScore +=1
		Current.save()

		QnACount = QnA_Board.objects.count()
		if offset ==1:
			Previous = 1
		else:
			Previous = offset-1
		if offset == QnACount:
			Next = QnACount
		else:
			Next = offset+1

		try:
			QnA_Reply = Reply.objects.filter(QuestionID = Current.id)
		except:
			QnA_Reply =None
	
		return render_to_response("qna-contents.html", 
			{'user':request.user, 
			'Current':Current, 
			'QnA_Reply' : QnA_Reply,
			'Previous' : Previous,
			'Next':Next})

def QnA_Reply(request, offset): 
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	return render_to_response("subscribe_reply.html",{'user':request.user, 'ID':offset})
@csrf_exempt
def QnA_Replying(request,offset):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/mysite2")
	if request.method =="POST":
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		Current = QnA_Board.objects.filter(id=offset).get()

	
		new_Text=request.POST['msg-body-txtarea2']		
		new_TextWriter = Profile.objects.get(User=request.user)
		new_TextName = request.POST['msg-title-input2']
		created = datetime.datetime.now()
		Question_ID = Current.id
		new_QnAReply = Reply(QuestionID= Question_ID,TextWriter = new_TextWriter, Text=new_Text, TextName=new_TextName)
		new_QnAReply.save()
	return HttpResponseRedirect("/mysite2/QnA")

# Create your views here.
		