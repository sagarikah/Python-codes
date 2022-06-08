##Given a number x, determine whether the given number is Armstrong number or not. A positive integer of n digits
##is called an Armstrong number of order n (order is number of digits) if
##
##abcd... = pow(a,n) + pow(b,n) + pow(c,n) + pow(d,n) + .... 
##
##Example:
##Input : 153
##Output : Yes
##
##153 is an Armstrong number
##1*1*1 + 5*5*5 + 3*3*3 = 153




import math

num = int(input("Enter a number : "))
order = len(str(num))

copy = num
sum = 0

while(num > 0):
    dig = num % 10
    dig_pow = math.pow(dig,order)
    sum = sum + dig_pow
    num = num //10

if (sum == copy):
    print("yes")
else:
    print("no")

    
