n = int(input("Enter a number: "))

fact = 1
i = 1

for i in range(1,n+1):
   fact = fact*i

print("Factorial of " ,n,  " = " ,fact)
