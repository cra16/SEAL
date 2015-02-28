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
from datetime import date #오늘날짜 불러오기 위한 import
from django.db.models import Q



def NoticeMain(request):#Notice 기능

	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		count=Notice_Board.objects.count()

		T_Count = (count/8)+1 #총 페이지수(아마 고쳐야할듯)
		PageInformation = [1,1,1]
		
		if T_Count>11:
			PageInformation[2] = 11
		else:
			PageInformation[2] =T_Count
		
		PageBoard = Notice_Board.objects.order_by('-id')[0:7]	
		Today = date.today()
		return render_to_response("notice.html",
					  {'user':request.user,
					   'PageBoard':PageBoard, 
					   'TotalCount' : range(0,PageInformation[2]),
					   'Today':Today 
					   })

def Notice(request,offset): #Notice Page 넘겨졌을때 나오는 페이지

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


		count = Notice_Board.objects.count()
		TotalCount = (count/8)+1
		PageInformation = [1,1,1]
        
		if TotalCount >11:
			#현재 페이지가 11이상일 경우
			if offset>11:
				#현재 페이지에서 +10을 했을 때 총페이지 보다 크면 마지막 next를 누르면 총페이지가 \
				#되도록 표현 
				if (offset+10)>T_Count[i]:
					PageInformation[0] = (offset -(offset%10))-9
					PageInformation[2] = TotalCount
				#아니면 그냥 원래대로 표현
				else:
					PageInformation[0] = (offset -(offset%10))-9
					PageInformation[2] = (offset -(offset%10))+11
			#현재 페이지가 11이하일경우 
			else:
				PageInformation[0] = 1
				PageInformation[2] = (offset - (offset%10))+11
		#총 페이지가 11이하일 경우 
		else:
			PageInformation[0] = 1	
			PageInformation[2] = TotalCount

		if (PageInformation[1]/10) >= TotalCount/10:
			TotalCount = range(PageInformation[1]-(PageInformation[1]%10)+1,TotalCount+1)
		else:
			TotalCount = range(PageInformation[1]-(PageInformation[1]%10)+1,PageInformation[1]-(PageInformation[1]%10)+11)
       

		Today = date.today()       
		return render_to_response("notice.html",
					  {'user':request.user, 
					   'PageBoard':PageBoard,
					   'TotalCount' : TotalCount,
					   'Today' :Today,
	       			  })

def Notice_Read(request, offset): #Notice Read 기능
	if request.user.username =="":
		return  HttpResponseRedirect("/mysite2")
	else:
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()

		Current = Notice_Board.objects.filter(id=offset).get()
		Current.ClickScore +=1
		Current.save()
		
	
		return render_to_response("notice-contents.html", {'user':request.user, 'Board':Current})

# Create your views here.
