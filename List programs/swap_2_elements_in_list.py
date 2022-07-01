##    Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
##
##    Examples: 
##     
##    Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
##    Output : [19, 65, 23, 90]
##
##    Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
##    Output : [1, 5, 3, 4, 2]





print("Enter the list: ")
li = list(map(int, input().split()))

pos1 = int(input("Enter the position: "))
pos2 = int(input("Enter the position: "))


temp = li[pos1-1]
li[pos1-1] = li[pos2-1]
li[pos2-1] = temp


print(li)
        
