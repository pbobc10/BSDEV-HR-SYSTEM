from django.shortcuts import render, HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from ..forms.user_form import LoginForm
from django.contrib.auth.models import User


# Create your views here.
# if no user is signed in, return to login page:
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('accounts:login'))
    # send users to dashboard page
    return HttpResponseRedirect(reverse('hrSystem:dashboard'))

def login_view(request):
    form = LoginForm()
    message=''
    if request.method == 'POST':
        # Accessing username and password from form data
        username = request.POST['username']
        password = request.POST['password']

        # check if username and password are correct, returning User object if so
        user = authenticate(request,username=username,password=password)

        # if user object is returned, log in and route to dashboard page:
        if user is not None :
           
            if user.last_login is not None :
                login(request,user)# create session
                # Get the value of the "next" parameter from the request's GET data
                next_url = request.GET.get('next')
                if next_url is not None:
                    return HttpResponseRedirect(next_url)
                else:
                    return HttpResponseRedirect(reverse('hrSystem:dashboard'))
            else:
                # Redirect to change password page for first time login
                login(request,user)# create session
                force_password_change(user.id)
                # Redirect to change password page for first time login
                return redirect ('accounts:change_password')
            
                
        # otherwise, return login page again with new context
        else:
            message='username or password is incorrect'
            
    #send user to login page
    context = {'form':form,'message':message}
    return render(request,'registration/login.html',context)

def force_password_change(user_id):
    user = User.objects.get(id=user_id)
    user.force_password_change = True
    user.save()   

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
