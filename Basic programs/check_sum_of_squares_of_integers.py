# Given an integer n, write a python function to return true, if it is possible to
# represent it as a sum of the squares of two different integers, else return false.



def check_squares(number):
    flag= 0
    
    for n1 in range(1,number//2):
        sq_n1= n1*n1
        sq_n2= number - sq_n1
        n2= 1
        
        while(n2 < sq_n2):
            if n2*n2== sq_n2 and n2 != n1:
               flag= 1
               break
               
            else:
                n2+= 1

    if flag== 1:
        return True
    else:
         return False
    

number=100
print(check_squares(number))
