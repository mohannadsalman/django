
from django.shortcuts import redirect, render,HttpResponse
from user_auth_app.models import user
def index(request):
    return render(request,'index.html')
def login(request):
    username = request.POST['username']
    passwd = request.POST['passwd']
    Users =user.objects.filter(username=username)
    
    if len(Users)==0:
        return redirect('/')

    Users = user.first()
    if Users.password != passwd:
        return redirect('/')
    data= {
        "username": Users.username,
        "password": Users.passwd,
        "address": Users.address,
        "email": Users.email,
    }
    request.session['Users']=data
    return redirect('/welcome')

def register(request):
    username = request.POST['username']
    passwd = request.POST['passwd']
    address = request.POST['address']
    email = request.POST['email']
    
    User = user.objects.create(username = username, password =passwd, address = address, email = email)
    data= {
        "username": username,
        "password": passwd,
        "address": address,
        "email": email,
    }
    request.session['user']= data
    return redirect("/welcome")

def welcome(request):
    if 'user'in request.session:
        user = request.session['user']
        return render(request,"welcome.html", user)
    return redirect('/')

def logout(request):
    if 'user'in request.session:
        request.session.clear()
    return redirect("/")