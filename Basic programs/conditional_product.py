# Write a python program to find and display the product of three positive integer values based on the rule mentioned below:

# It should display the product of the three values except when one of the integer value is 7.
# In that case, 7 should not be included in the product and the values to its left also should not be included.
# If there is only one value to be considered, display that value itself.
# If no values can be included in the product, display -1.

#  Note: Assume that if 7 is one of the positive integer values,
#   then it will occur only once. Refer the sample I/O given below:
#
#          Sample Input	    Expected Output
#                1, 5, 3  	15
#                3, 7, 8	8
#                7, 4, 3	12
#                1, 5, 7	-1



num1= int(input("Enter a number: "))
num2= int(input("Enter a number: "))
num3= int(input("Enter a number: "))

if num1 != 7 and num2 != 7 and num3!=7:
    product= num1*num2*num3

elif num1== 7:
    product= num2*num3

elif num2== 7:
    product= num3

else:
    product= -1

print("Product= ",product)
