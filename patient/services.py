from datetime import datetime, timedelta
import time
from hms_admin.models import Consultation
from .models import Booking
from django.db.models import Q


def get_slots(time1, time2):

    time1 = datetime.strptime(time1, '%H:%M')
    time2 = datetime.strptime(time2, '%H:%M')
    continue_iter = True
    slots = []
    t = time1
    format1 = '%I:%M %p'
    slots.append(t.time().strftime(format1))
    while continue_iter:
        t1 = t + timedelta(minutes=10)
        
        temp1 = t1.time().strftime(format1)
        temp2 = time2.time().strftime(format1)
        print(temp1)
        slots.append(temp1)

        if temp1 == temp2:
            continue_iter = False

        t = t1

    print(slots)
    return slots


# print(get_slots('10:00','11:00'))


def create_slots(query_set):
    
     
    session_count=1
    available_session = {}
    slot_arr = []
    available_slots = []
    for i in query_set :
        available_session ={}
        key = 'session'+ str(session_count)
        session_time  = i.time.split(' - ')
        slot = get_slots(session_time[0],session_time[1])

        # print('slot iss', slot) 

        available_session[key] = slot

        available_slots.append(available_session)
        # print('sample is ',sample)
        session_count +=1

    # print('session isssss',available_session)
    slot_arr.append(available_session)
     
    return  available_slots
   

def create_bookings(query_set):
    booking_arr = []
    booking_dict ={}

    for i in query_set:
        print(i.time,'heree')


def generate_slot(doctor,date, day):
    
    sessions = []
    
    time_obj ={}

    book_time = []

    consultaion_records = Consultation.objects.filter(doctor = doctor, day = day).values('time')
    booking_records = Booking.objects.filter(~Q(status = 'cancelled'),doctor = doctor, booking_date = date).values('time')
      
    for record in booking_records:
        book_time.append(record['time'])
    
     
    
        
    for records in consultaion_records:

        time = records['time'].split(' - ')
        slots = get_slots(time[0], time[1])

        for i in slots : 
            
            if book_time.count(i) > 0:
                time_obj[i] = 'booked'

            else:
                time_obj[i] = 'not booked'

    sessions.append(time_obj)
    print(sessions)
    return sessions