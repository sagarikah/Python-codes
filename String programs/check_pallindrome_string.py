##    Write a function, check_palindrome() to check whether the given string is a palindrome or not.
##    The function should return true if it is a palindrome else it should return false.





def check_pallindrome(st):
   size= len(st)
  
   for i in range(size//2):
      if st[i] == st[(size-1)-i]:
         continue
      else:
         return False
   
   return True   
       


st= input("Enter a string: ")

print(check_pallindrome(st))
