##    Remove i’th character from string
##
##    Input :
##        Enter a string : Geeks for geeks
##        Enter position : 4
##
##    Output:
##        Gees for geeks



s = input("Enter a string : ")
pos = int(input("Enter position : "))

res = []

for i in range(0, len(s)):
    if i != pos-1:
        res.append(s[i])

print(''.join(res))

