# Check if the given number is Pallindrome

num = int(input("Enter a number: "))
copy= num
rev= 0

while num>0:
    dig= num%10
    rev= (rev*10)+dig
    num= num//10

if rev == copy:
    print(copy," is Pallindrome")
else:
    print(copy," is not Pallindrome")
    

    







    
