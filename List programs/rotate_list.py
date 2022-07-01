# Write a Python function to rotate the list of elements by N positions to the right. The function should return the rotated list
# Assume that number of positions to be rotated is always a value >= 0 and <= length of the input list.




def rotate_list(input_list,n):
    output_list= []

    for item in range(len(input_list) - n, len(input_list)):
        output_list.append(input_list[item])
    
    for item in range(0, len(input_list) - n): 
        output_list.append(input_list[item])
        
    return output_list



input_list= [1,2,3,4,5,6]

output_list=rotate_list(input_list,4)
print(output_list)
