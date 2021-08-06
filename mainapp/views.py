from mainapp.models import tab_login, tab_register
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def emp(request):
    return render(request,'emp.html')

def login(request):
    msg=""
    if request.method=='POST':
        username2=request.POST.get('username2')
        password2=request.POST.get('password2')
        if tab_login.objects.filter(username2=username2,password2=password2):
            data=tab_register.objects.get(username=username2,password=password2)
            request.session['userid']=data.id
            if data.status=='admin':
                return render(request,'reg.html',{'msg':msg})
            elif data.status=='1':
                return render(request,'emp.html',{'msg':msg})
        else: 
            msg="incorrect password or username"
          # return HttpResponse("incorrect password or username")
    return render(request,"login.html",{'msg':msg})

def reg(request):
    msg=""
    if request.method=="POST":
        username=request.POST.get('username')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if password==cpassword:
            if tab_register.objects.filter(username=username):
                msg="Username already exists"
                return render(request,'reg.html',{'msg':msg})
            else:
                if tab_register.objects.filter(email=email):
                    msg="Email already exists"
                    return render(request,'reg.html',{'msg':msg})
                else:
                    data=tab_register.objects.create(username=username,phone=phone,email=email,password=password,status=1)
                    data=tab_login.objects.create(username2=username,password2=password,status=1)
                    msg="Registration successfully done!!!"
                    return render(request,"login.html")
        else:
            msg="Password didn't match"
    return render(request,'reg.html',{'msg':msg})


