from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from discodesocial.models import Publicacion

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget = forms.TextInput(attrs={'class':'form__input', 'type':'text', 'placeholder':' '}), required = True)
    email = forms.EmailField(label='', widget = forms.EmailInput(attrs={'class':'form__input', 'type':'email', 'placeholder':' '}), required = True)
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form__input', 'placeholder':' '}), required = True)
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form__input', 'placeholder':' '}), required = True)

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }


class PostForm(forms.ModelForm):
    contenido = forms.CharField(label = '', widget = forms.Textarea(attrs={'class':'form__textarea', 'placeholder':'¿Que estas pensando?'}), required = True)

    class Meta:
        model = Publicacion
        fields = ['contenido']