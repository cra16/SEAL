from django.db import models


class Study(models.Model):
    Name = models.CharField(max_length=30)
    HeartCount = models.IntegerField(default=0)
        
    def __unicode__(self):
        return self.Name

class ReviewOfStudy(models.Model):
    Name = models.CharField(max_length=30)
    UserID = models.CharField(max_length=30)
    
    solve1 = models.FloatField(default=0.0)
    solve2 = models.FloatField(default=0.0)
    solve3 = models.FloatField(default=0.0)
    solve4 = models.FloatField(default=0.0)


# Create your models here.
