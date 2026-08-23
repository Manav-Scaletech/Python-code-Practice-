from django.shortcuts import render

from .forms import StudentForm

from .models import Student


def register(request):

    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():

            Student.objects.create(

                name=form.cleaned_data["name"],

                email=form.cleaned_data["email"],

                age=form.cleaned_data["age"],

                password=form.cleaned_data["password"]

            )

            return render(

                request,

                "register.html",

                {

                    "form": StudentForm(),

                    "message": "Registration Successful"

                }

            )

    else:

        form = StudentForm()

    return render(

        request,

        "register.html",

        {

            "form": form

        }

    )