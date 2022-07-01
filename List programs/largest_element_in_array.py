##    Given an array, find the largest element in it.
##
##    Input : 10,20,4
##    Output : 20
##
##    Input : 20,10 ,20 ,4,100
##    Output : 100






arr = list(map(int, input().split(',')))

size = len(arr)
max = arr[0]

for i in range(0,size):
    if arr[i] > max:
        max = arr[i]

print(max)
