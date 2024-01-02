ALL_BOOKINGS = [
        {
            "booking_name": "Quick Chat",
            "index": "1",
            "tag": "1:1 Call",
            "time": "30 mins meeting",
            "duration": "30 mins",
            "type": "Video Meeting",
            "price": "₹ 500 +",
            "slashed_price": None,
            "desc": """
                In client interactions, I provide targeted technical insights and 
                career guidance. Drawing on my expertise, I deliver clear 
                explanations on emerging technologies and industry trends. 
                Whether discussing software development or IT infrastructure,
                 I aim to empower clients with informed decision-making. 
                 Additionally, I offer personalized career advice, assisting 
                 individuals in aligning their skills with evolving industry 
                 demands. Through these conversations, I strive to create a 
                 supportive environment where clients feel confident in both 
                 their technical choices and career trajectories.
            """
        },


        
        {
            "booking_name": "Mock Interview",
            "index": "2",
            "tag": "1:1 Call",
            "time": "60 mins meeting",
            "duration": "60 mins",
            "type": "Video Meeting",
            "price": "₹ 1,100 +",
            "slashed_price": "I can help create a few mock question papers for tech stuffs if needed",
            "desc": """
                In client interactions, I provide targeted technical insights and 
                career guidance. Drawing on my expertise, I deliver clear 
                explanations on emerging technologies and industry trends. 
                Whether discussing software development or IT infrastructure,
                 I aim to empower clients with informed decision-making. 
                 Additionally, I offer personalized career advice, assisting 
                 individuals in aligning their skills with evolving industry 
                 demands. Through these conversations, I strive to create a 
                 supportive environment where clients feel confident in both 
                 their technical choices and career trajectories.
            """
        },


        
        {
            "booking_name": "Interview prep & tips",
            "index": "3",
            "tag": "1:1 Call",
            "time": "45 mins meeting",
            "duration": "45 mins",
            "type": "Video Meeting",
            "price": "₹ 650 +",
            "slashed_price": "I can take a demo interview for you for better confident",
            "desc": """
                In client interactions, I provide targeted technical insights and 
                career guidance. Drawing on my expertise, I deliver clear 
                explanations on emerging technologies and industry trends. 
                Whether discussing software development or IT infrastructure,
                 I aim to empower clients with informed decision-making. 
                 Additionally, I offer personalized career advice, assisting 
                 individuals in aligning their skills with evolving industry 
                 demands. Through these conversations, I strive to create a 
                 supportive environment where clients feel confident in both 
                 their technical choices and career trajectories.
            """
        },


        
        {
            "booking_name": "Career guidance",
            "index": "4",
            "tag": "1:1 Call",
            "time": "30 mins meeting",
            "duration": "30 mins",
            "type": "Video Meeting",
            "price": "₹ 500 +",
            "slashed_price": None,
            "desc": """
                In client interactions, I provide targeted technical insights and 
                career guidance. Drawing on my expertise, I deliver clear 
                explanations on emerging technologies and industry trends. 
                Whether discussing software development or IT infrastructure,
                 I aim to empower clients with informed decision-making. 
                 Additionally, I offer personalized career advice, assisting 
                 individuals in aligning their skills with evolving industry 
                 demands. Through these conversations, I strive to create a 
                 supportive environment where clients feel confident in both 
                 their technical choices and career trajectories.
            """
        },


        
        {
            "booking_name": "1:1 Mentorship",
            "index": "5",
            "tag": "1:1 Call",
            "time": "30 mins meeting",
            "duration": "30 mins",
            "type": "Video Meeting",
            "price": "₹ 600",
            "slashed_price": "Mentorship for better future and discipline",
            "desc": """
                In client interactions, I provide targeted technical insights and 
                career guidance. Drawing on my expertise, I deliver clear 
                explanations on emerging technologies and industry trends. 
                Whether discussing software development or IT infrastructure,
                 I aim to empower clients with informed decision-making. 
                 Additionally, I offer personalized career advice, assisting 
                 individuals in aligning their skills with evolving industry 
                 demands. Through these conversations, I strive to create a 
                 supportive environment where clients feel confident in both 
                 their technical choices and career trajectories.
            """
        },


        
        {
            "booking_name": "Resume review",
            "index": "6",
            "tag": "1:1 Call",
            "time": "45 mins meeting",
            "duration": "45 mins",
            "type": "Video Meeting",
            "price": "₹ 500",
            "slashed_price": "Unsure about your resume credibility? Allow me to help you",
            "desc": """
                In client interactions, I provide targeted technical insights and 
                career guidance. Drawing on my expertise, I deliver clear 
                explanations on emerging technologies and industry trends. 
                Whether discussing software development or IT infrastructure,
                 I aim to empower clients with informed decision-making. 
                 Additionally, I offer personalized career advice, assisting 
                 individuals in aligning their skills with evolving industry 
                 demands. Through these conversations, I strive to create a 
                 supportive environment where clients feel confident in both 
                 their technical choices and career trajectories.
            """
        },
        
    ]





def show_all_booking_types(id=-1):
    global ALL_BOOKINGS
    id = int(id)

    if 0 <= id < len(ALL_BOOKINGS):
        return ALL_BOOKINGS[:id] + ALL_BOOKINGS[id+1:]
    else:
        return ALL_BOOKINGS
    



def target_booking(id:int=0):
    global ALL_BOOKINGS
    return ALL_BOOKINGS[id]

#===============================================================================
#===============================================================================



def get_booking_types():
    return [
        {
            "booking_name": "Quick Chat",
            "tag": "1:1 Call",
            "index": 1,
            "time": "30 min meeting",
            "price": "₹ 500 +",
            "slashed_price": None
        },


        
        {
            "booking_name": "Mock Interview",
            "tag": "1:1 Call",
            "index": 2,
            "time": "60 min meeting",
            "price": "₹ 1,100 +",
            "slashed_price": "I can help create a few mock question papers for tech stuffs if needed"
        },


        
        {
            "booking_name": "Interview prep & tips",
            "tag": "1:1 Call",
            "index": 3,
            "time": "45 min meeting",
            "price": "₹ 650 +",
            "slashed_price": "I can take a demo interview for you for better confident"
        },


        
        {
            "booking_name": "Career guidance",
            "tag": "1:1 Call",
            "index": 4,
            "time": "30 min meeting",
            "price": "₹ 500 +",
            "slashed_price": None
        },


        
        {
            "booking_name": "1:1 Mentorship",
            "tag": "1:1 Call",
            "index": 5,
            "time": "30 min meeting",
            "price": "₹ 600",
            "slashed_price": "Mentorship for better future and discipline"
        },


        
        {
            "booking_name": "Resume review",
            "tag": "1:1 Call",
            "index": 6,
            "time": "45 min meeting",
            "price": "₹ 500",
            "slashed_price": "Unsure about your resume credibility? Allow me to help you"
        },


        
    ]






