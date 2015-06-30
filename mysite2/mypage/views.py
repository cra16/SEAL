# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
from login.models import Profile
from functionhelper.views import CheckingLogin

# Create your views here.

@csrf_exempt
def MyPagePassWordChange(request):
		CheckingLogin(request.user.username)

		if request.method =="POST":
			ChangePassword = request.POST['PasswordBox']
			ProfileData = Profile.objects.get(User = request.user)
			
			#외래키는 저장이안되서 직접 해야 되네요. (솔직히 그냥 불러도되긴한데...)		
			UserData = ProfileData.User
			UserData.set_password(ChangePassword)
			UserData.save()

			return render_to_response("sealmypage.html", {'data':1})

		else:
			return render_to_response("sealmypage.html", {'data':0})