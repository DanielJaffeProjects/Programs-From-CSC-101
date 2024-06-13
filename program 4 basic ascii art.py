#program 4 Ascii Art
#Daniel Jaffe
#This program is taking a file and making the content into a image
#Date modified 2/27/24

#subroutine for processing lines
def line_into_array(art):
    for line in art:
        line = line.rstrip("\n")
        #Checks if the line has a space or not
        if line =="":
            print()
        else:
            #Split each line into a array
            line = line.split()
            if line[1] == "..":
                line[1] = ' '
            #Multiplies the first thing in the array by the second thing in the array
            result = int(line[0])* line[1]
            #Used ChatGPT end function to solve my problem of getting the line to all combine
            print(result, end="")
   
#Main program
art = open('ascii2-data.txt','r')
line_into_array(art)
print("Why did the hourglass go to therapy? It had too much time on its hands and was feeling a little 'stressed out!'")
art.close()