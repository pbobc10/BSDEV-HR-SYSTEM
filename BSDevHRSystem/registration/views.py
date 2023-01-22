from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .user_form import LoginForm

# Create your views here.
# if no user is signed in, return to login page:
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('registration:login'))
    # send users to dashboard page
    return HttpResponse('<h1 style="width:160px;heigh:200px;">Bonjour</h1>')

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        # Accessing username and password from form data
        username = request.POST['username']
        password = request.POST['password']

        # check if username and password are correct, returning User object if so
        user = authenticate(request,username=username,password=password)

        # if user object is returned, log in and route to dashboard page:
        if user:
            login(request,user)
            return HttpResponseRedirect(reverse('registration:index'))
        # otherwise, return login page again with new context
        else:
            return render(request,'registration/login.html',{
                'message':'Your username and password dind''t match',
                'form':form,
            })
    #send user to login page
    context = {'form':form}
    return render(request,'registration/login.html',context)

def logout_view(request):
    logout(request)
    return render(request,'registration/login.html',{
        'message':'Logged Out'
        })
