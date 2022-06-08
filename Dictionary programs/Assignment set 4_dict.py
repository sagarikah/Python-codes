#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    #word=""
    #frequency=0
    #dict= {}
    
    data_list= data.split()
    count_list= []
    
    for i in data_list:
       frequency= data_list.count(i)
       count_list.append(frequency)
       
    max_frequency= count_list[0]
    
    for i in count_list:
        if i> max_frequency:
           max_frequency= i 
            
    word_max_list= []

    for i in range(len(data_list)):
        if data_list.count(data_list[i])== max_frequency:
            word_max_list.append(i)

    if len(word_max_list)==1:
        word_max= word_max_list[0]

    else:
        length= 1

        for i in range(len(word_max_list)):
            if len(word_max_list[i])>length:
                word_max= word_max_list[i]
        
    print(word_max +' '+str(max_frequency))
        
    #start writing your code here
    #Populate the variables: word and frequency


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data="Rain on the green grass and Rain on the tree"
max_frequency_word_counter(data)
