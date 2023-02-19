from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from users.forms import RegisterForm, InfoUserForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    form = InfoUserForm(instance=request.user, data=request.POST)
    if form.is_valid():
        form.save()
    else:
        print(form.errors)
    context = {'form': form}
    return render(request, 'users/profile.html', context)



