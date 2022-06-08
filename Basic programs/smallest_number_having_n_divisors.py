##    Write a python function find_smallest_number() which accepts a number n and returns the smallest number having n divisors.
##
##        Sample Input	 Output
##              16	 120



def find_smallest_number(n):
    divisors= 0
    res= 1

    while divisors<= n:
        for i in range(1,res+1):
            if res%i == 0:
                divisors= divisors+1
        res= res+1

    print(res)
        



find_smallest_number(16)

