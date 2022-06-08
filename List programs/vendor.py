## The vendor serves the following menu – Veg Roll, Noodles, Fried Rice and Soup and also maintains the quantity available for each item.
## The customer can order any combination of items. The customer is provided the item if the requested quantity of item is available with the vendor.
##
## Write a python program which implements the following functions:
##    
## 1. place_order(*item_tuple): This function accepts the order placed by the customer.The function should check whether the items requested
##      are present in the vendor’s menu and if so, it should check whether the requested quantity is available
##      for each by invoking the check_quantity_available() method.
##
##      The function should display appropriate messages for each item in the order for the below scenarios:
##      1.    When the requested item is not available in vendor’s menu, display <Item Name> is not available
##      2.    When the quantity requested by the customer is not available, display <Item Name> stock is over
##      3.    When the requested quantity of the item is available with the vendor, display <Item Name> is available
##
## 2. check_quantity_available(index,quantity_requested): This function should check whether the requested quantity of the specified item is available.
##      If so, it should reduce the quantity requested from the quantity available for that item and return True. Otherwise, it should return False.
##
##
##
##             Sample Input	                                        Expected Output
##    Menu and quantity available	         Items Ordered	
##
##    (Veg Roll, Noodles, Fried Rice , Soup)
##        [2,200,250,3]	                          Veg Roll,2            Veg Roll is available
##                                                Noodles,2             Noodles is available	        
        



def place_order(*item_tuple):

    for i in range(len(item_tuple)):

        if type(item_tuple[i]) == int:
            continue
        else:
            if item_tuple[i] in menu:
                check_quantity_available(item_tuple[i],item_tuple[i+1])
                
            else:
                print(item_tuple[i],"is not available")
       
                

def check_quantity_available(index,quantity_requested):
    quantity_available= menu.get(index)

    if quantity_available >= quantity_requested:
        print(index,"is available")

    else:
        print(index,"stock is over")



menu= {"Veg Roll" : 2, "Noodles" : 200, "Fried Rice" : 250 , "Soup" : 3}

order= input("Enter your order:")
quantity= int(input("Enter the quantity:"))

list= []
list.append(order)
list.append(quantity)

item_tuple= tuple(list)

print(item_tuple)

place_order(*item_tuple)
