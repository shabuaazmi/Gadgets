from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from electronics.models import table_user,table_gadgets
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def login(request):
    return render(request,'login.html')
def createac(request):
    return render(request,'createac.html')
def createac1(request):
    a=User()
    u=table_user()
    u.name=request.POST.get('name')
    u.gender=request.POST.get('gender')
    u.phone=request.POST.get('phone')
    u.email=request.POST.get('email')
    u.place=request.POST.get('Place')
    u.address=request.POST.get('address')
    a.first_name=request.POST.get('name')
    a.email=request.POST.get('email')
    a.username=request.POST.get('username')
    u.username=request.POST.get('username')
    ps=request.POST.get('pswrd')
    # print(ps,"heloooo")
    a.set_password(ps)
    
    p=request.FILES['photo']
    fs=FileSystemStorage()
    c=fs.save(p.name,p)
    fileurl=fs.url(c)
    u.photo=fileurl
    a.save()
    u.save()
    return redirect('/')
def login1(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    # print(username,"test2",password)
    o=authenticate(username=username,password=password)
    print(o,"test1")
    request.session['username']=username
    if o is not None and o.is_superuser==1:
        return redirect('/adminpage/')
    elif o is not None and o.is_superuser==0:
        return redirect('/userpage/')
    else:
        return HttpResponse('invalid_respond')
def adminpage(request):
    return render(request,'adminpage.html')
def userpage(request):
    s=request.session['username']
    return render(request,'userpage.html',{'x':s})
def userprofile1(request):
    s=request.session['username']
    # print(s,"testinggg")
    e=table_user.objects.get(username=s)
    f=User.objects.get(username=s)
    return render(request,'userprofile.html',{'y':e,'z':f})

def updateprofile(request,id):
    a=table_user.objects.get(id=id)
    return render(request,'updateprofile.html',{'x':a})
def updateprofile1(request,id):
    try:
        a=table_user.objects.get(id=id)
        a.username=request.POST.get('username')
        a.name=request.POST.get('name')
        a.gender=request.POST.get('gender')
        a.place=request.POST.get('place')
        a.phone=request.POST.get('phone')
        a.email=request.POST.get('email')
        a.address=request.POST.get('address')
        p=request.FILES['photo']
        fs=FileSystemStorage()
        c=fs.save(p.name,p)
        fileurl=fs.url(c)
        a.photo=fileurl
        a.save()
    except:
        a=table_user.objects.get(id=id)
        a.username=request.POST.get('username')
        a.name=request.POST.get('name')
        a.gender=request.POST.get('gender')
        a.place=request.POST.get('place')
        a.phone=request.POST.get('phone')
        a.email=request.POST.get('email')
        a.address=request.POST.get('address')
        a.save()
    return redirect('/userprofile/')
def gadget(request):
    a=table_gadgets.objects.all()
    return render(request,'gadget.html',{'data':a})
def addgadget(request):
    a=table_gadgets.objects.all()
    return render(request,'addgadget.html',{'data':a})
def gadgetform(request):
    return render(request,'gadgetform.html')
def gadgetform1(request):
    g=table_gadgets()
    g.g_name=request.POST.get('pname')
    g.g_price=request.POST.get('price')
    g.g_warranty=request.POST.get('warranty')
    g.g_category=request.POST.get('category')
    p=request.FILES['photo']
    fs=FileSystemStorage()
    c=fs.save(p.name,p)
    fileurl=fs.url(c)
    g.photo=fileurl
    g.save()
    return redirect('/gadgetsform/')
def viewgedget(request):
    a=table_gadgets.objects.all()
    return render(request,'addgadget.html',{'data':a})

# filter

def viewmobile(request):
    a=table_gadgets.objects.filter(g_category="mobile")
    return render(request,'gadget.html',{'data':a})
def lessprice(request):
    a=table_gadgets.objects.filter(g_price__lte=50000)
    return render(request,'gadget.html',{'data':a})


def usertable(request):
    a=table_user.objects.all()
    return render(request,'usertable.html',{'data':a})
def dltuser(request,id):
    a=table_user.objects.get(id=id)
    a.delete()
    return redirect('/usertable/')
def updategadget(request,id):
    a=table_gadgets.objects.get(id=id)
    return render(request,'updategadget.html',{'x':a})
def updategadget1(request,id):
    try:
        g=table_gadgets.objects.get(id=id)
        g.g_name=request.POST.get('pname')
        g.g_price=request.POST.get('price')
        g.g_warranty=request.POST.get('warranty')
        g.g_category=request.POST.get('category')
        p=request.FILES['photo']
        fs=FileSystemStorage()
        c=fs.save(p.name,p)
        fileurl=fs.url(c)
        g.photo=fileurl
        g.save()
    except:
        g=table_gadgets.objects.get(id=id)
        g.g_name=request.POST.get('pname')
        g.g_price=request.POST.get('price')
        g.g_warranty=request.POST.get('warranty')
        g.g_category=request.POST.get('category')
        g.save()
    return redirect('/viewgedget/')
def dltgadget(request,id):
    a=table_gadgets.objects.get(id=id)
    a.delete()
    return redirect('/viewgedget/')


    






# Create your views here.
