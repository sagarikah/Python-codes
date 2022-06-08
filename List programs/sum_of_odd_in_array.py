# Sum of odd integers in array



def SumOddIntegers(arr, n):
     sum = 0

     for i in range(0,n):
         if arr[i] % 2 != 0:
             odd = arr[i]
             sum += odd

     print(sum)



n = int(input())

arr = list(map(int, input().split()))

SumOddIntegers(arr, n)
