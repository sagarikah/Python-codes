num_int_walls= int(input("Enter number of interior walls: "))
num_ext_walls= int(input("Enter number of exterior walls: "))

surf_area_int_list= []
surf_area_ext_list= []

cost_int= 0
cost_ext= 0

if num_int_walls >= 0:
    for i in range(num_int_walls):
        surf_area_int= float(input("Enter surface area of interior wall: "))
        surf_area_int_list.append(surf_area_int)

if num_ext_walls >= 0:
    for i in range(num_ext_walls):
        surf_area_ext= float(input("Enter surface area of exterior wall: "))
        surf_area_ext_list.append(surf_area_ext)

if len(surf_area_int_list) > 0:
    for i in range(len(surf_area_int_list)):
        cost_int += surf_area_int_list[i] * 18

if len(surf_area_ext_list) > 0:
    for i in range(len(surf_area_ext_list)):
        cost_ext += surf_area_ext_list[i] * 12

total_cost= cost_int + cost_ext
print("Total cost: ",total_cost)
                           
