# Minimum among 3 numbers

num1= int(input("Enter a number:"))
num2= int(input("Enter a number:"))
num3= int(input("Enter a number:"))

if num1<num2 and num1<num3:
    min= num1
    print("Minimum number is ",min)
elif num2<num1 and num2<num3:
    min= num2
    print("Minimum number is ",min)
else:
    min= num3
    print("Minimum number is ",min)

    
