##    WAP to print Fibonacci series upto 'n' number of terms
##
##    The sequence Fn of Fibonacci numbers is defined by the recurrence relation 
##    Fn = Fn-1 + Fn-2
##
##    With seed values 
##    F0 = 0 and F1 = 1.
##
##    First few Fibonacci numbers are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, .. 



n = int(input("Enter the number of terms: "))

series = []
i = len(series)

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1)+fibonacci(i-2)
        
while(i < n):
    x = fibonacci(i)
    series.append(x)
    i += 1

print("Fibonacci series: ", series)
