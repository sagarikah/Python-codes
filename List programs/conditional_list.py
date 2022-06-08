##    Write a python program which finds the maximum number from num1 to num2 (num2 inclusive) based on the following rules.
##
##    1.  Always num1 should be less than num2
##    2.  Consider each number from num1 to num2 (num2 inclusive). Populate the number into a list, if the below conditions are satisfied
##        1.  Sum of the digits of the number is a multiple of 3
##        2.  Number has only two digits
##        3.  Number is a multiple of 5
##    3.  Display the maximum element from the list
##
##    In case of any invalid data or if the list is empty, display -1.


num1= int(input("Enter the starting number: "))
num2= int(input("Enter the ending number: "))

list= []

if num1<num2:
    for i in range(num1,num2+1):
        if i%5 == 0:
            list.append(i)
            
        else:
            count=0
            temp= i
            while i>0:
               dig= i%10
               count= count+1
               i= i//10
            if count == 2:
                list.append(temp)

            else:
                sum=0
                temp1= temp
                while temp>0:
                    dig= temp%10
                    sum= sum+dig
                    temp= temp//10
                if sum%3 == 0:
                    list.append(temp1)

    for j in range(len(list)):
        print(list[j])

    list.sort()
    print("Maximum element= ",list[-1])

if len(list)==0 or num1>num2:
    print("-1")
    
            
       
