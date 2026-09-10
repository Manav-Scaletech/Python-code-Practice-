from django import forms
from django.core.exceptions import ValidationError


class StudentForm(forms.Form):

    name = forms.CharField(

        max_length=50,

        min_length=3

    )

    email = forms.EmailField()

    age = forms.IntegerField(

        min_value=18

    )

    password = forms.CharField(

        min_length=8,

        widget=forms.PasswordInput()

    )

    confirm_password = forms.CharField(

        widget=forms.PasswordInput()

    )

    # Field Validation

    def clean_name(self):

        name = self.cleaned_data["name"]

        if not name.isalpha():

            raise ValidationError(

                "Name should contain only alphabets."

            )

        return name

    # Form Validation

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")

        confirm = cleaned_data.get("confirm_password")

        if password != confirm:

            raise ValidationError(

                "Passwords do not match."

            )

        return cleaned_data