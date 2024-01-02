from django.shortcuts import render

import time
import threading
import json
import re

from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth import authenticate as default_authenticate, login as LoginUser, logout as LogoutUser
# from django.contrib.auth.models import User as RegisteredUsers
from django.contrib.auth.views import LoginView


from .bookings import *
from .available_times import *


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApiVersion

ATLAS_URI = ""


def extract_numbers_from_string(input_string):
    num = 0
    for i in range(0,len(input_string)):
        if(input_string[i] in ['0','1','2','3','4','5','6','7','8','9']):
            num = num*10 + int(input_string[i])

    return num

#================================================================
#================================================================

# @/
def homepage(req):
    if req.method == "GET":
        print(get_booking_types())
        props = {
            "bookings": get_booking_types()
        } 
        return render(req, "src/main.html", props)
    
    else:
        return send_bad_request(req)
    


# @/date-pick/
def goto_datepick(req):
    return redirect('/date-pick/1/')




# @/date-pick/<int:id>/
def datepick(req,id=1):
    if req.method == "GET":
        id = int(id) if id is not None else 1

        targeted_booking = target_booking(id-1)
        props = {

            "booking_name": targeted_booking["booking_name"],
            "booking_price": targeted_booking["price"],
            "booking_duration": targeted_booking["time"],
            "booking_desc": targeted_booking["desc"],

            "available_dates": get_available_dates(),
            "available_timeslots": get_available_timeslots(),


            "bookings": show_all_booking_types(id-1)

        } 
        return render(req, "src/datepick.html", props)
    
    else:
        return send_bad_request(req)
    



# @/payment/
def payment(req):
    if req.method == "POST":

        selected_date = req.POST.get("selected_date")
        selected_time = req.POST.get("selected_time")
        booking_id = req.POST.get("booking_id")

        # print(f"\n\n===================> {selected_date}, at {selected_time} ......... type = {booking_id} \n\n")

        x = target_booking(int(booking_id)-1)
        price = extract_numbers_from_string(x["price"])

        prices = [
            "₹ "+str(price),
            "₹ "+str(int(price*1.05)),
            "₹ "+str(int(price*1.2)),
            "₹ "+str(int(price*1.5))
        ]



        props = {
            "booking_name": x["booking_name"],
            "booking_details": x["type"] + ", " + x["duration"],
            "booking_price": x["price"],
            "prices": prices,
            "booking_time": f"{selected_date} | {selected_time} (GMT +05:30)"
        } 
        return render(req, "src/payment.html", props)
    
    else:
        return send_bad_request(req)
    



def process_payment(req):
    pass





def send_bad_request(req):
    return render(req, "src/404.html")