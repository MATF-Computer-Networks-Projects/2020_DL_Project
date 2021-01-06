from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    # user = authenticate(request, username=username)
    # if user is not None:
    return render(request, 'chat/index.html')
    # else:
    #     print("Not working")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User successfully created!') 
                return redirect('login')

        context = {
            'form': form
            }
        return render(request, 'chat/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Username or password is incorrect")
                return render(request, 'chat/login.html')

        context = {}
        return render(request, 'chat/login.html')
    
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })