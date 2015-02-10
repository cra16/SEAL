from django.db import models
from lecture.models import Lecture
from login.models import Profile
class QnA_Board(models.Model):
	TextWriter = models.CharField(max_length =30)
	TextName = models.CharField(max_length =50)
	ClickScore = models.PositiveIntegerField(default =0)
	Text = models.TextField()
	created = models.DateField(auto_now_add=True, auto_now=True)
	def __unicode__(self):
		return self.TextName

class Notice_Board(models.Model):
	TextWriter = models.CharField(max_length =30)
	TextName = models.CharField(max_length =50)
	ClickScore = models.PositiveIntegerField(default =0)
	Text = models.TextField()
	created = models.DateField(auto_now_add=True, auto_now=True)

	def __unicode__(self):
		return self.TextName
	
class Course_Evaluation(models.Model):
	Course = models.ForeignKey(Lecture)
	CreatedID = models.ForeignKey(Profile)
	Speedy = models.PositiveSmallIntegerField(default=5, null=False)
	Reliance = models.PositiveSmallIntegerField(default=5, null=False)
	Helper = models.PositiveSmallIntegerField(default=5, null=False)
	Question = models.PositiveSmallIntegerField(default=5, null=False)
	Exam = models.PositiveSmallIntegerField(default=5, null=False)
	Homework = models.PositiveSmallIntegerField(default=5, null=False)
		
	def __unicode__(self):
		return self.Course.CourseName

class Total_Evaluation(models.Model):
        CourseName = models.ForeignKey(Lecture)
        Total_Speedy = models.IntegerField(default=0)
        Total_Reliance = models.IntegerField(default=0)
        Total_Helper = models.IntegerField(default=0)
        Total_Question = models.IntegerField(default=0)
        Total_Exam = models.IntegerField(default=0)
        Total_Homework=models.IntegerField(default=0)
		Total_Count =models.IntegerField(default=0)
        def __unicode__(self):
                return self.CourseName.Code



# Create your models here.
