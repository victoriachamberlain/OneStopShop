from django import forms

class RegisterForm(forms.Form):
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)
    email = forms.EmailField()
    birth_date = forms.DateField()
    password = forms.CharField(max_length = 200, widget=forms.PasswordInput)
    confirm_pw = forms.CharField(max_length = 200, widget=forms.PasswordInput)
