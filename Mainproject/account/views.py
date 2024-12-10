from django.shortcuts import render,redirect
from django.views import View
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login
# Create your views here.

class Register(View):
    def get(self,request):
        form= RegisterForm()
        return render(request,"accounts/register.html",{'form':form})

    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,"accounts/register.html",{'form':form})
        




class Login(View):
    def get(self,request):
        form= LoginForm()
        return render(request,"accounts/login.html",{'form':form})

    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(form.cleaned_data['username'],form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect('register')
        return render(request,"accounts/login.html",{'form':form})



