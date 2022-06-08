##    Given two lists, both having String elements, write a python program using python lists to
##    create a new string as per the rule given below:
##
##    The first element in list1 should be merged with last element in list2,
##    second element in list1 should be merged with second last element in list2 and so on.
##    If an element in list1/list2 is None, then the corresponding element in the other list
##    should be kept as it is in the merged list.
##
##
##                    Sample Input                                   Expected Output
##                              
##    list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']     “An apple a day keeps the doctor away”
##    list2=['y','tor','e','eps','ay',None,'le','n']




def merge_list(list1, list2):
    merged_data = ""
    temp_list = []
    
    for i in range(len(list1)):
        st = list1.pop()
        temp_list.append(st)

    for i in range(len(temp_list)):
        s = temp_list.pop()
        s1 = list2.pop()
        
        if s != None and s1 != None:
             merged_data = merged_data + s + s1 + " "
             
        elif s == None:
            merged_data = merged_data + s1 + " "
            
        else:
            merged_data = merged_data + s + " "  
            
    
    return merged_data


list1 = ['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y','tor','e','eps','ay',None,'le','n']

merged_data = merge_list(list1,list2)
print(merged_data)
