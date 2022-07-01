##    Convert Snake case to Pascal case
##
##    Input : geeks_for_geeks
##    Output : GeeksForGeeks
##
##    Input : left_index
##    Output : LeftIndex




s = input("Enter a string: ")

list_s = s.split('_')

res = ''

for i in range(0, len(list_s)):
    word = list_s[i]
    up = word.capitalize()
    res += up

print(res)
