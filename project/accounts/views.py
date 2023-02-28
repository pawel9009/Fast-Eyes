from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect

from . import forms


# class SignUp(generic.CreateView):
#     form_class = forms.UserCreateForm
#     success_url = reverse_lazy('login')
#     template_name = 'accounts/signup.html'



def register(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            # Przetwórz pomyślnie utworzonego użytkownika
            return redirect('home')
    else:
        form = forms.UserCreateForm()
    return render(request, 'accounts/signup.html', {'form': form})