# Print all the even length words of a sentence

s= str(input("Enter a sentence: "))
size_s= len(s)
word= s.split(" ")
size_word= len(word)

for i in range(size_word):
   if(len(word[i])) % 2 == 0:
      print(word[i])

        


