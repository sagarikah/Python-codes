# second largest element in a list

list= []
size= int(input("Enter size of list: "))


for i in range(size):
    ele= int(input("Enter a number: "))
    list.append(ele)

list.sort()
print("Second largest element= ", list[-2])
