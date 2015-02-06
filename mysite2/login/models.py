# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings

class Profile(models.Model):
    class Meta:
        verbose_name = u'프로필'
        verbose_name_plural = u'프로필'
    User = models.OneToOneField(settings.AUTH_USER_MODEL)
    StuNum = models.CharField(max_length=2)
    FirstMajor = models.CharField(max_length=30)
    SencondMajor = models.CharField(max_length=30)



# Create your models here.
