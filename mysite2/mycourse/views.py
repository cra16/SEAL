# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from index.models import *
from lecture.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime

def MyCourse(request):
        if request.user.username =="":
                return HttpResponseRedirect("/mysite2")
        else:
			MyProfile = Profile.objects.get(User=request.user)
			PageInformation1 = [1,1,1]
			PageInformation2 = [1,1,1]
			RecommendPage=[]
			LikePage=[]
			
			RecommendPage = Recommend_Course.objects.filter(CreatedID = MyProfile)[0:5]
			R_Count = Recommend_Course.objects.filter(CreatedID = MyProfile).count()/6+1
			
			LikePage=Like_Course.objects.filter(CreatedID = MyProfile)[0:5]
			L_Count=Like_Course.objects.filter(CreatedID = MyProfile).count()/6+1
				
			if R_Count>11:
				PageInformation1[0] = 1
				PageInformation1[2] = 11
			else :
				PageInformation1[0] = 1
				PageInformation1[2] = R_Count
			if L_Count>11:
				PageInformation2[0] =1
				PageInformation2[2] =11
			else:
				PageInformation2[0]= 1
				PageInformation2[2]= L_Count




			return render_to_response("mycourses.html", {'user':request.user, 
														'RecommendPage':RecommendPage,
														'PageInformation1' : PageInformation1,
														'PageInformation2' : PageInformation2,
														})
#def MyCoursePage(request, offset)



# Create your views here.
