from django.shortcuts import render , HttpResponse , redirect
from .models import *
from datetime import datetime
# Create your views here.
def Index(request):
    date=datetime.now()
   
    data=AboutModel.objects.all()[0]
    age=date.year-data.DateOfBirth.year
    context={
        "data":data,
        "age":age,
    }
    print("my data is",data)
    return render(request, 'index.html',context)



# ------------------------Dashboard Section 
def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        data = Administrator.objects.get(username=username)
        if( data.password == password):
            request.session['active']=True
            return redirect('dashboard')
        else:
            return HttpResponse("not FOund")
    return render(request, 'dashboard/login.html')

def Dashboard(request):
    if request.session.has_key('active'):
         return HttpResponse("This is index page")