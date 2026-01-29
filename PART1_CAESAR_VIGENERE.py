#GOAL: Encrypt/Decrypt using two different techniques implemented as separate functions: Caesar Cipher and Vigenere Cipher

#Caesar Cipher Function
def caesar_cipher(message, shift, encrypt):
    result = ""

    #Define the language and its range of total 95 characters
    lang_start = 32
    lang_end = 126
    lang_range = lang_end - lang_start + 1 

    #Language translation stream for each character unit
    for char in message:
        ASCII_code = ord(char) #Converts ASCII Symbol to ASCII code

        #Shift forward by [shift] for ENCRYPT[TRUE]
        #Shift backward by [shift] for DECRYPT[FALSE]
        if encrypt:
            ASCII_code += shift
        else: 
            ASCII_code -= shift

        #Wrap around the language to remain within symbols 32-126, inclusive
        while ASCII_code > lang_end: #upper limit
            ASCII_code -= lang_range

        while ASCII_code < lang_start: #lower limit
            ASCII_code += lang_range

        #Converts ASCII code back to ASCII symbol
        result += chr(ASCII_code)

    return result

#Vigenere Cipher Function
def vigenere_cipher(message, keyword, encrypt):
    result = ""
    index = 0

    #Language translation stream for each character unit
    for char in message:
        #If end of keyword is reached, go back to start index of keyword
        if index == len(keyword):
            index = 0
        keyword_char = keyword[index] #select the keyword character from keyword at current index

        #Calculates caesar_cipher's 'shift' value according to Vigenere Cipher Rules
        shift = ord(keyword_char) - 32

        #Reuse caesar_cipher to Encrypt/Decrypt only one characte using the updated shift
        shifted_char = caesar_cipher(char, shift, encrypt)

        result += shifted_char #Append the new character to final output (result)
        index += 1 #Update index to move to the next letter in keyword
    
    return result



#USER INTERACTION PROMPTS

#Prompts user for integer to select between cipher techniques: Caesar (1) or Vigenere (2)? 
cipher_choice = int(input("WELCOME! ENTER '1' FOR CAESAR CIPHER AND '2' FOR VIGENERE CIPHER: "))

#Prompts user for message
message = input("ENTER YOUR MESSAGE: ")

#User selected 1 - Caesar Cipher
if cipher_choice == 1:
        #Prompts user for integer for shift value
        shift = int(input("ENTER THE SHIFT [INTEGER]: ")) 
        
#User selected 2 - Vigenere Cipher
elif cipher_choice == 2:
        #Prompts user for keyword for Vigenere implementation
        keyword = input("ENTER THE KEYWORD: ")
#Handles anything User inputs other than '1' or '2'
else: 
     print("INVALID CIPHER CHOICE")
     exit()

#Prompt user - Encrypt or Decrypt?
while True: 
    boolean_choice = input("ENTER 'TRUE' to ENCRYPT - or - 'FALSE' to DECRYPT: ").lower() #.lower() for case-insensitive
    if boolean_choice == "true": #ENCRYPT
        encrypt = True
        break
    elif boolean_choice == "false": #DECRYPT
        encrypt = False
        break
    else:
        print("INVALID INPUT FROM USER. PLEASE TYPE 'TRUE' OR 'FALSE'") #Error if user enters something weird/unexpected

#FINAL OUTPUT
if cipher_choice == 1:
    result = caesar_cipher(message, shift, encrypt) #call caesar_cipher function + store result
elif cipher_choice == 2:
    result = vigenere_cipher(message, keyword, encrypt) #call vigenere_cipher function + store result

print("RESULT: " + result)




