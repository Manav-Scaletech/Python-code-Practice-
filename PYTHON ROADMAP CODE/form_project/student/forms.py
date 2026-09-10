from django import forms

class StudentForm(forms.Form):

    name = forms.CharField(max_length=100)

    email = forms.EmailField()

    age = forms.IntegerField()

    password = forms.CharField(widget=forms.PasswordInput())