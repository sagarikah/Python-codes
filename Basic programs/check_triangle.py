##    Write a python function to check whether three given numbers can form the sides of a triangle.
##
##    Hint: Three numbers can be the sides of a triangle if none of the numbers are greater than
##      or equal to the sum of the other two numbers.


num1= int(input("Enter a number: "))
num2= int(input("Enter a number: "))
num3= int(input("Enter a number: "))

if num1+num2 > num3 and num2+num3 > num1 and num1+num3 > num2:
    print("Triangle is possible")
else:
    print("Triangle is not possible")


