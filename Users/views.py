from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm,UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Dear {username}, Your account has been created successfully!')
            return redirect('blog-login')
        # else:
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    return render(request, 'users/profile.html', dict(u_form=u_form, p_form=p_form))


