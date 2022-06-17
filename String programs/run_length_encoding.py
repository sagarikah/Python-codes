##    Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding.
##    Write a python function which performs the run length encoding for a given String
##    and returns the run length encoded String.
##
##	  Sample Input	     Expected Output
##	  AAAABBBBCCCCCCCC     4A4B8C
##	  AABCCA	       2A1B2C1A



s= input("Enter a string: ")
encoded_form= []

for i in range(len(s)):
    if s[i] in encoded_form:
        continue
    else:
        count= s.count(s[i])
        encoded_form.append(count)
        encoded_form.append(s[i])
        count= 0

for i in range(len(encoded_form)):
    print(encoded_form[i], end='')


        
    
    
    
