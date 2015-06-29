# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render

# Create your views here.

#세션 유지된 아이디 확인
def CheckingLogin(userID):
	if userID=="":
		return  HttpResponseRedirect("/mysite2");
	else:
		return True
#처음 그 페이지에 갔을 때 정보의 페이지 번호 보여줌
def FirstPageView(i,Count):
	PageInformation =[1,1,1]
	if Count[i]>11:
		PageInformation[0] = 1
		PageInformation[2] = 11
	else :
		PageInformation[0] = 1
		PageInformation[2] = Count[i]
	return PageInformation
#처음을 제외한 정보의 페이지 번호 보여줌
def CurrentPageView(T_Count,offset,i):
	PageInformation =[1,1,1]
	
	if T_Count[i] >11:
	#현재 페이지가 11이상일 경우
			if offset>11:
				#현재 페이지에서 +10을 했을 때 총페이지 보다 크면 마지막 next를 누르면 총페이지가 \
				#되도록 표현 
				if (offset+10)>T_Count[i]:
					PageInformation[0] = (offset -(offset%10))-9
					PageInformation[2] = T_Count[i]
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
			PageInformation[2] = T_Count[i]
	return PageInformation
#총 페이지 카운트
def PageTotalCount(i,T_Count,PageInformation):
	
	if (PageInformation[1]/10) >= T_Count[i]/10:
			TotalCount = range(PageInformation[1]-(PageInformation[1]%10)+1,T_Count[i]+1)
	else:
			TotalCount = range(PageInformation[1]-(PageInformation[1]%10)+1,PageInformation[1]-(PageInformation[1]%10)+11)
	
	return TotalCount

