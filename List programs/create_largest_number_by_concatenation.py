##    Write a python function, create_largest_number(), which accepts a list of numbers and
##    returns the largest number possible by concatenating the list of numbers.
##
##    Note: Assume that all the numbers are two digit numbers.
##
##          Sample Input	Expected Output
##           23,34,55	        553423




def create_largest_number(list):

    list.sort(reverse=True)
    largest_num= ' '

    for i in list:
       largest_num= largest_num + str(i)

    return int(largest_num)
        



list= [23,34,55]
print(create_largest_number(list))

