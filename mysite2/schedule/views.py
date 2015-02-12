# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from lecture.models import *

# 시간표 선택시 검색 기능
def SelectPeriod(request, period):
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:
		cur_semester = '14-2'
		lec_lst = Lecture.objects.filter(Semester=cur_semester, Period__contains=period)[0:6]
		ctx = {
			'user':request.user,
			'lec_lst':lec_lst
		}

		return render_to_response('schedule.html', ctx)