# Swap first and last elements in a list

a= ["banana", "apple", "mango", "cherry"]
i=0
size= len(a)

for i in range(size):
  if i == 0:
      temp= a[i]
      a[i]= a[size-1]
      a[size-1]= temp
  print(a[i])
