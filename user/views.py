from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView


signup = CreateView.as_view(
    form_class=UserCreationForm,
    template_name = "user/user_form.html",
    # success_url = settings.LOGIN_URL,
    success_url = "/user/signin/"
)

signin = LoginView.as_view(
    template_name = "user/user_form.html",
    # success_url = settings.LOGIN_REDIRECT_URL,
    success_url = "/"
)

signout = LogoutView.as_view(
    next_page="/"
)