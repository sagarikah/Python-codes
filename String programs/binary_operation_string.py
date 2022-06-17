##    Problem Description :
##
##    The Binary number system only uses two digits, 0 and 1 and number system can be called binary sting.
##    You are required to implement the following function:
##
##    int OperationsBinaryString(char* st);
##
##    The function accepts a sting st as its argument. The sting st consists of binary digits eparated with an alphabet as follows:
##
##    – A denotes AND operation
##    – B denotes OR operation
##    – C denotes XOR Operation
##    You are required to calculate the result of the sting st, scanning the sting to right taking one opearation at a time, and return the same.
##
##    Note:
##
##    No order of priorities of operations is required
##    Length of st is odd
##    If st is NULL or None (in case of Python), return -1
##
##
##    Input:
##    st: 1C0C1C1A0B1
##
##    Output:
##    1
##
##    Explanation:
##    The alphabets in st when expanded becomes “1 XOR 0 XOR 1 XOR 1 AND 0 OR 1”, result of the expression becomes 1, hence 1 is returned.




def OperationsBinaryString(st):
    dig_1 = int(st[0])
    exp = st[1]
    dig_2 = int(st[2])

    if exp == 'A':
        res = dig_1 & dig_2

    elif exp == 'B':
        res = dig_1 | dig_2

    else:
        res = dig_1 ^ dig_2

        
    if len(st) == 3:
        print(res)

    else:      
        new_st = str(res) + st[3:]
        OperationsBinaryString(new_st)


st = input()

OperationsBinaryString(st)

