#Program 6 Basic: Brutus
#This program finds the caesar encription then gives only the encripted part
#Daniel Jaffe
#Last modified 3/20/24

#Note I use the sample file because of the long time it took for the other file
from time import time
import string

#Subroutine for the caesar formula
def caesar(encription):
    alphabet = string.ascii_letters
    array_encription =[]
    for line in encription:
        shift = 1
        
        while shift < 26:
            array_encription.append("Shift " + str(shift) + ": ")
            for char in line:
            #Used Chatgpt for the is alpha function
            #checks if the character in the line is a alphabet
                if char.isalpha():
                    #shift the letter 2
                    newshiftval = ord(char)+shift
                    if newshiftval >= 91:
                        newshiftval = newshiftval - 26
                    #Used chatgpt for chr and ord functions
                    array_encription.append(chr((newshiftval)))
                #If the char in the line is not in the alphabet append it without changing it
                else:
                    array_encription.append(char)
            shift += 1
        #Used ChatGPT for the join function
    array =(''.join(array_encription))
    return(array)


#Putting all the words in the text into a array
def array_words(lines):
    array_of_words = []    
    #Removing all the extra blank lines and appending it the array
    for word in lines:
        word=word.rstrip("\n")
        array_of_words.append(word.upper())
    return(array_of_words)
    
    

# This compares the words from the caesar txt and the dictionary of words and determines whether it has real words in the sentence
def comparing_words(caesar_array,dictionary,encription2):
    resulting_array = []
    number_trials = 0
    
    cipher_text = []
    for line in encription2:
        cipher_text.append(line)

    #Taking the array and spliting per line
    for line in caesar_array:
        resulting_array = caesar_array.split("\n")
        
    #taking the resulting array and spliting into sentence then comparing each word inside the sentence to the dictionary word
    for sentence in resulting_array:
        counter = 0
        sentence = sentence.split(" ")
        length_sentence = len(sentence)
        for i in sentence:
            for word in dictionary:
                if i == word:
                    counter += 1
        if counter/length_sentence >= 0.40:
            print("Ciphertext: " + str(cipher_text[number_trials]).strip('\n'))
            print(' '.join(sentence)+'\n')
            number_trials +=1

#Main Program
encription = open("ciphertexts-SAMPLE (1).txt",'r')
#My code wasnt working with the other encription so I decided 2 is better than 1 ;)
encription2 = open("ciphertexts-SAMPLE (2).txt",'r')
words = open("words.txt",'r')

start = time()
caesar_array = caesar(encription)
dictionary = array_words(words)
comparing_words(caesar_array,dictionary,encription2)
end = time()

print("Process took {} s".format(end-start))
encription.close()


