##    Words Frequency in String
##
##    Input : test_str = ‘Gfg is best’
##    Output : {‘Gfg’: 1, ‘is’: 1, ‘best’: 1}
##
##    Input : test_str = ‘Gfg Gfg Gfg’
##    Output : {‘Gfg’: 3}




s = input("Enter a string: ")

list_s = s.split()
list_unique = []

for i in range(0,len(list_s)):
    if list_s[i] not in list_unique:
        list_unique.append(list_s[i])

        
frequency = []
count = 0

for i in range(0,len(list_unique)):
    for j in range(0,len(list_s)):
       if list_unique[i] == list_s[j]:
           count += 1
    frequency.append(count)
    count = 0   
 
       
Dict = {}

for i in range(0, len(list_unique)):
    key = str(list_unique[i])
    Dict[key] = frequency[i]

print(Dict)
