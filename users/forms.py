from django.contrib.auth.models import User
from django import forms
from .models import User


class LoginForm(forms.Form):
    email = forms.EmailField(label="Enter email")
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = User.objects.get(username=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password Incorrect"))
        except:
            self.add_error("email", forms.ValidationError("User Doesn't Exist"))

        return email

    def save(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")


class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(label="Enter email")
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput)
    password1 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("User Already exists")
        except User.DoesNotExist:
            return email

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password = self.cleaned_data.get("password")
        if password1 != password:
            raise forms.ValidationError(
                "Password and Confirmation Password does not match."
            )
        else:
            return password1

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        createdUser = User.objects.create_user(email, email, password)
        createdUser.first_name = first_name
        createdUser.last_name = last_name
        createdUser.save()