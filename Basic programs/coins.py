#    You have x no. of 5 rupee coins and y no. of 1 rupee coins.
#    You want to purchase an item for amount z. The shopkeeper wants you to provide exact change.
##    You want to pay using minimum number of coins. How many 5 rupee coins and 1 rupee coins
##    will you use?
##    If exact change is not possible then display -1.
##
##                             Sample Input	                                               Expected Output
##    Available Rs. 1 coins	Available Rs. 5 notes	Amount to be made	Rs. 1 coins needed	Rs. 5 notes needed
##              2 	               4	              21	              1	                4
##              11	               2	              11	               1	        2
##              3	               3	              19	             -1



num_one_coins= int(input("Enter number of available Rs 1 coin: "))
num_five_coins= int(input("Enter number of available Rs 5 coin: "))
amt= int(input("Enter amount to be made: "))

amt_available= (5*num_five_coins) + num_one_coins

if amt>amt_available:
    print("-1")

else:
    five_coins_needed= amt//5
    one_coins_needed= amt - (5*five_coins_needed)

    print("Number of Rs 1 coin needed= ",one_coins_needed)
    print("Number of Rs 5 coin needed= ",five_coins_needed)
