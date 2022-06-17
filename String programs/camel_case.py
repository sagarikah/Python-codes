##There is a sequence of words in CamelCase as a string of letters, s, having the following properties:
##
##It is a concatenation of one or more words consisting of English letters.
##All letters in the first word are lowercase.
##For each of the subsequent words, the first letter is uppercase and rest of the letters are lowercase.
##Given s, determine the number of words in s.
##
##Returns:
##int: the number of words in s
##
##Input Format:
##A single line containing string s.
##
##Sample Input:
##saveChangesInTheEditor
##
##Sample Output:
##5





def camelcase(s):
    n = 1

    for i in range(0,len(s)):
        if s[i].isupper() == True:
            n+= 1

    return n


s = input()
num_words = camelcase(s)

print(num_words)

