parent_name= input("Enter parent member name: ")
child= input("Enter Y if parent member has child members otherwise enter N: ")

total_members= 1
child_list= []


if child == "Y":
    child_name = input("Enter names of child members: ")

    child_list= child_name.split(",")
    
    total_members += len(child_list)

    parent_comm= len(child_list)*(0.1*5000)

elif child == "N":
    parent_comm= 0.05 * 5000

else:
    print("Invalid input")
    parent_comm= 0.05 * 5000
    
    
print("Total members: ",total_members)
print("Comission details:")
print(parent_name +": " + str(parent_comm) +" INR")

if child == "Y":
    for i in range(len(child_list)):
        child_list_comm= 0.05 * 5000
        print(child_list[i] +": " + str(child_list_comm) +" INR")


