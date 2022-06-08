
##    Write a Python program to calculate the bill amount to be paid by a customer based on the list of gems and quantity purchased.
##    Any purchase with a total bill amount above Rs.30000 is entitled to 5% discount.
##    If any gem required by the customer is not available in the store, then consider total bill amount to be -1.
##
##        gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
##        price_list=[1760,2119,1599,3920,3999]
##
##        List of gems required by the customer
##        reqd_gems=["Ivory","Emerald","Garnet"]
##        reqd_quantity=[3,10,12]




reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[3,10,12]

gems_dict= {"Emerald" : 1760, "Ivory" : 2119, "Jasper" : 1599, "Ruby" : 3920, "Garnet" : 3999 }

total_price=0

for i in range(len(reqd_gems)):
    if reqd_gems[i] in gems_dict:
        price= reqd_quantity[i]* gems_dict.get(reqd_gems[i])
        total_price= total_price + price

    else:
        total_price= -1

if total_price >30000:
    disc_amt= 0.05*total_price
    final_price= total_price - disc_amt
    print("Final amount: Rs ", final_price)

else:
    print("Final amount: Rs ", total_price)



