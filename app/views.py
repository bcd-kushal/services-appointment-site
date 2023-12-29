from django.shortcuts import render

import time
import threading

from django.shortcuts import render, redirect
from django.conf import settings
# from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate as default_authenticate, login as LoginUser, logout as LogoutUser
# from django.contrib.auth.models import User as RegisteredUsers
from django.contrib.auth.views import LoginView


from .bookings import get_booking_types



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApiVersion

ATLAS_URI = ""

#================================================================
#================================================================

# @/
def homepage(req):
    if req.method == "GET":
        props = {
            "bookings": get_booking_types()
        } 
        return render(req, "src/main.html", props)
    
    else:
        return send_bad_request(req)
    


# @/datepick
def datepick(req):
    if req.method == "POST":
        props = {

        } 
        return render(req, "src/datepick.html", props)
    
    else:
        return send_bad_request(req)
    



# @/payment
def payment(req):
    if req.method == "GET":
        props = {

        } 
        return render(req, "src/payment.html", props)
    
    else:
        return send_bad_request(req)
    



def process_payment(req):
    pass





def send_bad_request(req):
    return render(req, "src/404.html")