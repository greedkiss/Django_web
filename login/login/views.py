from django.shortcuts import render,redirect

from django.http import HttpResponse

from django import forms

def run(request):
    return render(request, 'login.html')


def login(request):
    error_meg = ""

    if request.method == "POST":
        user = request.POST.get('username', None)
        pwd = request.POST.get('pwd', None)

        if user == 'root' and pwd == 'admin':
            return render(request, 'home.html')
        else:
            error_meg = "用户名或密码错误"
            return render(request, 'login.html', {'error_msg':error_meg})


def home(request):
    return render(request, 'home.html')




