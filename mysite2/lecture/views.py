# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from lecture.models import Lecture
import xlrd
# Create your views here.

def lec_update(request):
	semester_lst = ['11-1', '11-2', '11-Summer', '11-Winter', '12-1', '12-2', '12-Summer', '12-Winter', '13-1', '13-2', '13-Summer', '13-Winter', '14-1', '14-2', '14-Summer', '14-Winter']
	file_location = "/opt/bitnami/apps/django/django_projects/darkzero/mysite2/gasul_table/"
	# 학부별 정리
	for semester in semester_lst:
		file_lst = [
					file_location+semester+'/0001.xlsx',
					file_location+semester+'/0009.xlsx',
					file_location+semester+'/0010.xlsx',
					file_location+semester+'/0011.xlsx',
					file_location+semester+'/0012.xlsx',
					file_location+semester+'/0021.xlsx',
					file_location+semester+'/0022.xlsx',
					file_location+semester+'/0024.xlsx',
					file_location+semester+'/0033.xlsx',
					file_location+semester+'/0071.xlsx',
					file_location+semester+'/0074.xlsx',
					file_location+semester+'/0077.xlsx',
					file_location+semester+'/0078.xlsx',
					file_location+semester+'/0090.xlsx'
					]
		for xls in file_lst:
			try:
				workbook = xlrd.open_workbook(xls)
			except:
				continue
			sheet = workbook.sheet_by_index(0)
			lec_lst = []
			for row in range(3, sheet.nrows, 4):
				lec_info = []
				for col in range(sheet.ncols):
					val = sheet.cell_value(row,col)
					# if val == '' :	# 값이 NULL이면 조작안함
					lec_info.append(val)
				lec_info.append(sheet.cell_value(row+1,3))	# 과목영어이름
				lec_info.append(sheet.cell_value(row+1,5))	# 교수님 성함
				lec_lst.append(lec_info)
			for var in lec_lst:
				if not var[11]:
					var[11] = var[5]	# 전공일 경우에는 전공명으로
				if var[9] == '':
					var[9] = 0
				if var[4] == '':
					var[4] = 0
				try:
					d_lec = Lecture.objects.filter(Semester=semester, Code=var[1], Class=var[2])
					if d_lec: # 업데이트 가능한 요소들
						d_lec.Class =  var[2]
						d_lec.Credit = var[4]
						d_lec.Period = var[6]
						d_lec.ClassRoom = var[7]
						d_lec.Fix_num = var[8]
						d_lec.Take_num = var[9]
						d_lec.EnglishRatio = var[10]
						d_lec.Professor = var[-1]
					else:
						new_lec = Lecture(
							Semester=semester,
							Category=var[0],
							Code=var[1],
							Class=var[2],
							CourseName=var[3],
							Credit=var[4],
							Major=var[5],
							Period=var[6],
							ClassRoom=var[7],
							Fix_num=var[8],
							Take_num=var[9],
							EnglishRatio=var[10],
							CategoryDetail=var[11],
							CourseName_Eng=var[-2],
							Professor=var[-1],
							)
						new_lec.save()
				except:
					return HttpResponse('데이터 입력 중 오류가 발생했습니다.')
	return HttpResponse('성공적으로 데이터를 입력했습니다.')
