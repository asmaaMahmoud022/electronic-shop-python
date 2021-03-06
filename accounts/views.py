from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
# from .forms import SignUpForm
from django.contrib.auth.models import User
from .forms import RegisterForm
# Create your views here.

# def sign_up(request):
#     if request.method == "POST":
#         # form = UserCreationForm(request.POST)
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             first_name = form.cleaned_data.get('first_name')
#             last_name = form.cleaned_data.get('last_name')
#             email = form.cleaned_data.get('email')
#             user.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect('home/')
#         else:
#             print(form.errors)
#             return HttpResponse(form.errors)    
#     else:
#         # form = UserCreationForm()
#         form = SignUpForm()
#         return render(request, 'sign_up.html',{'form' : form})




def sign_up(request):
    # if this is a POST request we need to process the form data
    template = 'sign_up.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.phone_number = form.cleaned_data['phone_number']
                user.save()
               
                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return redirect('home/')
        else:
            print(form.errors)
            return HttpResponse(form.errors)          

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    # return render(request, template, {'form': form})
        return render(request, template, {'form' : form})