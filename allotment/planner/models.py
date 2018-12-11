from django.db import models


MONTHS = enumerate(['January',
					'February',
					'March',
					'April',
					'May',
					'June',
					'July',
					'August',
					'September',
					'October',
					'November',
					'December',],1)
# Create your models here.
class Month(models.Model):
	"""
	We might want to use this to determine what to work on
	EG wanna see all jobs for March without searching each possible task
	(planting, harvest etc) individually

	If we do, let's use the ID as the month number - so January = 1, December = 12
	We can make sure that happens using fixtures :)

	For now on the Plant I'll just use an Integer field rather than FK to a month
	"""
	name = models.CharField(max_length=10)


	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']

# for m in range(1,len(MONTHS)+1):
#     Month.objects.create(name=MONTHS[m-1],id=m)