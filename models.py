from django.db import models

# Create your models here.
class useractivity(models.Model):
	uname = models.CharField(max_length=10)
	uage = models.IntegerField()


	class Meta:
		verbose_name = "useractivity"
		verbose_name_plural = "useractivity"
	def __str__(self):
		return '%s'%{self.sname}