# write a code to calculate and display the final fees to be paid by each student.
# You may accept the branch of study, score and course fee as inputs for each student
# and calculate the final fees to be paid by each student based on formulae given below:
# Scholarship amount=course fee * (scholarship%)
# Final fee= course fee - scholarship amount


branch= input("Enter the branch: ")
score= int(input("Enter your score: "))
course_fee= int(input("Enter course fee amount: "))

if branch== "arts" or branch=="Arts":
    if score>= 90:
        sch_percent= 0.5
    else:
        if score%2 != 0:
            sch_percent= 0.05

if branch== "engineering" or branch== "Engineering":
    if score> 85:
        sch_percent= 0.5
    else:
        if score%7 == 0:
            sch_percent= 0.05

sch_amt= course_fee * sch_percent
final_fee= course_fee - sch_amt

print("Final fee amount= ",final_fee)
