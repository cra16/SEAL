from django.db import models
from login.models import Profile
class QnA_Board(models.Model):
	TextWriter = models.ForeignKey(Profile)
	TextName = models.CharField(max_length =50)
	ClickScore = models.PositiveIntegerField(default =0)
	Text = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.TextName

# Create your models here.
