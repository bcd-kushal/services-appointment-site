from datetime import datetime, timedelta

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




def get_available_timeslots():
    available_timeslots = [
        "7:30AM",
        "8:15AM",
        "9:00AM",
        "7:00PM",
        "1.30PM",
        "7:40PM",
        "8:20PM",
        "9:00PM",
        "9:40PM",
        "10:20PM",
        "11:00PM",
        "11:40PM",
    ]

    return available_timeslots