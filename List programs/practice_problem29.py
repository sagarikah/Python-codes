def exchange_list(number_list):
    #start writing your code here
    new_list= []
    length= len(number_list)
    mid_pos= (length//2)-1
    
    i= length-1
    while(i>mid_pos):
        new_list.append(number_list[i])
        i -= 1

    for j in range(mid_pos+1):
        new_list.append(number_list[j])

    return new_list
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))


