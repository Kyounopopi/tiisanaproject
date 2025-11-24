from django.contrib.auth.forms import UserCreationForm
from .models import Customuser

class CustomUserCreationForm(UserCreationForm):
    model = Customuser
    fields = ('email', 'password_1', 'password_2')
