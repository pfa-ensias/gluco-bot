from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm
from diabetes.models import Appointment, Diet, Bloodsugar, Weight



def login_user(request, *args, **kwargs):

    if request.method =='POST':
        username = request.POST['username'] # get from html name
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            # Redirect to a success page.
        else:
            messages.success(request,('unsuccess login, please try again!!'))
            return redirect('/members/login_user/')

    else:
            return render(request, "authentication/login.html", {})



def logout_user(request, *args,**kwargs):
   logout(request)
   messages.success(request, ('You were logged out!'))

   return redirect('home')




def register_view(request, *args,**kwargs):
    # if request == 'POST':
    logout(request)
    form = RegisterForm()
    context = {
        'form': form
    }
    if request.method =='POST':
        form = RegisterForm(request.POST)
        context['form'] = form

        if  form.is_valid(): #form is cleaned
            form.save()
            messages.success(request,('You have registed!'))
            form = RegisterForm() #re-render it after save

        else:
            messages.success(request, ('Unsuccess register!'))
            form = RegisterForm() #re-render it after save


    return render(request, "register/register.html", context)