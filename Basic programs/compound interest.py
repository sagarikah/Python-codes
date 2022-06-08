# A = P(1+ 0.01*R)**T
# CI = A-P




import math

p = int(input("Enter principle: "))
r = int(input("Enter rate: "))
t = int(input("Enter time: "))

amt = p* math.pow((1 + r/100),t)
ci = amt-p

print("Compound Interest = " + str(ci))
        
