from django import forms
from bluehaven.models import Bluehaven


class BluehavenRegistrationForm(forms.ModelForm):
    class Meta:
        model=Bluehaven
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