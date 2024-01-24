from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
from django.urls import reverse
from django.contrib.auth import authenticate,login

# Create your views here.

def register(request):
    EUFO=userForm()
    EPFO=profileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=="POST" and request.FILES:
        CUFO=userForm(request.POST)
        CPFO=profileForm(request.POST,request.FILES)
        if CUFO.is_valid() and CPFO.is_valid():
            MCUFO=CUFO.save(commit=False)
            pw=CUFO.cleaned_data['password']
            MCUFO.set_password(pw)
            MCUFO.save()

            MCPFO=CPFO.save(commit=False)
            MCPFO.username=MCUFO
            MCPFO.save()
            return HttpResponse('Registration SuccussFull')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'register.html',d)


def home(request):
    if request.session.get('username'):
        un=request.session.get('username')
        d={'un':un}
        return render(request,'home.html',d)
    return render(request,'home.html')

def userlogin(request):
    if request.method=='POST':
        un=request.POST['un']
        pw=request.POST['pw']
        AUO=authenticate(username=un,password=pw)
        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=un
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Invalid Credentials')

    return render(request,'userlogin.html')