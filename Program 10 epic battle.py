#Program 10 Epic battle!
#This program is a battle between the user and the computer were the user gets to choose a character to fight with 
#Daniel Jaffe
#Date modified 4/18/24

from random import choice
from random import randint

#Class for character
class character:
    def __init__(self,name,classtype,hp,strength,defense):
        self._name = name
        self._classtype = classtype
        self._hp = hp
        self._strength =strength
        self._defense = defense
        
#Getters
    def getname(self):
        return self._name
    def getclasstype(self):
        return self._classtype
    def gethp(self):
        return self._hp
    def getstrength(self):
        return self._strength
    def getdefense(self):
        return self._defense

#Setters
    def setname(self,name):
        self._name = name
    def setclasstype(self,classtype):
        self._classtype = classtype
    def sethp(self,hp):
        self._hp = hp
    def setstrength(self,strength):
        self._strength = strength
    def setdefense(self,defense):
        self._defense = defense
        
    name = property(getname,setname)
    classtype = property(getclasstype,setclasstype)
    hp = property(gethp,sethp)
    strength = property(getstrength,setstrength)
    defense = property(getdefense,setdefense)
        
        
    def calculate_attack(self,opponent_defense,opponents_hp):
        attack = round(float(self._strength*(1-opponent_defense)),1)
        return attack
    
    def calculate_defense(self,opponent_strength):
        self._hp = (opponent_strength*(1-self._defense))-6
        
    def is_still_alive(self):        
        if self._hp <= 0:
            return False
        else:
            return True
        
#Main program
user_name = input("Enter your name: ")
user_classtype = input("Choice your class type: ")

#Initializes class types abilities
if user_classtype == "Sword Fighter":
    user_hp = 120
    user_strength = 40
    user_defense = 0.2
elif user_classtype == "Unicorn":
    user_hp = 80
    user_strength = 35
    user_defense =0.6
elif user_classtype == "Battle Monk":
    user_hp = 100
    user_strength = 20
    user_defense = 0.42
else:
    print("User not found")
    
    
user = character(user_name,user_classtype,user_hp,user_strength,user_defense)

#Look up the choice function on chatgpt
computer_name = choice(["Megabyte","Hex","Glitch"])
computer_classtype = choice(["Battle Monk","Sword Fighter","Unicorn"])

if computer_classtype == "Sword Fighter":
    computer_hp = 120
    computer_strength = 40
    computer_defense = 0.2
elif computer_classtype == "Unicorn":
    computer_hp = 80
    computer_strength = 35
    computer_defense =0.6
elif computer_classtype == "Battle Monk":
    computer_hp = 100
    computer_strength = 20
    computer_defense = .42
else:
    print("User not found")
    
computer = character(computer_name,computer_classtype,computer_hp,computer_strength,computer_defense)

#Displaying both name and classtype of user and computer
print("{} the {}, your opponent is {} the {}!".format(user_name,user_classtype,computer_name,computer_classtype))

#Battling as long as both the computer and the user hp is above 0
battle_round = 1

while computer.is_still_alive() and user.is_still_alive():
    user_action = input("Do you (a)ttack or (d)defend? ")
    computer_action = choice(["a","d"])
    
    print("-Round {}-".format(battle_round))
    
    #User and computer attacks
    if user_action == "a" and computer_action == "a":     
        print("{} the {} attacked {} the {}!".format(user_name,user_classtype,computer_name,computer_classtype))       
        computer.hp = computer.hp - user.calculate_attack(computer.defense,computer.hp)
        print("{} now has {} HP.".format(computer_name,computer.hp))
        
        print("{} the {} attacked {} the {}!".format(computer_name,computer_classtype,user_name,user_classtype))
        user.hp = user.hp - computer.calculate_attack(user.defense,user.hp)
        print("{} now has {} HP.".format(user_name,user.hp))
        
    if user_action =="d" and computer_action == "d":
        print("{} the {} is on guard".format(user_name,user_classtype))
        print("{} the {} is on guard".format(computer_name,computer_classtype))
        
    if user_action == "d" and computer_action == "a":
        print("{} the {} is on guard".format(user_name,user_classtype))
        print("{} the {} attacked {} the {}!".format(computer_name,computer_classtype,user_name,user_classtype))
        user.hp = user.hp - computer.calculate_attack(user.defense,user.hp)
        print("{} now has {} HP.".format(user_name,user.hp))

    if user_action == "a" and computer_action == "d":
        print("{} the {} attacked {} the {}!".format(user_name,user_classtype,computer_name,computer_classtype))
        print("{} the {} is on guard".format(computer_name,computer_classtype))
        computer.hp = computer.hp - user.calculate_attack(computer.defense, computer.hp)
        print("{} now has {} HP.".format(computer_name,computer.hp))
    
    battle_round += 1

if user.is_still_alive():
    print("{} the {} was defeated...".format(computer_name,computer_classtype))
    print("{} the {} wins!".format(user_name,user_classtype))
elif computer.is_still_alive():
    print("{} the {} was defeated...".format(user_name,user_classtype))
    print("{} the {} wins!".format(computer_name,computer_classtype))
else:
    print(f"{user_name} and {computer_name} had a draw")
