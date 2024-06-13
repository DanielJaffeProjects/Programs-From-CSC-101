#Program 9: Getting Across
#This program is caculates how many possiblities their are to cross the path
#Daniel Jaffe
#Date Modified 4/12/24


#A recursion to count how many paths the user could take
def paths(individual_path,index):
    if index >= len(individual_path):
        return 0
    if individual_path[index] == "^":
        return 0

    if index == len(individual_path) - 1:
        return 1
    
    return paths(individual_path,index + 1) + paths(individual_path,index + 2)
        
    
# Main program
path_txt = open("paths.txt","r")
path = []
for line in path_txt:
    path.append(line.rstrip("\n"))
for individual_path in path:
    print("Path: : " + individual_path)
    path_possiblities = paths(individual_path,0)
    print("Number of posssible ways across: " + str(path_possiblities))
