from django.shortcuts import redirect, render
from .models import*

def index(req):
    context={
        "Shows": Show.objects.all()
    }
    return render(req,"main.html",context)
def show(req):
    return render(req,"addshow.html")
def addshow(req):
    title = req.POST['showtitle']
    network = req.POST['network']
    releasedate = req.POST['releasedate']
    desc = req.POST['desc']
    Show.objects.create(title=title,network=network,releasedate=releasedate,desc=desc)
    last = Show.objects.last()
    id = last.id
    return redirect('showtv/'+str(id))
def showtv(req,id):
    showid = Show.objects.get(id=id)
    
    context={
        'showid':showid.id,
        'showtitle':showid.title,
        'showdesc':showid.desc,
        'showreles':showid.releasedate
    }
    return render(req,"showtv.html",context)
def showedit(req,id):
    showid = Show.objects.get(id=id)
    context ={
        'showid':showid.id,
        'showtitle':showid.title,
        'showdesc':showid.desc,
        'showreles':showid.releasedate
    } 
    return render(req,"editshow.html",context)
def edit(req,id):
    title = req.POST['showtitle']
    network = req.POST['network']
    releasedate = req.POST['releasedate']
    desc = req.POST['desc']
    last = Show.objects.get(id=id)
    Show.objects.filter(id=last.id).update(title=title,network=network,releasedate=releasedate,desc=desc)
    last2 = Show.objects.get(id=id)
    context ={
        'showid':last2.id,
        'showtitle':last2.title,
        'showdesc':last2.desc,
        'showreles':last2.releasedate,
        
    } 
    return render(req,"showtv.html",context)
def destroy(req,id):
    Show.objects.filter(id=id).delete()
    return redirect('/shows')