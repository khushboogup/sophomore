from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
def Home(request):
    return render(request,'base/home.html')
def loginPage(request):
    page="login"
    if request.user.is_authenticated:
        return redirect('Home')
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request, "Not a user")
    context={"page":page}
    return render(request,'base/login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('Home')
def registerUser(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('Home')
        else:
            messages.error(request, "Not a user")
    return render(request,'base/login.html',{'form':form})
