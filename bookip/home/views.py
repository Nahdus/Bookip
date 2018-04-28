from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.


   
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                
                return redirect('booklist:recent')
            else:
                return render(request, 'home/login_page.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'home/login_page.html', {'error_message': 'Invalid login'})
    elif request.method == "get":
        return redirect('home:login_user')
    return render(request, 'home/login_page.html')




