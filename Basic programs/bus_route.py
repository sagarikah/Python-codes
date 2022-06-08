##    The bus runs on multiple routes having different distance in kms and number of passengers.
##    Write a function to calculate and return the profit earned (Rs) in each route. Return -1 in case of loss.
##
##    Assume that the following information are given:
##    Price per litre of fuel = 70
##    Mileage of the bus in km/litre of fuel = 10
##    Price(Rs) per ticket = 80




def profit_func(distance,num_passengers):
   earn= ticket_price * num_passengers
   spend= (distance//mileage)*fuel_price
   
   if earn>spend:
      profit= earn-spend
      return(profit)
   else:
      return(-1)



fuel_price= 70
mileage= 10
ticket_price= 80

distance= int(input("Enter the distance in kms: "))
num_passengers= int(input("Enter the number of passengers: "))

profit= profit_func(distance,num_passengers)

if profit> -1:
    print(" Profit of Rs",profit)
else:
    print("Loss")
