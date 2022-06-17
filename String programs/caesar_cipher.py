def CustomerCaesarCipher(key, input_string):
    encrypt_text= ''
    
    for i in range(len(input_string)):
        char= input_string[i]

        if char.isupper():
            encrypt_text += chr((ord(char) + key - 65) %26 + 65)

        elif char.islower():
            encrypt_text += chr((ord(char) + key - 97) %26 + 97)

        elif char.isdigit():
            encrypt_text += str(int(char) + key)

        elif char== '-':
            encrypt_text += '-'

        elif char.isspace():
            encrypt_text += ' '

    return encrypt_text


input_string= input("Enter your plain text: ")
key= input("Enter key: ")

output_string= CustomerCaesarCipher(key, input_string)

print("Encrypted text : ",output_string)
