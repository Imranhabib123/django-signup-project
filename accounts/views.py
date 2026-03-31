from django.shortcuts import render, redirect
from .forms import SignupForm

def signup_view(request):
    if request.method == 'POST':             # when button clicked the POST method works through link GET method
        form = SignupForm(request.POST)      # works.
        if form.is_valid():
            form.save()
            return redirect('signup_success')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def signup_success(request):
    return render(request, 'accounts/signup_success.html')
