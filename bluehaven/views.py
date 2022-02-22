
    
    
    
from bluehaven.models import Bluehaven
from django.forms.forms import Form
from django.shortcuts import redirect, render
from .forms import BluehavenRegistrationForm
from .models import Bluehaven



def register_bluehaven(request):
    if request.method =="POST":
      form=BluehavenRegistrationForm(request.POST , request.FILES)
      
      if form.is_valid():
          form.save()
      else:
          print(form.errors)
    else:
        form=BluehavenRegistrationForm()
    return render(request,"register_bluehaven.html",{"form":form})

def bluehaven_list(request):
    bluehaven=Bluehaven.objects.all()
    return render(request,"bluehaven_list.html",{"bluehaven":bluehaven})

def edit_bluehaven(request,id):
    bluehaven=Bluehaven.objects.get(id=id)
    if request.method=="POST":
        form=BluehavenRegistrationForm(request.POST,instance=bluehaven)
        if form.is_valid():
            form.save()
    else:
            form=BluehavenRegistrationForm(instance=bluehaven)
    return render(request,"edit_bluehaven.html",{"form":form})
    
def bluehaven_profile(request,id):
    bluehaven=Bluehaven.objects.get(id=id)
    return render(request,"bluehaven_profile.html",{"bluehaven":bluehaven})

def delete_bluehaven(request,id):
    bluehaven=Bluehaven.objects.get(id=id)
    bluehaven.delete()
    return redirect("bluehaven_list")
