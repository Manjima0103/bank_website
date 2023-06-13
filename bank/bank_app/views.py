# views.py
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import json

from .forms import BankForm


def home(request):
    return render(request, "home.html")


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already taken. Please choose a different username.")
            else:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, "Registration successful. Please login.")
                return redirect("bank_app:login")
        else:
            messages.error(request, "Passwords do not match")

    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('bank_app:new_page')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


BRANCH_CHOICES = {
    'Kasaragod': ['Branch A', 'Branch B', 'Branch C'],
    'Kannur': ['Branch D', 'Branch E', 'Branch F'],
    'Kozhikode': ['Branch G', 'Branch H', 'Branch I'],
    'Wayanad': ['Branch J', 'Branch K', 'Branch L'],
    'Malappuram': ['Branch M', 'Branch N', 'Branch O'],
}


def form_submission(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application accepted.')
            return redirect('bank_app:success')
    else:
        form = BankForm()

    return render(request, 'new_page.html', {'form': form})


def success_page(request):
    return render(request, 'success.html')


def new_page(request):
    districts = ['Kasaragod', 'Kannur', 'Kozhikode', 'Wayanad', 'Malappuram']
    form = BankForm()
    context = {'form': form, 'districts': districts, 'BRANCH_CHOICES_JSON': json.dumps(BRANCH_CHOICES),
               'messages': messages.get_messages(request)}
    return render(request, "new_page.html", context)


def logout(request):
    auth_logout(request)
    return redirect("/")


def branches(request):
    # Handle branches dropdown functionality
    return render(request, "branches.html")


def district_wikipedia(request, district):
    wikipedia_url = f"https://en.wikipedia.org/wiki/{district}"
    return redirect(wikipedia_url)



