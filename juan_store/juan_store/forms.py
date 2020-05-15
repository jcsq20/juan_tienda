from django import forms
#from django.contrib.auth.models import User
from users.models import User

class RegisterForm(forms.Form):
    username =  forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    "class": "form-control",
                                    "id": "username",

                                }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                    "class": "form-control",
                                    "id": "email",
                                    "placeholder": "example@gmail.com"
                                }))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    "class": "form-control",
                                }))

    password2 = forms.CharField(label="confirmar contraseña",
                            required=True,
                            widget=forms.PasswordInput(attrs={
                                "class": "form-control",
                            }))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("el usuario ya se encuentra registrado")
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError("el email ya se encuentra registrado")
        else:
            return email

    def clean(self): # seutiliza para verificar algo solo cuando algo depende de algo 
        cleaned_data = super().clean()
        if cleaned_data.get("password2")!= cleaned_data.get("password"):
            self.add_error("password2","La contraseña no coindice")

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get("username"),
            self.cleaned_data.get("email"),
            self.cleaned_data.get("password")
             )