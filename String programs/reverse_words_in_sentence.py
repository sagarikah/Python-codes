##    We are given a string and we need to reverse words of a given string
##
##    Examples:
##
##    Input : str = ”geeks quiz practice code”
##
##    Output : str = code practice quiz geeks  
##
##    Input : str = “my name is laxmi”
##
##    output : str= laxmi is name my 



inp = str(input("Enter a sentence: "))

list_str = inp.split()

list_str.reverse()
    
print(' '.join(list_str))
