from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "account_id",
            "email",
            "name",
        )

# ログインフォームを追加
class LoginForm(AuthenticationForm):
    class Meta:
        model = User