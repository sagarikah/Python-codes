#   Find the first repetting element in a list
#    input :  [3,5,3,1,1,4]     output: 3




##def first_repetting_element(list, item, i):
##    flag =0
##    for j in range(len(list)):
##        if j == i:
##            continue
##        else:
##            if list[j] == item:
##                flag = 1
##                break
##    if flag == 1:
##        print(item)
##    return True
            
        
    

list = []

for i in range (5):
    item = int(input("Enter a number: "))
    list.append(item)


for i in range(len(list)):
    item = list[i]
    for j in range(len(list)):
        if j == i:
            continue
        else:
            if list[j] == item:
                flag = 1
                break

if flag == 1:
        print(item)


