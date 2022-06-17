# Bubble Sort



##list = [12,2,5,40,1,25]
##size = len(list) 
##
##
##for i in range(0,size):
##
##    for j in range(i,size):
##
##        if list[i]> list[j]:
##            temp = list[j]
##            list[j] = list[i]
##            list[i] = temp
##
##
##for i in list:
##    print(i, end=" ") 
            

n = int(input())
arr = list(map(int, input().split()))

for i in range(0,n):
    for j in range(i,n):
        if arr[i] > arr[j]:
           temp = arr[j] 
           arr[j] = arr[i]
           arr[i] = temp

for i in arr:
    print(i, end= " ")
        
