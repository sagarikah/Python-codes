##    Given two positive integers start and end. The task is to write a Python program
##    to print all Prime numbers in that Interval.




start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

factor_count = 0

print("Prime numbers = ")

for i in range(start, end+1):
    num = i
    
    for j in range(2,num):
        if (num % j == 0):
            factor_count += 1

    if (factor_count == 0):
        print(num)

    factor_count = 0
