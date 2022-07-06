from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import FormView
from django.contrib.auth import login, logout
from accounts.forms import UserCreateForm, LoginCreateForm


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    form_class = LoginCreateForm
    success_url = 'bookstore'
    template_name = 'registration/login.html'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


class LogoutFormView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))
