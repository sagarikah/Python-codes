# Sum of elements in a list

list= []
size= int(input("Enter the size of list: "))

for i in range(size):
    n= int(input("Enter a number: "))
    list.append(n)

sum=0

for i in range(size):
    sum= sum+list[i]

print("sum= ", sum)
