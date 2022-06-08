##    Write a python function find_duplicates(), which accepts a list of numbers and returns another list
##    containing all the duplicate values in the input list. If there are no duplicate values, it should return an empty list.



def find_duplicates(list):
    duplicate_list= []

    for i in range(5):
        if list[i] in duplicate_list:
            continue
        else:
            if list.count(list[i]) >1:
                duplicate_list.append(list[i])
             
                 
    return duplicate_list



list= []

for i in range(5):
    num= input("Enter a number: ")
    list.append(num)


print(find_duplicates(list))
