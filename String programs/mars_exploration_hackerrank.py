##    HACKER RANK PROBLEM:

##    A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
##    Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, s,
##    determine how many letters of the SOS message have been changed by radiation.
##
##    Returns:
##    int: the number of letters changed during transmission
##
##    Input Format:
##    There is one line of input: a single string, s.
##
##
##    Sample Input 0 - 
##    SOSSPSSQSSOR
##
##    Sample Output 0 -
##    3
##
##    Explanation 0 -
##    Expected signal: SOSSOSSOSSOS
##    Recieved signal: SOSSPSSQSSOR
##    Difference:          X  X   X
##
##
##    Sample Input 1 -
##    SOSSOT
##
##    Sample Output 1 -
##    1
##
##    Explanation 1 -
##    Expected Signal: SOSSOS     
##    Received Signal: SOSSOT
##    Difference:           X



def marsExploration(s):
    mes = []
    count_error = 0

    for i in range(0, len(s), 3):
       part = s[i:i+3]
       mes.append(part)

    for i in range(0,len(mes)):
       if mes[i][0] == "S" and mes[i][1] == "O" and mes[i][2] == "S":
          continue
        
       else:
          if mes[i][0] != "S":
             count_error += 1
             
          if mes[i][1] != "O":
             count_error += 1
             
          if mes[i][2] != "S":
             count_error += 1 
       
    return count_error


s = input()
res = marsExploration(s)
print(res)
