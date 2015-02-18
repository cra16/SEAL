from django.db import models
from lecture.models import Lecture
from login.models import Profile

class Recommend_Course(models.Model):
	Course = models.ForeignKey(Lecture)
	CreatedID = models.ForeignKey(Profile)

	def __unicode__(self):
		return u'%s %s' % (self.Course.CourseName, self.CreatedID.UserName)

class Like_Course(models.Model):
	Course = models.ForeignKey(Lecture)
	CreatedID = models.ForeignKey(Profile)

	def __unicode__(self):
		return u'%s %s' % (self.Course.CourseName, self.CreatedID.UserName)
# Create your models here.