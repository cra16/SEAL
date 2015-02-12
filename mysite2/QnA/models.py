from django.db import models

class QnA_Board(models.Model):
	TextWriter = models.CharField(max_length =30)
	TextName = models.CharField(max_length =50)
	ClickScore = models.PositiveIntegerField(default =0)
	Text = models.TextField()
	created = models.DateField(auto_now_add=True, auto_now=True)
	def __unicode__(self):
		return self.TextName

# Create your models here.
