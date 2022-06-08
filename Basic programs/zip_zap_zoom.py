# Write a python program that displays a message as follows for a given number:
#   If it is a multiple of three, display "Zip"
#   If it is a multiple of five, display "Zap".
#   If it is a multiple of both three and five, display "Zoom".
#   If it does not satisfy any of the above given conditions, display "Invalid".


num= int(input("Enter a number: "))

if num %3== 0 and num%5== 0:
    print("ZOOM")

elif num %3== 0:
    print("ZIP")

elif num %5== 0:
    print("ZAP")

else:
    print("Invalid")
         
