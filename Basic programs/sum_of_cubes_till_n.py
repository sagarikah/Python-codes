##    Print the sum of series 1^3 + 2^3 + 3^3 + 4^3 + …….+ n^3 till n-th term.
##
##    Examples:
##    Input : n = 5
##    Output : 225
##    1^3 + 2^3 + 3^3 + 4^3 + 5^3 = 225



import math

n = int(input("Enter a number: "))

sum = 0

for i in range(1,n+1):
    cube = int(math.pow(i,3))
    sum += cube

print("Sum of cubes= ", sum)
