from django import template
from datetime import date, timedelta

register = template.Library()

@register.filter(name='lookup')
def lookup(d, key):
    return d[key]

register.filter(lookup)


def calculateData(val,arg):

	if arg==1000:
		if val-1000>=0:
			return 1
	elif arg==100:
		if val%1000 -100 >=0:
			return 1

	elif arg==10:
		if val%100 -10 >=0:
			return 1
	elif arg==1:
		if val%10 -1 >=0:
			return 1
	return 0
register.filter(calculateData)