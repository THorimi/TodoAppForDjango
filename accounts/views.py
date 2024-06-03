from django.contrib.auth import login, logout, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .forms import SignUpForm, LoginForm


class IndexView(TemplateView):
    template_name = "todo/index.html"


class SignupView(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:index")

    def form_valid(self, form):
        # login after signup
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        login(self.request, user)
        return response
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "アカウント新規登録"
        return context


class LoginView(BaseLoginView):
    form_class = LoginForm
    template_name = "accounts/login.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "ログインページ"
        return context

def logout_view(request):
    logout(request)
    return redirect('accounts:login')