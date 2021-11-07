from django.http.response import BadHeaderError, HttpResponse,JsonResponse
from django.core.mail import send_mail, BadHeaderError

from .models import Investment

# Create your views here.
from django.shortcuts import  render, redirect
from .forms import ContactForm, NewUserForm, ScheduleOfInvestmentForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

from django.core.paginator import Paginator #import Paginator
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm, UserCreationForm #add this

from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

# "uid": urlsafe_base64_encode(force_bytes(user.pk)).decode() if jango version is 2.1


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "main/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="main/password/password_reset.html", context={"password_reset_form":password_reset_form})
# Create your views here.
def homepage(request):
	investment = Investment.objects.all() #queryset containing all books we just created
	paginator = Paginator(investment, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request=request, template_name="main/home.html", context={'investment':page_obj})    


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})
	
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'users/register.html', context)	
    
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect ("main:homepage")
      
    form = ContactForm()
    return render(request, "main/contact.html", {'form':form})







def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("main:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})    

# Create your views here.
def investment(request):
	investment = Investment.objects.all() #queryset containing all books we just created
	paginator = Paginator(investment, 6)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request=request, template_name="main/investmentcompanies.html", context={'investment':page_obj})
   
def register_investment(request):
    if request.method =="POST":
      form=ScheduleOfInvestmentForm(request.POST , request.FILES)
      
      if form.is_valid():
          form.save()
      else:
          print(form.errors)
    else:
        form=ScheduleOfInvestmentForm()
    return render(request,"main/investmentform.html",{"form":form})

def investment_list(request):
    investments=Investment.objects.all()
    return render(request,"main/investments.html",{"investments":investments})

def edit_investment(request,id):
    investment=Investment.objects.get(id=id)
    if request.method=="POST":
        form=ScheduleOfInvestmentForm(request.POST,instance=investment)
        if form.is_valid():
            form.save()
    else:
            form=ScheduleOfInvestmentForm(instance=investment)
    return render(request,"edit_investment.html",{"form":form})
    
def investment_profile(request,id):
    investment=Investment.objects.get(id=id)
    return render(request,"investment_profile.html",{"investment":investment})




def delete_investment(request,id):
    investment=Investment.objects.get(id=id)
    if request.method == 'POST':
        investment.delete()
        return redirect('main/investments.html')
    return render (request,'main/delete.html')

def landingpage(request):
    landingpage  #queryset containing all books we just created
    return render(request=request, template_name="main/landing.html", context={'landingpage':landingpage})  

