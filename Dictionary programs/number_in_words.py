# range: 1 - 1000

def integer_to_english(number):
    
    dict_ones= {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    dict_tens= {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
                20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}
    dict_hundreds= {100:'one hundred', 200:'two hundred', 300:'three hundred', 400:'four hundred', 500:'five hundred', 600:'six hundred',
                    700:'seven hundred', 800:'eight hundred', 900:'nine hundred'}

    if number<1 or number>1000:
        return -1

    elif number<10:
        word= dict_ones.get(number)
        return word

    elif number<100:
        if number in dict_tens:
            word= dict_tens.get(number)

        else:
            dig_ones= number%10
            word_ones= dict_ones.get(dig_ones)
            
            dig_tens= number - dig_ones
            word_tens= dict_tens.get(dig_tens)
            
            word= word_tens +' '+ word_ones
        
        return word

    elif number<1000:
        if number in dict_hundreds:
            word= dict_hundreds.get(number)
            return word

        else:   
            dig_tens= (number%100)
            if dig_tens in dict_tens:
                word_tens= dict_tens.get(dig_tens)
                
            else:
                dig_ones= number%10
                word_ones= dict_ones.get(dig_ones)
                word_tens= dict_tens.get(dig_tens-dig_ones) +' '+ word_ones
            
            dig_hundreds= (number//100)*100
            word_hundreds= dict_hundreds.get(dig_hundreds)
            
            word= word_hundreds +' '+ word_tens 
        
            return word

    else:
        word= 'one thousand'
        return word
    

number=999
print(integer_to_english(number))


