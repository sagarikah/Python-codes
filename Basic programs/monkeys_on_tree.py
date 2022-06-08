total_monkeys= int(input("Enter total number of monkeys in tree: "))
num_banana= int(input("Enter number of bananas single monkey can eat: "))
num_peanut= int(input("Enter number of peanuts single monkey can eat: "))
total_banana= int(input("Enter total number of bananas: "))
total_peanut= int(input("Enter total number of peanuts: "))

if total_monkeys <=0 or num_banana <=0 or num_peanut <=0 or total_banana<=0 or total_peanut <=0:
    print("Invalid input")

else:
    monkeys_on_ground= total_banana//num_banana
    monkeys_on_ground += total_peanut//num_peanut

    if total_banana % num_banana != 0 or total_peanut % num_peanut != 0:
        banana_left = total_banana % num_banana
        peanut_left= total_peanut % num_peanut
        monkeys_on_ground += 1

    monkeys_on_tree= total_monkeys - monkeys_on_ground

    print("Number of monkeys left on the tree: ",monkeys_on_tree)

    
        
                  
                   
