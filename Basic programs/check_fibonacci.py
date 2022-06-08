##    Given a number ‘n’, WAP to check if n is a Fibonacci number. First few Fibonacci numbers are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .. 
##
##    Examples : 
##    Input : 8
##    Output : Yes
##
##    A simple way is to generate Fibonacci numbers until the generated number is greater than or equal to ‘n’.
##    Following is an interesting property about Fibonacci numbers that can also be used to check if a given number is Fibonacci or not: 
##    A number is Fibonacci if and only if one or both of (5*(n^2) + 4) or (5*(n^2) – 4) is a perfect square 





import math

n = int(input("Enter a number: "))

if (n == 0):
    print("fibonacci number")

else:
    def isPerfectSquare(x):
        s = int(math.sqrt(x))
        return s*s == x
     
    def isFibonacci(n):
        return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
        
    if (isFibonacci(n) == True):
        print (n," is a Fibonacci Number")
    else:
        print (n," is not Fibonacci Number ")
