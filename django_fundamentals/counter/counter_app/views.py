from django.shortcuts import render, redirect

def index(request):
    if 'visit' not in request.session:
        request.session['visit'] = 0
    request.session['visit'] += 1
    context = {
        'temp' : str(request.session['visit'])
    }
    return render(request, 'index.html', context)

def destroy_session(request):
    del request.session['visit'] 
    return redirect('')

    