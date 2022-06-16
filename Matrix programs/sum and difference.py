##    Print the sum (A+B) and difference (A-B) of 2 matrices A,B

##    Input:
##        Enter number of rows in matrix : 3
##        Enter number of columns in matrix : 3
##        Enter the elements of matrix A: 
##        1 2 3 4 5 6 7 8 9    
##        Enter the elements of matrix B: 
##        1 2 3 4 5 6 7 8 9        
##
##    Output:
##        Sum = [[2, 4, 6],[8, 10, 12],[14, 16, 18]]
##        Difference = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]




import numpy as np

rows = int(input("Enter number of rows in matrix : "))
columns = int(input("Enter number of columns in matrix : "))

print("Enter the elements of matrix A: ")
A = list(map(int, input().split()))

print("Enter the elements of matrix B: ")
B = list(map(int, input().split()))

arr_A = np.array(A).reshape(rows,columns)
arr_B = np.array(B).reshape(rows,columns)

add = arr_A + arr_B
sub = arr_A - arr_B

print("Sum = ", add)
print("Difference = ", sub)



    
