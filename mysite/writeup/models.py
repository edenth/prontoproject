from django.db import models

# Create your models here.
class Report(models.Model):
	report_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
class Checklist(models.Model):
	report = models.ForeignKey(Report)
	list_text = models.CharField(max_length = 200)
	stage = models.IntegerField()
	is_check = models.BooleanField(default= False)