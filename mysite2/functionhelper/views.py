# -*- coding: utf-8 -*-
# -*- coding: euc-kr -*-

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q #데이터 베이스 OR 기능 구현
from index.models import * #아직 시험중		
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
		PageInformation[1] = 1
		PageInformation[2] = 11
	else :
		PageInformation[0] = 1
		PageInformation[1] = 1
		PageInformation[2] = Count[i]
	return PageInformation
#처음을 제외한 정보의 페이지 번호 보여줌
def CurrentPageView(T_Count,offset,i):
	PageInformation =[1,1,1]
	Condition =((offset%10) !=0 )and offset%10 or 10
	
	if T_Count[i] >=11:
	#현재 페이지가 11이상일 경우
			if offset>=11:
				#현재 페이지에서 +10을 했을 때 총페이지 보다 크면 마지막 next를 누르면 총페이지가 \
				#되도록 표현 
				if (offset+10)>=T_Count[i]:
					PageInformation[0] = (offset -Condition)-9
					PageInformation[2] = T_Count[i]
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
			PageInformation[2] = T_Count[i]
	return PageInformation
#총 페이지 카운트
def PageTotalCount(i,T_Count,PageInformation):
	Codition = ((PageInformation[1]%10 !=0) and PageInformation[1]%10 or 10)
	if (PageInformation[1]/10) >= T_Count[i]/10:
			TotalCount = range(PageInformation[1]- Codition+1,T_Count[i]+1)
	else:
			TotalCount = range(PageInformation[1]-Codition+1,PageInformation[1]-Codition+11)
	
	return TotalCount



def MainPageView(user, pageinformation,PageNumber,MajorNumber):

	User = user
	PageInformation=pageinformation
	#main 자바스크립트 조작 하기 위한 기능
	

	##강의 DB에 저장된 자료들을 코드로 필터를 해서 Total Page를 만듦
	##그리고 나서 강의추천된 강의들만 따로 또 필터해서 데이터 넣는 과정임
	##후배여러분이 좀 알고리즘 잘짜서 더 최적화해주세요..(최대한 했지만..발적화임..))
	
	CourseCode = MajorSelect(User)
	
	#2차원 list로 각 전공당 총 페이지 수 저장
	T_Count=[[] ,[] ,[]]
	if CourseCode[0] !="ENG":
		DBCount1=Lecture.objects.filter(Q(Code__contains=CourseCode[0]) | Q(Code__contains= CourseCode[1])).count()
		DBCount2=Lecture.objects.filter(Q(Code__contains= CourseCode[2]) | Q(Code__contains=CourseCode[3])).count()
		Condition1= (DBCount1%5!=0) and 1 or 0
		Condition2= (DBCount2%5!=0) and 1 or 0
		T_Count[0] = DBCount1/5+Condition1
		T_Count[1] = DBCount2/5+Condition2
	else:
		DBCount1=Lecture.objects.filter(Q(Code__contains=CourseCode[0]) | Q(Code__contains= CourseCode[1]) | Q(Code__contains=CourseCode[2])| Q(Code__contains=CourseCode[3]) | Q(Code__contains=CourseCode[4]) | Q(Code__contains=CourseCode[5])).count()
		DBCount2=Lecture.objects.filter(Q(Code__contains=CourseCode[0]) | Q(Code__contains= CourseCode[1]) | Q(Code__contains=CourseCode[2])| Q(Code__contains=CourseCode[3]) | Q(Code__contains=CourseCode[4]) | Q(Code__contains=CourseCode[5])).count()
		Condition1= (DBCount1%5!=0) and 1 or 0
		Condition2= (DBCount2%5!=0) and 1 or 0
		T_Count[0] = DBCount1/5+Condition1
		T_Count[1] = DBCount2/5+Condition2
	T_Count[2] = Lecture.objects.count()/5+1
	
	#main 페이지 활성화 기능(1전공, 2전공 all)

	#URL을 통해 무슨 전공 페이지에 있는지 확인해서 그 정보 긁어옴
	#페이지 갯수가 11개 이상일 경우
	PageInformation[MajorNumber]=CurrentPageView(T_Count,PageNumber,0)
	PageInformation[MajorNumber][1] = PageNumber
	
	#각 강의 전공에 해당하는 DB 정보 저장 함 
	TotalBoard = [[],[],[]]
	if CourseCode[0] !="ENG":
		TotalBoard[0] = Lecture.objects.filter(Q(Code__contains = CourseCode[0]) | Q(Code__contains=CourseCode[1])).order_by('Code')[(PageInformation[0][1]-1)*5:(PageInformation[0][1]-1)*5+5]
		TotalBoard[1] = Lecture.objects.filter(Q(Code__contains = CourseCode[2]) | Q(Code__contains=CourseCode[3])).order_by('Code')[(PageInformation[1][1]-1)*5:(PageInformation[1][1]-1)*5+5]
	else:
		TotalBoard[0] = Lecture.objects.filter(Q(Code__contains =CourseCode[0]) |Q(Code__contains=CourseCode[1])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('Code')[(PageInformation[0][1]-1)*5:(PageInformation[0][1]-1)*5+5]
		TotalBoard[1] = Lecture.objects.filter(Q(Code__contains =CourseCode[2]) |Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('Code')[(PageInformation[1][1]-1)*5:(PageInformation[1][1]-1)*5+5]
	TotalBoard[2] = Lecture.objects.order_by('Code')[(PageInformation[2][1]-1)*5:(PageInformation[2][1]-1)*5+5]

	PageBoard = PageView(TotalBoard)
	##Session Save
	

	# 페이지 총 수(페이지 넘길 때)
	TotalCount=list()
	for i in range(0,len(T_Count)):
		TotalCount.append(PageTotalCount(i,T_Count,PageInformation[i]))
	
	
	dic = {'user':User,
		   'PageBoard':PageBoard,
		   'TotalCount' : TotalCount,
		   'PageInformation' : PageInformation,
		   'T_Count':T_Count,
		   'Page':PageNumber
		   }

	return dic
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


def MainView(request):
	CourseCode = MajorSelect(request.user) 
	
	#1전공, 2전공 전체 강의 페이지 갯수를 불러옴
	T_Count=[ [],[] ,[] ]
	T_Count[0] = Lecture.objects.filter(Q(Code__contains=CourseCode[0]) |Q(Code__contains= CourseCode[1])).count()/6+1
	T_Count[1] = Lecture.objects.filter(Q(Code__contains= CourseCode[2]) | Q(Code__contains=CourseCode[3])).count()/6+1
	T_Count[2] = Lecture.objects.count()/6+1

	##메인페이지 전공 교양 페이지 넘기는 것을 독립적으로 돌리는 기능
	PageInformation = list()

	#페이지 넘기는 기능
	#각 전공을 표현하는데 11페이지가 넘어갈 경우 11로 고정시키고 그렇지 않을 경우 T_Count를 기준으로 한다.
	# for i in range(0,3): 
	# 	if T_Count[i]>11:
	# 		PageInformation[i][2] = 11
	# 	else:
	# 		PageInformation[i][2] =T_Count[i]
	for i in range (0,len(T_Count))	:
		PageInformation.append(FirstPageView(i,T_Count))

	#글로벌 리더십일 경우랑 그이외의 경우로 분류해서 출력(글로벌 리더십때문에 좀 꼬여서..)
	TotalBoard = [[],[],[]]
	if CourseCode[0] !="ENG":
		TotalBoard[0] = Lecture.objects.filter(Q(Code__contains = CourseCode[0]) | Q(Code__contains=CourseCode[1])).order_by('Code')[(PageInformation[0][1]-1)*5:(PageInformation[0][1]-1)*5+5]
		TotalBoard[1] = Lecture.objects.filter(Q(Code__contains = CourseCode[2]) | Q(Code__contains=CourseCode[3])).order_by('Code')[(PageInformation[1][1]-1)*5:(PageInformation[1][1]-1)*5+5]
	else:
		TotalBoard[0] = Lecture.objects.filter(Q(Code__contains =CourseCode[0]) |Q(Code__contains=CourseCode[1])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('Code')[(PageInformation[0][1]-1)*5:(PageInformation[0][1]-1)*5+5]
		TotalBoard[1] = Lecture.objects.filter(Q(Code__contains =CourseCode[2]) |Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[2])|Q(Code__contains=CourseCode[3])|Q(Code__contains=CourseCode[4])|Q(Code__contains=CourseCode[5])).order_by('Code')[(PageInformation[1][1]-1)*5:(PageInformation[1][1]-1)*5+5]
	TotalBoard[2] = Lecture.objects.order_by('-id')[(PageInformation[2][1]-1)*5:(PageInformation[2][1]-1)*5+5] 
	
	#페이지 보여주는 정보 함수 불러움 index참고
	PageBoard =  PageView(TotalBoard)

	##독립적 페이지 위치를 다음 페이지 넘기는 것할 때 정보 넘김
	request.session['PageInformation'] = PageInformation
	
	TotalCount=[range(1,PageInformation[0][2]),range(1,PageInformation[1][2]),range(1,PageInformation[2][2])]
	##보여주려는 페이지 자바스크립트 active(index.html {{Active}}참고)
	Active = ["active","",""]

	Temp = dict()
	Temp ={	'user': request.user,
			'PageBoard': PageBoard,
			'TotalCount' : TotalCount,
			'PageInformation' : PageInformation,
			'Path':request.path,
			'Active':Active,
			'Page':1
			}
	# Create your views here.
	return Temp


#메인 페이지 view 함수로 옮김
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