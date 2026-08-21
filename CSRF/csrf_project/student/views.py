from django.shortcuts import render


def index(request):

    if request.method == "POST":

        name = request.POST.get("name")

        return render(
            request,
            "index.html",
            {"message": f"Welcome {name}"}
        )

    return render(request, "index.html")