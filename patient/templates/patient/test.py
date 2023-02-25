import time


data = '06:00 - 07:00'

time_arr = data.split(' - ')

def getList(time1,time2):

    time_list = []
    # print(time1[3:5])
    is_24hr = False

    # time_list.append(time1)
    temp1 = time1
    temp2 = time2
    min = time1[3:5]
    hr = time1[0:2]
    
    if(int(hr) > 12):  # 18:00 - 19 :00
        hr1 = int(hr) - 12  # hr1 = 6
        is_24hr = True
        if int(hr1) < 10 :
            # print('yess')
            temp1 = '0'+str(hr1) + ':' + str(min) # temp1 = 06:00
            hr ='0'+ str(hr1)
        if(int(time2[0:2]) > 12):  # 18:00 - 19 :00
            hr2 = int(time2[0:2]) - 12  # hr1 = 6

            if int(hr2) < 10 :
                
                temp2 = '0'+str(hr2) + ':' + str(time2[3:5])
                # temp2 = '0'+str((int(time2[0:2]) - 12)) + ':' + str(time2[3:5])
      
    
    print(temp1)
    print(temp2)       
    while temp1 != temp2 :
        
        
        new_time = 0
        print('min value is',min)
        if((int(min) + 10) >=60):
            # if not is_24hr :
            hr = '0' +str(int(hr) + 1)
            # else:
                # hr = str(int(hr) + 1)

            min = '00'
        
        else:
            print('000', type(min))
            if int(min) > 50:
                hr = '0' +str(int(hr) + 1)
                min = '00'
                print('here')
                # hr = '0' +str(int(hr) + 1)
            print('else working')
            # min = int(min)+10
        
        min = int(min)+10 
        
        new_time = str(hr)+ ":" + str(min)
        time_list.append(temp1)
        print('appending')
        print(time_list)
        temp1 = new_time

        # print(temp1)
        # print(temp2)


    # if((int(min) + 10) >=60):
    #     hr = int(hr) + 1
    #     min = '00'
    
    # else:
    #     min = int(min)+10
    
    # new_time = str(hr)+ ":" + str(min)
    
    
    # temp1 = new_time

    # print(temp1)
    # print(temp2)
   
    # print('**********')
    # time_list.append(new_time) 
    # print(time_list)
    # print('**********')
    # time_list.pop()
    

 

getList(time_arr[0],time_arr[1])

 

 