from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from login_app.models import *
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def reg(request):
    
    if request.POST['password'] == request.POST['confirmpassword']:
        errors=User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/')
        else:
            hashpassword= bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            data={'username':request.POST['Username'],
            'password':hashpassword,
            'email':request.POST['email']}
            User.objects.create(username=request.POST['Username'],password=hashpassword,email=request.POST['email'])
            request.session['user']=data
            return redirect('/welcome')
def welcome(request):
    if 'user' in request.session:
        return render(request,'welcome.html')
    return redirect('/login')
def logout(request):

    request.session.clear()
    return render(request,"login.html")
def loginz(request):
    psswd=request.POST['password']
    username=request.POST['Username']
    user = User.objects.filter(username=username)
    if user:
        logged_user=user[0]
        
        if bcrypt.checkpw(psswd.encode(), logged_user.password.encode()):

            request.session['user']={
                'username':username,
                'password':psswd
            }
           
            return redirect('/welcome')
        else :
            return HttpResponse('password is wrong')
    else:
        return HttpResponse('user is not found')