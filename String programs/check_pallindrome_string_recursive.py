##    Write a recursive function, is_palindrome() to find out whether a string is a palindrome or not.
##    The function should return true, if it is a palindrome. Else it should return false.





def is_pallindrome(s):
    if len(s) == 0 or len(s)==1:
        print("Pallindrome")
    else:
        if s[0] == s[-1]:
            is_pallindrome(s[1:-1])
        else:
            print("Not Pallindrome")


s= input("Enter a string: ")
is_pallindrome(s)

