from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse, reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # user = User.objects.get(request.user)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            print(request.user)
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, Your account is created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')