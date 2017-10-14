from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from innstal.forms import UserRegistrationForm

from .models import Product

# from innstal import models

# from .models import Greeting

# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    # return HttpResponse('Hello from Python!')

    products = Product()

    products = Product.objects.all()

    return render(request, 'index.html', {'products' : products})

def login(request):
	return render(request, 'login.html')

def register_warrantly(request):
	return render(request, 'register_warrantly.html')

def pricing(request):
	return render(request, 'pricing.html')

def about(request):
	return render(request, 'about.html')

def service(request):
	return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')

def search_result(request):
    products = Product()

    products = Product.objects.all()

    return render(request, 'search_result.html', {'products' : products})

# def db(request):

#     greeting = Greeting()
#     greeting.save()

#     greetings = Greeting.objects.all()

#     return render(request, 'db.html', {'greetings': greetings})

