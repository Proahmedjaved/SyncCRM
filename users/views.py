from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('leads:index')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})
