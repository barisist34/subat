from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import *

# Create your views here.

def giris_islemleri(request):
    form = LoginForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            #messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        #messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)

    #return HttpResponse("Giris")
def kayit(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        newUser = User(username =username,email=email)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        #messages.info(request,"Başarıyla Kayıt Oldunuz...")
        return redirect("index")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

def cikis(request):
    logout(request)
    return redirect("index")

   