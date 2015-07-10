# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q #데이터 베이스 OR 기능 구현
from index.models import * #아직 시험중		
# Create your views here.

"""
전반적으로 해당 view에서 보이지 않는 모든 함수를 여기에 한곳에 모음
현재는 기능과 DB와 관련된 모든 함수가 섞여있는데 나중에 분류할 예정 7/6일 자
"""

#세션 유지된 아이디 확인
def CheckingLogin(userID):
	if userID=="":
		return  HttpResponseRedirect("/mysite2");
	else:
		return True
#최초로 페이지에 도달했을때 1전공 2전공 all의 페이지 위치 정보를 알려주는 기능
def FirstPageView(Count):
	PageInformation =[1,1,1]
	if Count>11:
		PageInformation[0] = 1
		PageInformation[1] = 1
		PageInformation[2] = 11
	else :
		PageInformation[0] = 1
		PageInformation[1] = 1
		PageInformation[2] = Count
	return PageInformation
#최초로 페이지 도달한 것을 제외한 모든 상황에서 1전공 2전공 all의 페이지 위치 정보 알려주는 기능
def CurrentPageView(T_Count,offset):
	PageInformation =[1,1,1]
	#페이지가 0으로 떨어질때 필요한 조건
	
	Condition =((offset%10) !=0 )and offset%10 or 10
	
	#Pagenation 하는 부분의 수가 11개 이상일 경우(즉 1,2,3,4,5,6.... 11일 경우 11,12,13...20으로 맞추기 위해 필요한 조건)
	if T_Count >=11:
	#현재 페이지가 11이상일 경우
			if offset>=11:
				#현재 페이지에서 +10을 했을 때 총페이지 보다 크면 마지막 next를 누르면 총페이지가 \
				#되도록 표현 
				if (offset+10)>=T_Count:
					PageInformation[0] = (offset -Condition)-9
					PageInformation[2] = T_Count
				#아니면 그냥 원래대로 표현
				else:
					PageInformation[0] = (offset -Condition)-9
					PageInformation[2] = (offset -Condition)+11
			#현재 페이지가 11이하일경우 
			else:
				PageInformation[0] = 1
				PageInformation[2] = (offset - Condition)+11
		#총 페이지가 11이하일 경우 
	else:
			PageInformation[0] = 1
			PageInformation[2] = T_Count
	return PageInformation
#PageNation하는 부분 표시하기 위한 기능
def PageTotalCount(T_Count,PageInformation):
	Codition = ((PageInformation[1]%10 !=0) and PageInformation[1]%10 or 10)
	if (PageInformation[1]/10) >= T_Count/10:
			TotalCount = range(PageInformation[1]- Codition+1,T_Count+1)
	else:
			TotalCount = range(PageInformation[1]-Codition+1,PageInformation[1]-Codition+11)
	return TotalCount


#Main Page 강의 추천하는 곳을 보여주는 기능
def MainPageView(user, pageinformation,PageNumber,MajorNumber):

	#login view에서 사용하는 MainPageView와 로그인 되었을때 mainPageView가 조금씩 달라서 설정
	if pageinformation !=None:
			User = user
			PageInformation=pageinformation
	else:
		User= user
		PageInformation=[[1,1,1],[1,1,1],[1,1,1]]
		PageNumber=1
		MajorNumber=0


	#user의 전공에 따른 전공 코드를 뿌려줌
	CourseCode = MajorSelect(User)
	
	#2차원 list로 각 전공당 총 페이지 수 저장
	T_Count=[[] ,[] ,[]]
	if CourseCode[0] !="ENG":
		DBCount1=Lecture.objects.filter(Q(Code__contains=CourseCode[0]) | Q(Code__contains= CourseCode[1])).count()
		DBCount2=Lecture.objects.filter(Q(Code__contains= CourseCode[2]) | Q(Code__contains=CourseCode[3])).count()
		T_Count[0] = DataCount(5,DBCount1)
		T_Count[1] = DataCount(5,DBCount2)
	else:
		DBCount1=Lecture.objects.filter(Q(Code__contains=CourseCode[0]) | Q(Code__contains= CourseCode[1]) | Q(Code__contains=CourseCode[2])| Q(Code__contains=CourseCode[3]) | Q(Code__contains=CourseCode[4]) | Q(Code__contains=CourseCode[5])).count()
		DBCount2=Lecture.objects.filter(Q(Code__contains=CourseCode[0]) | Q(Code__contains= CourseCode[1]) | Q(Code__contains=CourseCode[2])| Q(Code__contains=CourseCode[3]) | Q(Code__contains=CourseCode[4]) | Q(Code__contains=CourseCode[5])).count()
		T_Count[0] = DataCount(5,DBCount1)
		T_Count[1] = DataCount(5,DBCount2)
	DBCount3=Lecture.objects.count()
	T_Count[2] = DataCount(5,DBCount3)
	
	#현재 페이지 위치정보
	PageInformation[MajorNumber] = CurrentPageView(T_Count,PageNumber)
	PageInformation[MajorNumber][1] = PageNumber
	
	#각 강의 전공에 해당하는 DB 정보 저장 함 
	TotalBoard = [[],[],[]]
	if CourseCode[0] !="ENG":
		TotalBoard[0] = Lecture.objects.filter(Q(Code__contains = CourseCode[0]) | Q(Code__contains=CourseCode[1])).order_by('-Semester')[(PageInformation[0][1]-1)*5:(PageInformation[0][1]-1)*5+5]
		TotalBoard[1] = Lecture.objects.filter(Q(Code__contains = CourseCode[2]) | Q(Code__contains=CourseCode[3])).order_by('-Semester')[(PageInformation[1][1]-1)*5:(PageInformation[1][1]-1)*5+5]
	else:
		TotalBoard[0] = Lecture.objects.filter(Q(Code__contains =CourseCode[0]) |Q(Code__contains=CourseCode[1])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('-Semester')[(PageInformation[0][1]-1)*5:(PageInformation[0][1]-1)*5+5]
		TotalBoard[1] = Lecture.objects.filter(Q(Code__contains =CourseCode[2]) |Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('-Semester')[(PageInformation[1][1]-1)*5:(PageInformation[1][1]-1)*5+5]
	TotalBoard[2] = Lecture.objects.order_by('-Semester')[(PageInformation[2][1]-1)*5:(PageInformation[2][1]-1)*5+5]

	#페이지에 나타나는 강의 추천된 Board를 평균에 맞춰서 계산
	PageBoard = PageView(TotalBoard)
	##Session Save
	

	# 페이지 총 수(페이지 넘길 때)
	TotalCount=list()
	for i in range(0,len(T_Count)):
		TotalCount.append(PageTotalCount(T_Count[i],PageInformation[i]))
	#추천많이받은 순으로 보여주는 Board
	BestBoard = BestBoardView()

	dic = {'user':User,
		   'PageBoard':PageBoard,
		   'TotalCount' : TotalCount,
		   'PageInformation' : PageInformation,
		   'T_Count':T_Count,
		   'Page':PageNumber,
		   'BestBoard':BestBoard
		   }

	return dic
#MainPage Template설정
def TargetTemplate(Current):
	target = ["",""]
	if Current =="FirstPageNation":
		target[0] = "FirstMajorPage.html"
		target[1] = "0"
	elif Current =="SecondPageNation":
		target[0] = "SecondPage.html"
		target[1] ="1"
	else:
		target[0] = "AllPage.html"
		target[1] = "2"
	return target

#전공 코드 쏘는 기능
def MajorSelect(user):
		try:
			Student = Profile.objects.get(User =user)
		except:
			return None
		MajorCode= [[],[],[],[],[],[]]	
		FirstMajor = str(Student.FirstMajor)
		SecondMajor = str(Student.SecondMajor)
			#1전공 선택 하는 조건문
		if FirstMajor.find("국제") != -1 or FirstMajor.find("영어") != -1:
			MajorCode[0]="ISE"
			MajorCode[1]="None"
		elif FirstMajor.find("경영학") != -1 or FirstMajor.find("경제학")!= -1:
			MajorCode[0]="GMP"
			MajorCode[1]="MEC"
		elif FirstMajor.find("한국법") != -1 or FirstMajor.find("UIL")!= -1:
			MajorCode[0]="LAW"
			MajorCode[1]="UIL"
		elif FirstMajor.find("공연영상")!= -1 or FirstMajor.find("언로정보학")!= -1:
			MajorCode[0]="CCC"
			MajorCode[1]="None"
		elif FirstMajor.find("건설공학") != -1 or FirstMajor.find("도시환경")!= -1:
			MajorCode[0]="CUE"
			MajorCode[1]="None"
		elif FirstMajor.find("기계공학")!= -1 or FirstMajor.find("전자제어")!= -1 or FirstMajor.find("기전공학")!=-1:
			MajorCode[0]="HMM"
			MajorCode[1]="None"
		elif FirstMajor.find("시각디자인")!= -1 or FirstMajor.find("제품디자인")!= -1:
			MajorCode[0]="IID"
			MajorCode[1]="None"
		elif FirstMajor.find("생명과학")!= -1:
			MajorCode[0]="BFT"
			MajorCode[1]="None"
		elif FirstMajor.find("컴퓨터") != -1 or FirstMajor.find("전자") != -1:
			MajorCode[0]="ECE"
			MajorCode[1]="ITP"
		elif FirstMajor.find("상담심리") != -1 or FirstMajor.find("사회복지")!= -1:
			MajorCode[0]="CSW"
			MajorCode[1]="None"
		elif FirstMajor.find("에디슨")!= -1 :
			MajorCode[0]="GEA"
			MajorCode[1]="None"
		elif FirstMajor.find("영어학과")!= -1 or FirstMajor.find("경영학과")!= -1 or FirstMajor.find("사회복지학과")!= -1:
			MajorCode[0]="SIE"
			MajorCode[1]="None"
		elif FirstMajor==None :
			MajorCode[2]="None"
			MajorCode[3]="None"
			MajorCode[4]="None"
			MajorCode[5]="None"
		else:
			MajorCode[0]="ENG"
			MajorCode[1]="GEK"
			MajorCode[2]="GCS"
			MajorCode[3]="PCO"
			MajorCode[4]="ISL"
			MajorCode[5]="PST"

		if SecondMajor.find("국제")!=-1 or SecondMajor.find("영어")!=-1:
			MajorCode[2]="ISE"
			MajorCode[3]="None"
		elif SecondMajor.find("경영학")!=-1 or SecondMajor.find("경제학")!=-1:
			MajorCode[2]="GMP"
			MajorCode[3]="MEC"
		elif SecondMajor.find("한국법")!=-1 or SecondMajor.find("UIL")!=-1:
			MajorCode[2]="LAW"
			MajorCode[3]="UIL"
		elif SecondMajor.find("공연영상") !=-1 or SecondMajor.find("언로정보학")!=-1:
			MajorCode[2]="CCC"
			MajorCode[3]="None"
		elif SecondMajor.find("건설공학") !=-1 or SecondMajor.find("도시환경")!=-1:
			MajorCode[2]="CUE"
			MajorCode[3]="None"
		elif SecondMajor.find("기계공학")!=-1 or SecondMajor.find("전자제어")!=-1 or SecondMajor.find("기전공학")!=-1:
			MajorCode[2]="HMM"
			MajorCode[3]="None"
		elif SecondMajor.find("시각디자인")!=-1 or SecondMajor.find("제품디자인")!=-1:
			MajorCode[2]="IID"
			MajorCode[3]="None"
		elif SecondMajor.find("생명과학")!=-1:
			MajorCode[2]="BFT"
			MajorCode[3]="None"
		elif SecondMajor.find("컴퓨터")!=-1 or SecondMajor.find("전자")!=-1:
			MajorCode[2]="ECE"
			MajorCode[3]="ITP"
		elif SecondMajor.find("상담심리")!=-1 or SecondMajor.find("사회복지")!=-1:
			MajorCode[2]="CSW"
			MajorCode[3]="None"
		elif SecondMajor.find("에디슨")!=-1:
			MajorCode[2]="GEA"
			MajorCode[3]="None"
		elif SecondMajor.find("영어학과") !=-1 or SecondMajor.find("경영학과") !=-1 or SecondMajor.find("사회복지학과")!=-1:
			MajorCode[2]="SIE"
			MajorCode[3]="None"
		elif SecondMajor==None :
			MajorCode[2]="None"
			MajorCode[3]="None"
			MajorCode[4]="None"
			MajorCode[5]="None"
		else:
			MajorCode[2]="GCS"
			MajorCode[3]="PCO"
			MajorCode[4]="ISL"
			MajorCode[5]="PST"
		return MajorCode



#강의 추천 평균 계산
def PageView(TotalBoard):
	PageBoard=[[],[],[]]
	count =0
	
	for DBBoard in TotalBoard:
		for Board in DBBoard:
			try:
				# 총 강의 추천된 DB 강의 명으로 호출
				BoardData = Total_Evaluation.objects.get(Course=Board)
			except :
				BoardData = None

			if BoardData is not None:
				BoardData.Total_Speedy = BoardData.Total_Speedy/BoardData.Total_Count
				BoardData.Total_Reliance = BoardData.Total_Reliance/BoardData.Total_Count
				BoardData.Total_Helper = BoardData.Total_Helper/BoardData.Total_Count
				BoardData.Total_Question = BoardData.Total_Question/BoardData.Total_Count
				BoardData.Total_Exam = BoardData.Total_Exam/BoardData.Total_Count
				BoardData.Total_Homework = BoardData.Total_Homework/BoardData.Total_Count
				PageBoard[count].append(BoardData)
			else:
				BoardData = Total_Evaluation(Course=Board)
				BoardData.Total_Speedy =5
				BoardData.Total_Reliance =5
				BoardData.Total_Helper = 5
				BoardData.Total_Question = 5
				BoardData.Total_Exam = 5
				BoardData.Total_Homework = 5
				BoardData.Total_Count =0
				PageBoard[count].append(BoardData)
		count=count+1
	return PageBoard

#DB에서 호출 된 모든 정보에 대한 페이지 총 개수를 계산하는 기능
def DataCount(divide, DataBaseCount):


        DBCount = DataBaseCount
        Condition = (DBCount%divide!=0) and 1 or 0
        Count=DBCount/divide+Condition
        return Count
#가장 추천많이 받은 강의 보여주는 기능
def BestBoardView():
	TotalBoard = Total_Evaluation.objects.all()
	MaxCount = 0  
	SecondCount = 0
	ThirdCount =0
	BestBoard =[0,0,0]
	for Board in TotalBoard:
		if Board.Total_Count>MaxCount:
			MaxCount=Board.Total_Count
			BestBoard[0] = Board
		elif Board.Total_Count>SecondCount:
			SecondCount=Board.Total_Count
			BestBoard[1] = Board
		elif Board.Total_Count >ThirdCount:
			ThirdCount=Board.Total_Count
			BestBoard[2] = Board

	return BestBoard