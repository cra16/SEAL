from django.db import models
from lecture.models import Lecture

class QnA_Board(models.Model):
	TextWriter = models.CharField(max_length =30)
	TextName = models.CharField(max_length =50)
	ClickScore = models.PositiveIntegerField(default =0)
	Text = models.TextField()
	created = models.DateField(auto_now_add=True, auto_now=True)

class Notice_Board(models.Model):
	TextWriter = models.CharField(max_length =30)
	TextName = models.CharField(max_length =50)
	ClickScore = models.PositiveIntegerField(default =0)
	Text = models.TextField()
	created = models.DateField(auto_now_add=True, auto_now=True)
	
class Course_Evaluation(models.Model):
	Course = models.ForeignKey(Lecture)
	Speedy = models.PositiveSmallIntegerField(default=5, null=False)
	Reliance = models.PositiveSmallIntegerField(default=5, null=False)
	Helper = models.PositiveSmallIntegerField(default=5, null=False)
	Question = models.PositiveSmallIntegerField(default=5, null=False)
	Exam = models.PositiveSmallIntegerField(default=5, null=False)
	Homework = models.PositiveSmallIntegerField(default=5, null=False)
		




# Create your models here.
