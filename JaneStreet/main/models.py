
# Create your models here.
from django.db import models
import datetime

# Create your models here.

class 	Investment(models.Model):
	company_name = models.CharField(max_length=150)
	fund_ownership = models.DecimalField(max_digits=5, decimal_places=2)
	initial_investment_date= models.DateField(auto_now=False,null=True)
	initial_investment= models.IntegerField()
	total_invested=models.IntegerField()
	reported_value_end_of_Q2=models.IntegerField()
	unrealised_gain=models.IntegerField()
	MOIC=models.DecimalField(max_digits=5, decimal_places=2)
	year=models.IntegerField(null=True)
	image=models.ImageField(null=True,blank=True)
	


	def __str__(self):
		return self.company_name