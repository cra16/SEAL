# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from lecture.models import *


# 시간표 선택시 검색 기능
def SelectPeriod(request, period, page):
	"""
	period -> 테이블에서 선택한 강의시간
	page -> pagination에서 선택한 page
	"""
	if request.user.username =="":
		return HttpResponseRedirect("/mysite2")
	else:
		cur_page = int(page)
		# cur_page = request.session['cur_page']

		start = 6 * (cur_page-1)
		end = 6 * cur_page
		cur_semester = '14-2'	# 데이터가 많으므로 현재 학기만 가져오도록 한다.
		if period[1] == '1':	# 1교시의 경우 10교시가 같이 나오는 것을 방지하기 위한 장치
			lec_cnt = Lecture.objects.filter(Semester=cur_semester, Period__contains=period).exclude(Period__contains='10').count()
			lec_lst = Lecture.objects.filter(Semester=cur_semester, Period__contains=period).exclude(Period__contains='10')[start:end]
		else:
			lec_cnt = Lecture.objects.filter(Semester=cur_semester, Period__contains=period).count()
			lec_lst = Lecture.objects.filter(Semester=cur_semester, Period__contains=period)[start:end]
		total_page = ( (lec_cnt - 1) / 6 ) + 1
		is_odd = lec_cnt % 2
		ctx = {
			'user':request.user,
			'period':period,
			'total_page': range(1, total_page+1),
			'lec_lst':lec_lst,
			'is_odd':is_odd,
			'cur_page':cur_page
		}
		# request.session['cur_page'] = cur_page + 1

		return render_to_response('schedule.html', ctx)