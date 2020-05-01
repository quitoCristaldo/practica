from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def inicio(request):
    return render(request=request,
     template_name='main/aviso.html',
     context= {})

def logout_request(request):
    logout(request)
    messages.success(request, "Adios!!")
    return redirect("main:inicio")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  
                messages.success(request, f"bienvenido {username}")
                return redirect('/productos')
            else:
                messages.error(request, "usuario y/o contraseña invalidos ") 

        else:
            messages.error(request, "usuario y/o contraseña invalidos ")  

    form = AuthenticationForm()
    return render(  request=request,
                    template_name='main/login.html',
                    context= {"form":form})
