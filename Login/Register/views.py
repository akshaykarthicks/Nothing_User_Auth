from django.shortcuts import render
from .forms import registerform
from django.contrib.auth.decorators import login_required
# django auth forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, authenticate 
# from django.shortcuts import redirect

# Create your views here.
def register(response):
    if response.method=='POST':
        form=registerform(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
           
    else:
        form=registerform() #if the method is not post

    return render(response,'register.html',{'form':form})
@login_required 
def home(response):
    return render(response,'home.html')