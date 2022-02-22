from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
class ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    email_address = forms.EmailField(max_length = 150)
    message = forms.CharField(widget = forms.Textarea, max_length = 2000)


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101,required=True)
    last_name = forms.CharField(max_length=101,	required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']	        
        
from .models import Investment

class ScheduleOfInvestmentForm(forms.ModelForm):
    class Meta:
        model=Investment
        fields="__all__"
widget={
    "company_name":forms.NumberInput(attrs={"class":"form-control"}),
    "fund_ownership":forms.NumberInput(attrs={"class":"form-control"}),
    
    
    "initial_investment_date":forms.DateInput(attrs={"class":"form-control"}),
    "initial_investment":forms.NumberInput(attrs={"class":"form-control"}),
    "total_invested":forms.NumberInput(attrs={"class":"form-control"}),
    "reported_value_end_of_Q2":forms.NumberInput(attrs={"class":"form-control"}),
    "unrealised_gain":forms.NumberInput(attrs={"class":"form-control"}),
    "MOIC":forms.NumberInput(attrs={"class":"form-control"}),
    "year":forms.DateInput(attrs={"class":"form-control"}),
    "image":forms.FileInput(attrs={"class":"form-control"}),
}  
class InvestmentForm(forms.ModelForm):
    class Meta:
        model=Investment
        fields="__all__"
widget={
    "company":forms.NumberInput(attrs={"class":"form-control"}),
    "company_name":forms.NumberInput(attrs={"class":"form-control"}),

    "total_commited":forms.NumberInput(attrs={"class":"form-control"}),
    "net_investment":forms.DateInput(attrs={"class":"form-control"}),
    "total_bhi_shares_remaining":forms.NumberInput(attrs={"class":"form-control"}),
    "latest_share_price":forms.NumberInput(attrs={"class":"form-control"}),
    "fair_market_value":forms.NumberInput(attrs={"class":"form-control"}),
    "total_coc_returns":forms.NumberInput(attrs={"class":"form-control"}),
    "year":forms.DateInput(attrs={"class":"form-control"}),
    "image":forms.FileInput(attrs={"class":"form-control"}),
}  
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()