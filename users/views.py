from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#from .things import retrive

import urllib3
import urllib.request
import re
from urllib3 import request
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    data_read = urllib.request.urlopen('https://api.thingspeak.com/channels/866457/feeds.json?api_key=ORN9IAZY7TR3K55V&results=2')
    #print(data_read.read())
    select = repr(data_read.read())
    #select = select[384:388]
    #select = select[400:405]
    select = select[300:]
    #print(select)
    #return select
    pick = re.search('field1":"(.+?)",',select)
    a = str(pick)[48:51]
    if a == int(100):
        a = str(pick)[48:51]
    else:
        a = str(pick)[48:50]
    #if pick:
     #   print(pick.group(1));
    #print(str(pick)[48:51])
     
        
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {
        'u_form': u_form,
        'p_form':p_form,
        'data':a

            }
    return render(request, 'users/profile.html', context)

