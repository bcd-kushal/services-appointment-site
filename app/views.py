from django.shortcuts import render

import time
import threading
import json
import re
import razorpay

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

        timeslots = get_available_timeslots()
        dateslots = get_available_dates()

        default_times = timeslots[dateslots[0]["date"]]

        props = {

            "booking_name": targeted_booking["booking_name"],
            "booking_price": targeted_booking["price"],
            "booking_duration": targeted_booking["time"],
            "booking_desc": targeted_booking["desc"],

            "available_dates": dateslots,
            "available_timeslots": default_times,
            "all_timeslots": timeslots,


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

        print(f"\n\n===================> {selected_date}, at {selected_time} ......... type = {booking_id} \n\n")

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
            "booking_time": f"{selected_date} | {selected_time} (GMT +05:30)",
            "meet_date": selected_date,
            "meet_time": selected_time,
            "meet_length": x["duration"]
        } 
        return render(req, "src/payment.html", props)
    
    else:
        return send_bad_request(req)
    



# @/payment-process/
def process_payment(req):
    if req.method == "POST":
        # get form data for paymenting
        name = req.POST.get("customer_name")
        email = req.POST.get("customer_email")
        about = req.POST.get("customer_call_details")
        mobile = int(req.POST.get("customer_mobile") or -1)
        amount = int(req.POST.get("pay_amount"))
        meet_type = req.POST.get("meet_type")
        meet_date = req.POST.get("meet_date")
        meet_time = req.POST.get("meet_time")
        meet_length = req.POST.get("meet_length")
        recieve_updates = req.POST.get("get_mail_update")
        

        if mobile == -1:
            mobile = None


        props_success = {
            "svg": '<svg xmlns="http://www.w3.org/2000/svg" style="scale:1.2;fill:#008000;"  height="16" width="16" viewBox="0 0 512 512"><path d="M256 48a208 208 0 1 1 0 416 208 208 0 1 1 0-416zm0 464A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM369 209c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-111 111-47-47c-9.4-9.4-24.6-9.4-33.9 0s-9.4 24.6 0 33.9l64 64c9.4 9.4 24.6 9.4 33.9 0L369 209z"/></svg>',
            "msg_color": "green",
            "message": "Payment Successful",
            "link": "/",
            "link_msg": "Go Home"
        }
        props_failure = {
            "svg": '<svg xmlns="http://www.w3.org/2000/svg" style="scale:1.2;fill:#ff0000;" height="16" width="16" viewBox="0 0 512 512"><path d="M256 48a208 208 0 1 1 0 416 208 208 0 1 1 0-416zm0 464A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM175 175c-9.4 9.4-9.4 24.6 0 33.9l47 47-47 47c-9.4 9.4-9.4 24.6 0 33.9s24.6 9.4 33.9 0l47-47 47 47c9.4 9.4 24.6 9.4 33.9 0s9.4-24.6 0-33.9l-47-47 47-47c9.4-9.4 9.4-24.6 0-33.9s-24.6-9.4-33.9 0l-47 47-47-47c-9.4-9.4-24.6-9.4-33.9 0z"/></svg>',
            "msg_color": "red",
            "message": "Unsuccessful Payment",
            "link": "/",
            "link_msg": "Go Home"
        }





        # rzp_item = meet_type
        # rzp_amount = amount * 100 
        
        # client = razorpay.Client(auth=('rzp_test_i2Olh4B1BnBa6y','My7JEHHTovYfiSo4OlGUlVQg'))
        # payment = client.order.create({
        #         'amount':amount,
        #         'currency':"INR",
        #         'payment_capture': '1'
        # })

        # print(payment)

        # return render(req,"src/payment_status.html",{
        #     "payment": payment,
        #     "theme": '#715fbe'
        # })




            

        PAYMENT_SUCCESS = True

        if PAYMENT_SUCCESS:
            # remove this timeslot from available
            # add this to booked slot
            book_timeslot(date=meet_date[:6],time=meet_time)

            
        

            # add booking details
            add_new_booking(name=name,
                        email=email,
                        about=about,
                        amount=amount,
                        mobile=mobile,
                        payment_status=False,
                        meeting={
                            'date': meet_date,
                            'time': meet_time,
                            'type': meet_type,
                            'length': meet_length
                        },
                        recieve_updates = recieve_updates
                    )
        
            return render(req,"src/payment_status.html",props_success)



        else:
            return render(req,"src/payment_status.html",props_failure)
        

    else:
        return send_bad_request(req)



def send_bad_request(req):
    return render(req, "src/404.html")