from django.db import models

# Create your models here.
class Lecture(models.Model):
	Category = models.CharField(max_length=20, null=False)
	Code = models.CharField(max_length=20, null=False)
	CourseName = models.CharField(max_length=40, null=False)
	Credit = models.PositiveSmallIntegerField(default=0, null=False)
	def __unicode__(self):
		rt_name = "%s" % (self.CourseName, )
		return rt_name
	