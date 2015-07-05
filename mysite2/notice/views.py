# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from login.models import *
from notice.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime  #오늘날짜 불러오기 위한 import
from django.db.models import Q
from functionhelper.views import *


def NoticeMain(request):#Notice 기능

	CheckingLogin(request.user.username)
	
	count=Notice_Board.objects.count()
	T_Count=[1]
	T_Count[0] = (count/8)+1 #총 페이지수(아마 고쳐야할듯)
	
	PageInformation=(FirstPageView(0,T_Count))
	PageBoard = Notice_Board.objects.order_by('-id')[0:7]	
	Today = datetime.datetime.now()
	return render_to_response("notice.html",
				  {'user':request.user,
				   'PageBoard':PageBoard, 
				   'PageInformation':PageInformation,
				   'TotalCount' : range(1,PageInformation[2]+1),
				   'Today':Today 
				   })
@csrf_exempt
def Notice(request): #Notice Page 넘겨졌을때 나오는 페이지

	CheckingLogin(request.user.username)
	try:
		offset = int(request.POST['Page'])
	except ValueError:
		raise Http404()

	#페이지 수 정보
	PageFirst = (offset-1)*6
	PageLast = (offset-1)*6 + 6
	PageBoard = Notice_Board.objects.order_by('-id')[PageFirst:PageLast] 
	#페이지 넘기는 기능

	count = Notice_Board.objects.count()
	T_Count=list()
	T_Count.append((count/8)+1)
	

	PageInformation=CurrentPageView(T_Count,offset,0)


	TotalCount = PageTotalCount(0,T_Count,PageInformation)

	Today =datetime.date.today()    
	return render_to_response("NoticeList.html",
				  {'user':request.user, 
				   'PageBoard':PageBoard,
				   'TotalCount' : TotalCount,
				   'Today' :Today,
				   'PageInformation':PageInformation
       			  })

def Notice_Read(request, offset): #Notice Read 기능
	CheckingLogin(request.user.username)
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	Current = Notice_Board.objects.filter(id=offset).get()
	Current.ClickScore +=1
	Current.save()

	NoticeCount = Notice_Board.objects.count()

	if offset ==1:
		Previous = 1
	else:
		Previous = offset-1
	if offset == NoticeCount:
		Next = NoticeCount
	else:
		Next = offset+1
	

	return render_to_response("notice-contents.html", 
		{'user':request.user,
		'Previous' :Previous,
		'Next' :Next,
		'Board':Current})


def Notice_Write(request): #Q&A Write 기능
	CheckingLogin(request.user.username)
	return render_to_response("subscribe_notice.html",{'user':request.user})
@csrf_exempt
def Notice_Writing(request):
	CheckingLogin(request.user.username)
	if request.method =="POST":
		new_Text=request.POST['msg-body-txtarea']		
		new_TextWriter = Profile.objects.get(User=request.user)
		new_TextName = request.POST['msg-title-input']
		created = datetime.datetime.now()
		new_Notice = Notice_Board(Text=new_Text, TextWriter = new_TextWriter, TextName=new_TextName)
		new_Notice.save()
	return HttpResponseRedirect("/mysite2/Notice")
# Create your views here.
