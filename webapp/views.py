from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from api.models import Organization
from .filters import OrganizationFilter
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def loginView(request):
    message = None
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            message = 'Enter a Valid Username and Password'
    return render(request, 'webapp/login.html', {
        "message" : message
    })

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required(login_url='login')
def index(request):
    orgs = Organization.objects.all()
    filter = OrganizationFilter(request.GET, queryset=orgs)
    orgs = filter.qs

    return render(request, 'webapp/home.html', {
        "orgs" : orgs,
        'filter' : filter
    })

