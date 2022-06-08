m= int(input())
n= int(input())

if m<n and 0<m<999 and 1<n<=999:
    temp= m
    
    if temp<10 and n<10:
        while temp<=n:
            temp_str= "0"+ str(temp)      
            print(int(temp_str))
            temp+=1
            
