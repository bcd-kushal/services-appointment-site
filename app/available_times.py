from datetime import datetime, timedelta

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

ATLAS_URI = "MONGODB_URI"



def ascending_times(arr):
    sorted_arr = datetime.strptime(arr, "%I:%M%p")
    return sorted_arr


#=======================================================

def get_available_dates():
    # what we do is get next 7 days of weekends
    today = datetime.today()
    
    next_saturday = today + timedelta(days=(5 - today.weekday() + 7) % 7)
    next_sunday = today + timedelta(days=(6 - today.weekday() + 7) % 7)

    available_dates = []

    for _ in range(7):
        available_dates.append({
                                "day": "Sat",
                                "date": next_saturday.strftime('%d %b')
                            })
        available_dates.append({
                                "day": "Sun",
                                "date": next_sunday.strftime('%d %b')
                            })
        next_saturday += timedelta(days=7)
        next_sunday += timedelta(days=7)

    return available_dates









def get_db_dateslots():
    mongo_client = MongoClient(ATLAS_URI,server_api = ServerApi('1'))
    
    atlas_db = mongo_client.get_database("booking_site")
    data = atlas_db.timeslots

    available_timeslots = data.find_one({ "dateslots": { "$exists": True } })

    return available_timeslots["dateslots"]








def get_db_timeslots():
    mongo_client = MongoClient(ATLAS_URI,server_api = ServerApi('1'))
    
    atlas_db = mongo_client.get_database("booking_site")
    data = atlas_db.timeslots

    available_timeslots = data.find_one({ "timeslots": { "$exists": True } })

    return available_timeslots["timeslots"]






def get_available_timeslots():
    # update_dates()   
    available_timeslots = get_db_timeslots() 
    return available_timeslots











#==================================================================================
#==============[ CREATE / UPDATE SECTION ]=========================================
#================================================================================== 


# BOOK TIME SLOT ==================================================================
def book_timeslot(date,time):
    mongo_client = MongoClient(ATLAS_URI,server_api = ServerApi('1'))
    
    atlas_db = mongo_client.get_database("booking_site")
    data = atlas_db.timeslots

    available_timeslots = data.find_one({ "timeslots": { "$exists": True } })
    available_timeslots = available_timeslots["timeslots"][date]

    if time in available_timeslots:
        booked_slots = data.find_one({ "booked_slots" : { "$exists": True } })
        booked_slots = booked_slots["booked_slots"][date]


        available_timeslots.remove(time)
        if time not in booked_slots:
            booked_slots.append(time)
            booked_slots = sorted(booked_slots, key=ascending_times)

        # now update available timeslots with this
        data.update_one(
            {"timeslots.{}".format(date): {"$exists": True}},
            {"$set": {"timeslots.{}".format(date): available_timeslots}}
        )
        
        # now update booked timeslots with this
        data.update_one(
            {"booked_slots.{}".format(date): {"$exists": True}},
            {"$set": {"booked_slots.{}".format(date): booked_slots}}
        )








# CANCEL TIME SLOT ==================================================================
def cancel_timeslot(date,time):
    mongo_client = MongoClient(ATLAS_URI,server_api = ServerApi('1'))
    
    atlas_db = mongo_client.get_database("booking_site")
    data = atlas_db.timeslots

    booked_timeslots = data.find_one({ "booked_slots": { "$exists": True } })
    booked_timeslots = booked_timeslots["booked_slots"][date]

    if time in booked_timeslots:
        available_slots = data.find_one({ "timeslots" : { "$exists": True } })
        available_slots = available_slots["timeslots"][date]


        booked_timeslots.remove(time)
        if time not in available_slots:
            available_slots.append(time)
            available_slots = sorted(available_slots, key=ascending_times)

        # now update booked timeslots with this
        data.update_one(
            {"booked_slots.{}".format(date): {"$exists": True}},
            {"$set": {"booked_slots.{}".format(date): booked_timeslots}}
        )
        
        # now update available timeslots with this
        data.update_one(
            {"timeslots.{}".format(date): {"$exists": True}},
            {"$set": {"timeslots.{}".format(date): available_slots}}
        )








# UPDATE DATES ==================================================================
def update_dates():
    current_dates = get_available_dates()
    date_list = [ entry['date'] for entry in current_dates ]


    print("\n\n\n ===========================\n\n")
    print("date_list =", date_list)

    mongo_client = MongoClient(ATLAS_URI,server_api = ServerApi('1'))
    
    atlas_db = mongo_client.get_database("booking_site")
    data = atlas_db.timeslots

    prev_dates = data.find_one({ "dateslots": { "$exists": True } })
    prev_dates = prev_dates["dateslots"]
    prev_dates = [ entry['date'] for entry in prev_dates ]

    
    print("\nprev_dates =", prev_dates)

    # now update dates
    data.update_one(
        {"dateslots": {"$exists": True}},
        {"$set": {"dateslots": current_dates}}
    )

    print("\n====================> UPDATED 1")

    # then update booked slots and timeslots date keys
    n = len(date_list)
    for i in range(0,n):

        if date_list[i] in prev_dates:
            continue

        data.update_many(
            { f"booked_slots.{prev_dates[i]}": { "$exists": True } },
            { "$rename": { f"booked_slots.{prev_dates[i]}": f"booked_slots.{date_list[i]}" } }
        )
        data.update_many(
            { f"timeslots.{prev_dates[i]}": { "$exists": True } },
            { "$rename": { f"timeslots.{prev_dates[i]}": f"timeslots.{date_list[i]}" } }
        )
        
        print("\n====================> UPDATED",i+2)
        
    print("\n====================> UPDATED N")
        

