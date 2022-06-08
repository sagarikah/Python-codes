## Assume that the marks of 10 students are available in a tuple. The marks are out of 25.
##
## Write a python program to implement the following functions:
##    
## 1.  find_more_than_average(): Find and return the percentage of students who have scored more than the average mark of the class.
##
## 2.  generate_frequency(): Find how many students have scored the same marks. For example, how many have scored 0, how many have scored 1,
##            how many have scored 3….how many have scored 25. The result should be populated in a list and returned.
##            
## 3.  sort_marks(): Sort the marks in the increasing order from 0 to 25. The sorted values should be populated in a list and returned
##
##
##        Sample Input	                       Expected Output
##    list_of_marks = (12,18,25,24,2,
##                     5,18,20,20,21)	          70.0
##                                            [0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 1, 1]
##
##                                            [2, 5, 12, 18, 18, 20, 20, 21, 24, 25]




def find_more_than_average(list_of_marks):
    sum=0
    for i in range(10):
        sum= sum+list_of_marks[i]
    avg_marks= sum//10

    num_students=0
    for i in range(10):
        if list_of_marks[i] > avg_marks:
            num_students= num_students+1

    perc_students= float(num_students * 10)
    return perc_students

            

def generate_frequency(list_of_marks):
    list= []

    for i in range(26):        
        freq= list_of_marks.count(i)
        list.append(freq)

    return list
            
            

def sort_marks(list_of_marks):
    return sorted(list(list_of_marks))



list_of_marks = (12,18,25,24,2,5,18,20,20,21)     # tuple

print(find_more_than_average(list_of_marks))

print(generate_frequency(list_of_marks))

print(sort_marks(list_of_marks))
