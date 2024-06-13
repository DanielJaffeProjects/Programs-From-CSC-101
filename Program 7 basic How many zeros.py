#Program 7 Basic: How many zeros
#This program test the difference between chatgpt and my program to take a number and determine how many zeros occurs from 1 to the inputed number 
#Daniel Jaffe
#Date Modified: 3/26/24

from time import time
# This is chatGPT program

#Counts how many zeros their using string method
def count_zeros(num):
    zero_count = 0
    for i in range(1, num + 1):
        zero_count += str(i).count('0')
    return zero_count

def main():
    num = int(input("Enter a number: "))
    start = time()
    zeros = count_zeros(num)
    end = time()
    print(f"The number of zeros from 1 to {num} is: {zeros}")
    print("ChatGPT took {:.10f} seconds".format(end-start))


if __name__ == "__main__":
    main()

# This is my program

#Counts how many zeros their using integers method
def count_int(num2):
    counter = 0
    j = 0
    for i in range(1,num2+1):
        j = i
        while j > 9:
            if j%10 == 0:
                counter +=1
            j = j//10
    print("The number of zeros from 1 to {}  is : {}".format(num2,counter))
    
#Main program
num2 = int(input("Input a number: "))
start2 = time()
count_int(num2)
end2 = time()
print("My program took {:.10f} seconds".format(end2-start2))
#Conclusion chatgpt code is faster for bigger numbers while my code is faster for smaller numbers