from django.db import models

# Create your models here.
class 	Bluehaven(models.Model):
    company = models.CharField(max_length=150)
    total_commited=models.IntegerField()
    net_investment=models.DecimalField(max_digits=10, decimal_places=2)
    total_bhi_shares_remaining=models.IntegerField()
    latest_share_price=models.DecimalField(max_digits=5, decimal_places=2)
    fair_market_value=models.DecimalField(max_digits=10, decimal_places=2)
    total_coc_returns=models.DecimalField(max_digits=5, decimal_places=2)
    year=models.IntegerField(null=True)
    image=models.ImageField(null=True,blank=True)   
	
def __str__(self):
		return self.company