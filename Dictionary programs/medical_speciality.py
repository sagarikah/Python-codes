##    Care hospital wants to know the medical speciality visited by the maximum number of patients.
##    Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list.
##    The details of the medical specialities are stored in a dictionary as follows:
##
##         { "P":"Pediatrics", "O":"Orthopedics", "E":"ENT }
##
##    Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
##
##        Sample Input	                       Expected Output
##     [101,P,102,O,302,P,305,P]	        Pediatrics
##     [101,O,102,O,302,P,305,E,401,O,656,O]     Orthopedics



dict= {"P":"Pediatrics", "O":"Orthopedics", "E":"ENT"}

list= []
count_p= 0
count_o= 0
count_e=0

num_patients= int(input("Enter number of patients: "))

for i in range(num_patients):
    patient_id= input("Enter the patient id : ")
    list.append(patient_id)
    speciality= input("Enter the speciality visited : ")
    list.append(speciality)

for i in range(num_patients):
    if list[i] in dict:
        if list[i] == "P":
            count_p= count_p+1
        elif list[i] == "O":
            count_o= count_o+1
        else:
            count_e= count_e+1

if count_p > count_o and count_p > count_e:
    print(dict.get("P"))

elif count_o > count_p and count_o > count_e:
    print(dict.get("O"))

else:
    print(dict.get("E"))
