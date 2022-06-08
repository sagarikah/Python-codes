# Code to find the sum of numbers divisible by 4.
# The code must allow the user to input a number and add it to the sum if it is divisible by 4.
# It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.


size= int(input("Enter how many numbers you want to input: "))
sum=0

for i in range(size):
    num= int(input("Enter a number: "))
    if num%4 == 0:
        sum= sum+num
    else:
        continue

print("Sum of numbers which are divisible by 4= ",sum)
         
