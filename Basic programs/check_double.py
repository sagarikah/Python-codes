##    Write a python function, check_double(number) which accepts a whole number and returns True if it satisfies the given conditions.
##    Otherwise it should return False.
##
##        1.The number and its double should have exactly the same number of digits.
##        2.Both the numbers should have the same digits ,but in different order.   
##
##    Example: If the number is 125874 and its double, 251748, contain exactly the same digits, but in a different order.



def check_double(number):
    double= 2*number

    num_digits_number= 0
    num_digits_double= 0
    copy_number= number
    copy_double= double

    while number>0:
        dig= number % 10
        num_digits_number += 1
        number= number//10

    while double>0:
        dig= double % 10
        num_digits_double += 1
        double= double//10

    if num_digits_number == num_digits_double:
        s_number= str(copy_number)
        s_double= str(copy_double)

        for i in range(len(s_number)):
            if s_number[i] in s_double:
                if i == len(s_number)-1:
                    return True
                else:
                    continue
                
            else:
                return False

    else:
        return False
   

print(check_double(125874))
