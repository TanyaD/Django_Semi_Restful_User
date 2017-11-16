from django.shortcuts import render, HttpResponse, redirect


from models import *

def index(request):   
    return render(request, 'books_authors/index.html', {"users": User.objects.all()})

def show(request,id):
    return render(request, 'books_authors/userinfo.html', {"users": User.objects.filter(id=id)})

def edit(request,id):
    return render(request, 'books_authors/edituser.html', {"users": User.objects.filter(id=id)})

def new(request):
    return render(request, 'books_authors/newuser.html')

def create(request):
    inst=User.objects.create(full_name=request.POST['fullname'], email=request.POST['email'])
    return redirect('/users')

def update(request,id):
    user=User.objects.get(id=id)
    user.full_name=request.POST['fullname']
    user.email=request.POST['email']
    user.save()
    return redirect('/users')

def destroy(request,id):
    b=User.objects.get(id=id)
    b.delete()
    return redirect('/users')

    #newuser=User.objects.create(full_name="New User", email="nn@gmail.com")


"""def edit(request):
def show(request):
def create(request):
def destroy(request):
def update(request):"""




