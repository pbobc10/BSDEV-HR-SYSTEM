from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username',required=True)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)