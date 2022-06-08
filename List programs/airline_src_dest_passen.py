##    Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
##    The ticket number should be generated as airline:src:dest:number
##    1.  Consider AI as the value for airline
##    2.  src and dest should be the first three characters of the source and destination cities.
##    3.  number should be auto-generated starting from 101
##
##    The program should return the list of ticket numbers of last five passengers.
##    Note: If passenger count is less than 5, return the list of all generated ticket numbers.
##
##        Sample Input	            Expected Output
##
##        airline = AI
##        source = Bangalore
##        destination = London
##        no_of_passengers = 10	   ['AI:Ban:Lon:106', 'AI:Ban:Lon:107', 'AI:Ban:Lon:108', 'AI:Ban:Lon:109', 'AI:Ban:Lon:110']
##
##        airline = BA
##        source = Australia
##        destination = France
##        no_of_passengers = 2	   ['BA:Aus:Fra:101', 'BA:Aus:Fra:102']



airline= input("Enter name of airline: ")
src= input("Enter source: ")
dest= input("Enter destination :")
num_passengers= int(input("Enter number of passengers: "))

src1= src[0:3]
dest1= dest[0:3]

list= []

tick_no= 101

for i in range(num_passengers):
    s= airline + ":" + src1 + ":" + dest1 + ":" + str(tick_no)
    list.append(s)
    tick_no= tick_no+1


if num_passengers < 5:
    print(list)

else:
    print(list[-5:])

