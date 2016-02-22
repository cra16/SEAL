# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from login.models import Profile
from functionhelper.views import CheckingLogin

# Create your views here.
#암호 바꾸기
@csrf_exempt
def NicknameChange(request):
	if CheckingLogin(request.user.username):
		return HttpResponseRedirect("/")

		if request.method =="POST":
			nickname = request.POST['Nickname']
			myprofile = Profile.objects.get(User = request.user)
			is_same = Profile.objects.filter(UserName = nickname)
			# if len(is_same) > 0:	# 중복 여부 검사
			# 	return render_to_response('html/sealmypage.html')

			myprofile.update(UserName = nickname)
			if request.flavour =='full':
				return render_to_response('html/sealmypage.html')
			else:	
				return render_to_response("m_skins/m_html/sealmypage.html")

		else:
			if request.flavour =='full':
				return render_to_response('html/sealmypage.html')
			else:
				return render_to_response("m_skins/m_html/sealmypage.html")
