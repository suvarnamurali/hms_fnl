from datetime import datetime,timedelta
import time

def get_slots(time1,time2):

    time1 = datetime.strptime(time1, '%H:%M')
    time2 = datetime.strptime(time2, '%H:%M')
    continue_iter = True
    slots = []
    t = time1

    while continue_iter :
        t1 = t + timedelta(minutes=10)
        format1 = '%I:%M %p'
        temp1 = t1.time().strftime(format1)
        temp2 = time2.time().strftime(format1)
        slots.append(temp1)

        if temp1 == temp2:
            continue_iter = False

        t = t1
        return slots

slot = get_slots ('12:00','20:00')

 
