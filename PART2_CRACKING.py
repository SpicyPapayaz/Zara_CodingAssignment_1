#CODING PART OF PART 2 OF ASSIGNMENT (2.2-2.4)
#--------------------------------------------------------------------
#2.2 FREQUENCY ANALYSIS
#GOAL: Given a string via input and a predetermined alphabet, print
#frequency count of EACH letter in the alphabet
#--------------------------------------------------------------------

#frequency_analysis Function
def frequency_analysis(text):
    #Alphabet (symbols) and its total length (syn_len)
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    sym_len = len(symbols)
    count = {} #empty raw count dictionary

    #Indv. cycle through full range of symbols 
    for char in symbols:
        count[char] = 0 #initialize all raw counts to 0

    #Pass through each character in text and increment count upon each repeated instance
    #Counts occurrences 
    for char in text:
        if char in count:
            count[char] += 1
    
    total = len(text) #total length of text

    frequency = {} #empty frequency dictionary
    for char in symbols:
        frequency[char] = count[char]/total #Compute frequency

    return frequency

#--------------------------------------------------------------------
#2.3 CROSS-CORRELATION
#GOAL: to calculate cross-correlation among the sets provided. 
#Cross-correlation = sum of (English letter frequency × shifted ciphertext 
#letter frequency) for all letters.
#ANSWERS FOR 2.3 CHART IN ASSIGNMENT: 
#Cross-correlation of Set 1 and Set 2:  0.003098
#Cross-correlation of Set 1 and Set 3:  0.00254
#--------------------------------------------------------------------

#cross_correlation Function
def cross_correlation(X, Y, entries):
    result = 0
    for entry in entries:
        result += X[entry] * Y[entry] #Formula for cross-correlation
    return result

#--------------------------------------------------------------------
#2.4 CAESAR CRACKING
#GOAL: Determines the likely shift (int) used in Caesar cipher encryption
#--------------------------------------------------------------------

#get_caesar_shift Function
def get_caesar_shift(enc_message, expected_dist):

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    sym_len = len(letters)
    best_shift = 0 #best shift value
    best_CC_score = -1 #best cross-correlation score

    for shift in range(sym_len): #iterates thru all possible shifts
        #Caesar cipher
        shifted_text = ""
        #For each char in the encrypted message...
        for char in enc_message:
            if char in letters:
                index = letters.index(char) #find char's index in 'symbols'
                new_index = (index - shift) % (sym_len - 1) #Caesar shift backwards
                shifted_text += letters[new_index] #appends new character
            
        #Get frequency number values
        frequency = frequency_analysis(shifted_text)

        #Get CC Score
        entries = [letter for letter in expected_dist if letter != " "]
        CC_score = cross_correlation(frequency, expected_dist, entries)
        ##########
        #Keep the (best) shift with HIGHEST associated CC score
        if CC_score > best_CC_score:
            best_CC_score = CC_score
            best_shift = shift

    return best_shift

#--------------------------------------------------------------------
#2.4 VIGENERE CRACKING
#GOAL: given a ciphertext, and using brute force, gives us the candidates for the vigenere keywords
#--------------------------------------------------------------------

#get_vigenere_keyword Function
def get_vigenere_keyword(enc_message, size, expected_dist):
    #alphabet
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    keyword = "" #initializing empty string to store keyword
    clean_message = enc_message.replace(" ", "") #removes spaces from msg
    #Create empty strings for columns w/ the same size as the key length
    sep_messages = [""] * size

    #loop to distribute letters over columns
    for i, char in enumerate(clean_message):
        column = i % size
        sep_messages[column] += char

    #loops over each column
    for message in sep_messages:
        shift = get_caesar_shift(message, expected_dist) #finds caesar shift
        keyword += letters[shift] #converts shift value to a letter, then append to keyword

    return keyword
#--------------------------------------------------------------------
#MAIN PROGRAM 

#PART 2.2 FREQUENCY ANALYSIS
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
#USER PROMPT
text = input("WELCOME TO FREQUENCY ANALYZER!\nENTER TEXT: ")
#OUTPUT
frequency = frequency_analysis(text)
print("RESULT: \n")
for char in symbols:
        print('"' + char + '": ' + str(frequency[char]) + "\n")
        #Converted int frequency[char] to string for concat purposes to print


#PART 2.3 CROSS-CORRELATION

#Data from given table
set1 = {'A':0.012, 'B':0.003, 'C':0.01, 'D':0.1, 'E':0.02, 'F':0.001}
set2 = {'A':0.001, 'B':0.012, 'C':0.003, 'D':0.01, 'E':0.1, 'F':0.02}
set3 = {'A':0.1, 'B':0.02, 'C':0.001, 'D':0.012, 'E':0.003, 'F':0.01}
entries = ['A','B','C','D','E','F']
#OUTPUT
print("ANSWER TO SECTION 2.3 QUESTION")
print("Cross-correlation of Set 1 and Set 2: ", cross_correlation(set1, set2, entries))
print("Cross-correlation of Set 1 and Set 3: ", cross_correlation(set1, set3, entries))
print("")

#PART 2.4 CAESAR CRACKING

#Given dictionary ("typical" English letter frequencies)
expected_dist = {' ': .1828846265,'E': .1026665037, 'T': .0751699827, 'A': .0653216702, 'O': .0615957725, 'N':
.0571201113, 'I': .0566844326,'S': .0531700534,'R': .0498790855,'H': .0497856396,'L': .0331754796,'D':
.0328292310,'U': .0227579536,'C': .0223367596,'M': .0202656783,'F': .0198306716,'W': .0170389377,'G':
.0162490441,'P': .0150432428,'Y': .0142766662,'B': .0125888074,'V': 0.0079611644,'K': 0.0056096272,'X':
0.0014092016,'J': 0.0009752181,'Q': 0.0008367550,'Z': 0.0005128469}

#USER PROMPT
enc_message = input("WELCOME TO CAESAR CRACKING PROGRAM!\nENTER ENCRYPTED TEXT: ")
#OUTPUT
shift = get_caesar_shift(enc_message, expected_dist)
print("LIKELY SHIFT USED TO ENCRYPT: ", shift)

#PART 2.4 VIGENERE CRACKING
#USER PROMPT
enc_message = input("\nWELCOME TO VIGENERE CRACKING PROGRAM USING KASISKI METHOD!\nENTER CIPHER TEXT: ")

#Brute Force implementation
print("\nVIGENERE CRACKING USING SIMPLIFIED KASISKI METHOD: \n")
#brute force the length of the key til you find the right keyword
for size in range(1, 20): #try key lengths 1 thru 20
    keyword = get_vigenere_keyword(enc_message, size, expected_dist)
    #OUTPUT
    print("KEY LENGTH ", size, " -> ", keyword)