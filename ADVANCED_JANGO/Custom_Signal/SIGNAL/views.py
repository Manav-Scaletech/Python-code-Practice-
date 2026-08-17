from django.shortcuts import render , HttpResponse 
from SIGNAL import signals

# # Create your views here.
# def home(request):
#     signals.notification.send(sender = None , request = request , user = ['custom' , 'signals'])
#     return HttpResponse("here is the home page that you are looking for")


def home(request):
    count = request.session.get("page_count", 0) + 1
    request.session["page_count"] = count

    if count % 2 == 0:
        signals.notification.send(
            sender=None,
            request=request,
            user=['custom', 'signals']
        )

    return HttpResponse(f"Page loaded {count} times")


# this one for the testing exception task and codefile is tests.py
class ForbiddenException(Exception):
    pass


def is_user_allowed(user):
    if user.is_admin:
        return True

    raise ForbiddenException("User is not an admin")