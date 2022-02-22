
# Create your models here.
from django import forms
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
    
    

class 	Investments(models.Model):
    company = models.CharField(max_length=150)
    total_commited=models.IntegerField()
    net_investment=models.IntegerField()
    total_bhi_shares_remaining=models.IntegerField()
    latest_share_price=models.DecimalField(max_digits=5, decimal_places=2)
    fair_market_value=models.DecimalField(max_digits=10, decimal_places=2)
    total_coc_returns=models.DecimalField(max_digits=5, decimal_places=2)
    year=models.IntegerField(null=True)
    image=models.ImageField(null=True,blank=True)   
	
def __str__(self):
		return self.company_name

def __str__(self):
    		return self.company

# Create your models here.
class Movies(models.Model):
   file = models.FileField(upload_to='documents/')
   image = models.ImageField(upload_to='images/')