from django.shortcuts import render
from .forms import login_form, add_form,add_history

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User_info, Treatment

# Create your views here.
def home(request):
    return render(request,'html/home.html')

# -- Login --
def login_user(request):
    form= login_form()
    if request.method=='POST':
        form=login_form(request, data=request.POST) 
        if form.is_valid():
            username= request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('view')
    context={'form':form}
    return render(request, 'html/login.html', context=context)


# -- Logout --
@login_required(login_url='login_user')
def logout_user(request):
    auth.logout(request)
    return redirect('login')


# -- User info --
@login_required(login_url='login_user') 
def view_user(request):
    user=User_info.objects.all()
    context={'user':user}
    return render(request, 'html/view.html', context=context)


# -- Add new user --
@login_required(login_url='login_user') 
def add_user(request):
    form= add_form()
    if request.method=="POST":
        form=add_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    context={'form':form}
    return render(request,'html/user_creation_form.html', context=context)
 

# -- treatment info --
@login_required(login_url='login_user') 
def treatement_info(request, pk):
    task=Treatment.objects.all().filter(user=pk)
    context={'task':task}
    return render(request, 'html/view_treatment.html', context=context)

# -- treatement history --
@login_required(login_url='login_user') 
def new_history(request):
    form=add_history()
    if request.method =="POST":
        form=add_history(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view')
    context={'form':form}
    return render(request, 'html/add_history.html', context=context)


# ---- edit user details ----

@login_required(login_url='login_user') 
def update_user(request, pk):
    task=User_info.objects.get(user_id=pk)
    form=add_form(instance=task)
    if request.method=='POST':
        form=add_form(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('view')
    context={'task':form}
    return render(request, 'html/update.html', context=context)


# -- Delate user --
@login_required(login_url='login_user')
def delete_user(request,pk):
    task=User_info.objects.get(user_id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('view')
    context={'task':task}
    return render(request, 'html/delete.html', context=context)


