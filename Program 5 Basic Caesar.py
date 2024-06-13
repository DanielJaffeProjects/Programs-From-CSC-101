#Program 5 Basic: Caesar
#This program solves a caesar encription and gives you how long it took
#Daniel Jaffe
#Last modified 3/13/24



from time import time
import string

#Subroutine for the caesar formula
def caesar(encription):
    alphabet = string.ascii_letters

    for line in encription:
        shift = 1
        array_encription =[]
        print("Cyphertext: " + line.strip("\n"))
        
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
        print(''.join(array_encription))
        
#Main Program
encription = open("ciphertexts.txt",'r') 
start = time()
caesar(encription)
end = time()
print("Process took {} seconds".format(end-start))
encription.close()