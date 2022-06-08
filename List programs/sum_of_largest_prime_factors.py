##    Given a number n, write a program to find the sum of the largest prime factors of each of nine consecutive numbers starting from n.
##    g(n) = f(n) + f(n+1) + f(n+2) + f(n+3) + f(n+4) + f(n+5) + f(n+6) + f(n+7) + f(n+8)
##    where, g(n) is the sum and f(n) is the largest prime factor of n
##
##    For example,
##    g(10)=f(10)+f(11)+f(12)+f(13)+f(14)+f(15)+f(16)+f(17)+f(18)
##            =5 + 11 + 3 + 13 + 7 + 5 + 2 + 17 + 3
##            =66



def largest_prime_factor(n):
    
    factors= 0
    list_factors= []
    
    for i in range(1,n+1):
        if n%i == 0:
            for j in range(2,i):
                if i%j == 0:
                    factors= factors+1
                    
            if factors == 0:
                list_factors.append(i)

    if len(list_factors) == 1:
        return list_factors[0]

    else:
        max= list_factors[0]

        for k in range(len(list_factors)):
            if list_factors[k] > max:
                max= list_factors[k]        

        return max

              
    
sum= 0

n= int(input("Enter a number: "))

for i in range(9):
    res= largest_prime_factor(n+i)
    sum= sum+res

print(sum)

    
