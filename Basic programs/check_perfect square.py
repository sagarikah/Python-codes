# WAP to check if a number is a perfect square
# perfect squares = 1,4,9,16,....



import math

n = int(input("Enter a number: "))

sqrt = math.isqrt(n)

if (sqrt**2 == n):
    print("perfect square")
else:
    print("not perfect square")
        
