
time1 = '12:00'
time2 = '14:00'

time_list = []
is_prime = False

time1_min = time1[3:5]
time1_hr = time1[0:2]

time2_min = time2[3:5]
time2_hr = time2[0:2]

temp_time1 = 0
temp_time2 = 0

# temp_time1 = time1 
# temp_time2 = time2


if int(time1_hr) >12 :
    is_prime = True
    time1_hr = int(time1_hr) - 12
    time2_hr = int(time2_hr) - 12

    if int(time1_hr) < 10:
        time1_hr = '0' + str(time1_hr)
    
    if int(time2_hr) < 10:
        time2_hr = '0' + str(time2_hr)

# print(time1_hr, time2_hr)

temp_time1 = time1_hr + ':' + time1_min
temp_time2 = time2_hr  + ':' + time2_min


time_list.append(temp_time1)
i = 1
while temp_time1 != temp_time2 :
    if(int(time1_min) + 10 >= 60) :
        # if int(time1_hr) + 1 > 12 :
        #     s = i+1
        #     time1_hr = '0' + str(s) 
        if len(str(int(time1_hr) + 1 )) == 2 :
            time1_hr =  str(int(time1_hr) + 1)
            time1_min = '00'
        else:
            time1_hr = '0' +str(int(time1_hr) + 1)
            time1_min = '00'

    else:
        time1_min = int(time1_min)+10 

    # if int(time1_hr) < 12 :
    #     new_time = str(time1_hr)  + ":" + str(time1_min) + 'AM'

    # else:
    new_time = str(time1_hr)  + ":" + str(time1_min)

    temp_time1 = new_time
    time_list.append(temp_time1)


# result = list(map(lambda x:  x +' AM', time_list))
print(time_list)

# new_list1 = []

 
# for i in time_list :
#     hr = i[0:2]
#     print(hr)
#     if(int(hr) == 12) :

    
#         d = i +'Pm'
#         new_list1.append(d)
     
#     else:
#         d = i +'Am'
#         new_list1.append(d)


# print(new_list1)