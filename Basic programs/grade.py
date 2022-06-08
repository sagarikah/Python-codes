# A teacher in a school wants to find and display the grade of a student based on his/her percentage score.
# The criterion for grades is as given below:

#   Score (both inclusive)	Grade
#      Between 80 and 100	A
#      Between 73 and 79	B
#      Between 65 and 72	C
#       Between 0 and 64	D
#        Any other value	Z

# Assume that the percentage score is a whole number. Write a python program for the above requirement.



score= int(input("Enter your score: "))

if score>=80 and score<=100:
    print("Grade : A")

elif score>=73 and score<=79:
    print("Grade : B")

elif score>=65 and score<=72:
    print("Grade : C")

elif score>=0 and score<=64:
    print("Grade : D")

else:
    print("Grade : Z")
