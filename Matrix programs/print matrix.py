##    Input:
##
##    Enter number of rows = 
##    2
##    Enter number of columns = 
##    3
##    Enter elements = 
##    1 2 3 4 5 6
##
##
##    Output:
##        
##    [[1 2 3]
##     [4 5 6]]






import numpy as np

print("Enter number of rows = ")
rows = int(input())
print("Enter number of columns = ")
columns = int(input())

print("Enter elements = ")
l = list(map(int, input().split()))

arr = np.array(l)
new_arr = arr.reshape(rows,columns)

print(new_arr)
