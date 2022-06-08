##    Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
##
##    {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
##
##    and use it to translate your Christmas wishes from English into Swedish.
##
##    write a python function translate() that accepts the bilingual dictionary and a list of English words (your Christmas wish)
##    and returns a list of equivalent Swedish words.






def translate(dict,wish_list):
    swedish= []

    for i in range(len(wish_list)):
        if wish_list[i] in dict:
            word= dict.get(wish_list[i])
            swedish.append(word)

    return(swedish)
  


dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
wish= input("Enter your wish in English: ")

wish_list= wish.split()

print("Your wish in Swedish:")
print(translate(dict,wish_list))






