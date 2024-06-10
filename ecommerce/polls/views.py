from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm
from .models import Product

def Index(request):
    all_products = Product.objects.all()
    return render(request, 'polls/index.html', {'products': all_products})

def Mbrid(request):
    return render(request, 'polls/Mbrid.html')

def Charbrid(request):
    return render(request, 'polls/Charbrid.html')


def Sunbrid(request):
    return render(request, 'polls/Sunbrid.html')


def Skybrid(request):
    return render(request, 'polls/Skybrid.html')


def Harmbrid(request):
    return render(request, 'polls/Harmbrid.html')

def About(request):
    return render(request, 'polls/about.html')

def Contact(request):
    return render(request, 'polls/contact.html')


def Gallery(request):
    return render(request, 'polls/Gallery.html')

def Cart(request):
    return render(request, 'polls/Cart.html')

def Payment(request):
    return render(request, 'polls/Payment.html')

def Description(request):
    return render(request, 'polls/Description.html')

def Videog(request):
    return render(request, 'polls/Videog.html')








def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'polls/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Redirect to the homepage after login
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'polls/login.html')
