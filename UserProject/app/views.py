from django.shortcuts import render
from app.forms import UserForm, UserProfileInfoForm
# login imports
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,'app/index.html',context={'title':'Home'})

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save() # creating a user
            user.set_password(user.password) # hashes the password
            user.save() # save changes

            profile = profile_form.save(commit=False) # creates profile but doesn't save to database
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save() # save changes
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else: # not filled out
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context_dict = {'title':'Registration',
                    'registered': registered,
                    'user_form': user_form,
                    'profile_form': profile_form}

    return render(request,'app/registration.html',context=context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password) # built in

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else: # inactive account
                return HttpResponse("Account not active")
        else: # failed login
            return HttpResponse("invalid login")
    else:
        return render(request,'app/login.html')

    return render(request,'app/index.html',context={'title':'Login'})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
