# File Handling


Hi_file = open("Hi.txt","r")
text = Hi_file.read()
print(text)
Hi_file.close()




Hi_file =open("Hi.txt","w")
Hi_file.write("Good Morning !!!")
Hi_file.close()



Hi_file = open("Hi.txt","r")
new_text = Hi_file.read()
print(new_text)
Hi_file.close()







