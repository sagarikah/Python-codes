##    You are given a function.
##    int CheckPassword(char str[], int n);
##    The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
##    str is a valid password if it satisfies the below conditions.
##
##    – At least 4 characters
##    – At least one numeric digit
##    – At Least one Capital Letter
##    – Must not have space or slash (/)
##    – Starting character must not be a number
##
##    Assumption:
##    Input string will not be empty.
##
##    Example:
##
##    Input:
##    aA1_67
##
##    Output:
##    1




def CheckPassword(str, n):
    if n < 4:
        return 0
    
    else:
        if str[0].isdigit():
            return 0
        
        else:
            count_numeric = 0
            count_capital = 0
            
            for i in range(0,n):
                if str[i].isupper():
                    count_capital += 1
                    
                if str[i].isdigit():
                    count_numeric += 1
                    
                if str[i] == ' ' or str[i] == '/':
                    return 0

            if count_capital >= 1:
                return 1
            else:
                return 0

            if count_numeric >= 1:
                return 1
            else:
                return 0


str = input()

res = CheckPassword(str, len(str))

print(res)
