
time1 = '10:00'
time2 = '11:00'

time_list = []

time1_min = time1[3:5]
time1_hr = time1[0:2]

time2_min = time2[3:5]
time2_hr = time2[0:2]

temp_time1 = 0
temp_time2 = 0

temp_time1 = time1 
temp_time2 = time2

 
while temp_time1 != temp_time2 :
    if(int(time1_min) + 10 >=60) :
        if len(time1_hr) == 2 :
            time1_hr =  str(int(time1_hr) + 1)
            time1_min = '00'
        else:
            time1_hr = '0' +str(int(time1_hr) + 1)
            time1_min = '00'

    else:
        time1_min = int(time1_min)+10 

    new_time = str(time1_hr)  + ":" + str(time1_min)

    temp_time1 = new_time

    print(temp_time1)