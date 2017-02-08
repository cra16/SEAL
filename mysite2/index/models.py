from django.db import models
from login.models import Profile
from lecture.models import Lecture
import datetime
	
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
	CourseComment = models.TextField(max_length=1000)
	StarPoint =models.FloatField(default=0)
	What_Answer = models.IntegerField(default=0)
	Exam_Answer = models.ManyToManyField(Description_Answer)
	Who_Answer = models.TextField(max_length=200, null=True)
	
	Course_Answer = models.IntegerField(default=0)
	Url_Answer = models.TextField(max_length=200, null=True)
	create_date = models.DateTimeField(default=datetime.datetime.today())
	update_date = models.DateTimeField(default=datetime.datetime.today())
	def __unicode__(self):
			return '%s %s %s %s %s' % (self.Course.Code,self.Course.Professor, self.Course.CourseName,self.CreatedID,self.Course.Semester)


class Total_Evaluation(models.Model):
	Course = models.ForeignKey(Lecture)
	Total_Speedy = models.IntegerField(default=0)
	Total_Homework = models.IntegerField(default=0)
	Total_Level_Difficulty = models.IntegerField(default=0)
	Total_Count =models.IntegerField(default=0)
	Total_StarPoint = models.FloatField(default=0)
	Total_Recommend = models.IntegerField(default=0, null=False)
	Total_Mix = models.IntegerField(default=0)
	Total_Short_Answer = models.IntegerField(default=0)
	Total_Long_Answer = models.IntegerField(default=0)
	Total_Unknown_Answer = models.IntegerField(default=0)
	Total_Book_Like=models.IntegerField(default=0)
	Total_Ppt_Like = models.IntegerField(default=0)
	Total_Practice_Like = models.IntegerField(default=0)

	def __unicode__(self):
		return '%s %s %s' % (self.Course.Code,self.Course.Professor, self.Course.CourseName)

class Group_Total_Evaluation(models.Model):
	Code = models.CharField(max_length=20, null=False)
	CourseName = models.CharField(max_length=80, null=True)
	GroupTotalCount = models.IntegerField(default=0)

	def __unicode__(self):
		  return '%s %s %d' % (self.CourseName, self.Code,self.GroupTotalCount)

# Create your models here.
