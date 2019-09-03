from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Dear {username}, Your account has been created successfully!')
            return redirect('Blog:blog-home')
        # else:
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
