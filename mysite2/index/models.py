from django.db import models
from lecture.models import Lecture
from login.models import Profile
	
class Description_Answer(models.Model):
	CreatedID = models.ForeignKey(Profile)
	Answer = models.TextField(max_length=200)
	Course = models.ForeignKey(Lecture)
	def __unicode__(self):
		return self.CreatedID.User.username

class Course_Evaluation(models.Model):
	Course = models.ForeignKey(Lecture)
	CreatedID = models.ForeignKey(Profile)
	Speedy = models.PositiveSmallIntegerField(default=5, null=False)
	Homework = models.PositiveSmallIntegerField(default=5, null=False)
	Level_Difficulty = models.PositiveSmallIntegerField(default=5, null=False)
	Check = models.BooleanField(default=False)
	CourseComment = models.TextField(max_length=500)
	StarPoint =models.FloatField(default=0)
	What_Answer = models.IntegerField(default=0)
	Exam_Answer = models.ManyToManyField(Description_Answer)
	Who_Answer = models.TextField(max_length=200, null=True)
	Url_Answer = models.TextField(max_length=200, null=True)
	def __unicode__(self):
		return self.Course.CourseName

class Total_Evaluation(models.Model):
	Course = models.ForeignKey(Lecture)
	Total_Speedy = models.IntegerField(default=0)
	Total_Homework = models.IntegerField(default=0)
	Total_Level_Difficulty = models.IntegerField(default=0)
	Total_Count =models.IntegerField(default=0)
	Total_P_Knowledge = models.IntegerField(default=5, null=False)
	Total_StarPoint = models.FloatField(default=0)
	Total_Recommend = models.IntegerField(default=0, null=False)
	Total_Mix = models.IntegerField(default=0)
	Total_Short_Answer = models.IntegerField(default=0)
	Total_Long_Answer = models.IntegerField(default=0)
	Total_Unknown_Answer = models.IntegerField(default=0)

	def __unicode__(self):
		return self.Course.Code



# Create your models here.
