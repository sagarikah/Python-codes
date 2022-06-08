#   Rate per Adult: Rs. 37550.0
#   Rate per Child: 1/3rd of the rate per adult
#   Service Tax: 7% of the ticket amount (including all passengers)
#   As it was a holiday season, the airline also offered a 10% discount on the final ticket cost (after inclusion of the service tax).
#   Find and display the total ticket cost for a group which had adults and children.


adults= int(input("Enter number of adults: "))
children= int(input("Enter number of children: "))

ticket_amt_adults= adults * 37550
ticket_amt_children= children * 12516.66
ticket_amt= ticket_amt_adults + ticket_amt_children

tax_amt= 0.07 * ticket_amt
tot_ticket_amt= ticket_amt + tax_amt

disc_amt= 0.1 * tot_ticket_amt
final_amt= tot_ticket_amt - disc_amt

print("Final ticket amount= ",final_amt)
print("Have a Happy Journey !!!")

