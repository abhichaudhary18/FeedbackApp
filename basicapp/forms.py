from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Sendmessage


class UserCreateForm(UserCreationForm):
    first_name = forms.CharField(max_length=32,required = True)
    last_name = forms.CharField(max_length=32,required = True)
    email = forms.EmailField(max_length=64, help_text='Enter a valid email address',required= True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # I've tried both of these 'fields' declaration, result is the same
        # fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

class Sendmessage(forms.ModelForm):
    class Meta:
        model = Sendmessage
        fields = "__all__"
