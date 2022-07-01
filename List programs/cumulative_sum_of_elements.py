##    The problem statement asks to produce a new list whose i^{th} element will be equal to the sum of the (i + 1) elements.
##
##    Examples : 
##
##    Input : list = [10, 20, 30, 40, 50]
##    Output : [10, 30, 60, 100, 150]
##
##    Input : list = [4, 10, 15, 18, 20]
##    Output : [4, 14, 29, 47, 67]




print("Enter list: ")
A = list(map(int, input().split()))

new_A = []

cum_sum = 0

for i in range(0,len(A)):
    cum_sum += A[i]
    new_A.append(cum_sum)

print("Result= ", new_A)
