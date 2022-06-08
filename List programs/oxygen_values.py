oxygen_val=[]

print("Enter the oxygen values:")
for i in range(0,9):
    n= int(input())
    if n>1 and n<=100:
        oxygen_val.append(n)
        
sum_1=0
for i in range(0,9,3):
    sum_1= sum_1+ oxygen_val[i]
avg_oxy_1= sum_1//3


sum_2=0
for i in range(1,9,3):
    sum_2= sum_2+ oxygen_val[i]
avg_oxy_2= sum_2//3


sum_3= 0
for i in range(2,9,3):
    sum_3= sum_3+ oxygen_val[i]
avg_oxy_3= sum_3//3


if max(avg_oxy_1,avg_oxy_2,avg_oxy_3) < 70:
    print("All trainees are unfit")
else:
    max_avg_oxy= max(avg_oxy_1,avg_oxy_2,avg_oxy_3)
    
    if max_avg_oxy== avg_oxy_1:
        print("Trainee number : 1")

    if max_avg_oxy== avg_oxy_2:
        print("Trainee number : 2")

    if max_avg_oxy== avg_oxy_3:
        print("Trainee number : 3")
