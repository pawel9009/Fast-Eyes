from django.shortcuts import redirect, render

from . import forms


def register(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('home')
    else:
        form = forms.UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})
