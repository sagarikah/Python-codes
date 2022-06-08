##     Write a Python program to generate the next 15 leap years starting from a given year.
##     Populate the leap years into a list and display the list.


year= int(input("Enter a year: "))

list=[]
count=0

while count< 15:
    if year%4 == 0:
        count= count+1
        list.append(year)
    year= year+1

print("Next 15 leap years: ", list)


