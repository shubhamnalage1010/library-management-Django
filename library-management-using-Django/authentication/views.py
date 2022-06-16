from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from bookrecord.views import Book

def home(request):

    return render(request, 'home.html')


def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        user = User.objects.create_user(first_name = fname, last_name = lname,  username = username, email = email, password = pass1)
        user.save()
        return redirect('signin')

    else:
        return render(request, 'signup.html')


def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username =username , password = pass1)

        if user is not None :
            login(request, user)

            return redirect('addshow')
        else:
            return redirect('signup')

    return render(request, 'signin.html')



def signout(request):
    logout(request)
    
    return redirect('signin')

    


""" student view only Here student can't modify anythhing """
def student(request):
    books = Book.objects.all()
    return render(request, 'students.html',{'books':books})

