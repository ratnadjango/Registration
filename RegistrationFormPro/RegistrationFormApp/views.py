from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import RegistrationData
from django.http.response import HttpResponse

def Register_view(request):
    if request.method=="POST":
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            first_name = request.POST.get('first_name', '')
            last_name = request.POST.get('last_name', '')
            email_id = request.POST.get('email_id', '')
            mobile_number = request.POST.get('mobile_number', '')
            user_name = request.POST.get('user_name','')
            password = request.POST.get('password','')
            password1 = request.POST.get('password1','')
            data = RegistrationData(
                first_name = first_name,
                last_name = last_name,
                email_id = email_id,
                mobile_number = mobile_number,
                user_name = user_name,
                password = password,
                password1 = password1
            )
            data.save()
            lform =LoginForm()
            return render(request,'login.html',{'lform':lform})
            #return redirect('/')
    else:
        rform = RegistrationForm()
        return render(request,'registration.html',{'rform':rform})

def Login_view(request):

    if request.method=="POST":
        lform = LoginForm(request.POST)
        if lform.is_valid():
            uname = request.POST.get('user_name','')
            pwd = request.POST.get('password','')

            uname1 = RegistrationData.objects.filter(user_name=uname)
            pwd1 = RegistrationData.objects.filter(password=pwd)

            if uname1 and pwd1:
                return HttpResponse("valid details")
            else:
                return HttpResponse("invalid details")
    else:
        lform = LoginForm()
        return render(request,'login.html',{'lform':lform})