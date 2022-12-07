from django.shortcuts import render, redirect
from users.forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from users.utils import get_user_from_request
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.views import LogoutView


class LoginView(CreateView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class,
            'user': get_user_from_request(self.request)
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('/products')
            else:
                form.add_error('username', 'bad request')

        return render(request, self.template_name, context=self.get_context_data(form=form))


class LogoutViews(LogoutView):
    def get(self, request, *args, **kwargs): # Вот тут я сначала сделал метод post, но меня после выхода перекидывало
        logout(request)                      # в админку, а с методом get работает так как работало с функциональной вью
        return redirect('/products')


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'form': kwargs['form'] if kwargs.get('form') else self.form_class
        }

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            if form.cleaned_data.get('password') == form.cleaned_data.get('repeat'):
                user = User.objects.create_user(
                    username=form.cleaned_data.get('username'),
                    password=form.cleaned_data.get('password')
                )
                login(request, user)
                return redirect('/products')
            else:
                form.add_error('password', 'password do not match!')

        return render(request, self.template_name, context=self.get_context_data(form=form))
