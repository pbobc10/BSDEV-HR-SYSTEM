from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username',required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))