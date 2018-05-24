import random
from random import sample, shuffle

print("\n\t\tWELCOME TO MARVEL STUD10S\n")
print("\tLET'S MAKE A TEAM OF OUR SUPERHEROES TO DEFEAT 'THANOS'\n")
print("    INSTRUCTION: We can make a team of four superheroes, in which you are supposed to choose two.\n")

print("\t0 = Captain America\n"
      "\t1 = Ironman\n"
      "\t2 = Thor\n"
      "\t3 = Spiderman\n"
      "\t4 = Doctor Strange\n"
      "\t5 = Star-Lord\n"
      "\t6 = Gamora\n"
      "\t7 = Hulk\n"
      "\t8 = Black Panther\n"
      "\t9 = Black Widow\n")
str = ["Captain America", "Ironman", "Thor", "Spiderman", "Doctor Strange", "Star-Lord", "Gamora", "Hulk",
       "Black Panther", "Black Widow"]
my_choices = sample(str, 2)
shuffle(my_choices)
print("\tThese are my choices:", my_choices)
print("\t Choose two Superheroes from the remaining\n")
user_choice1 = int(input())
if user_choice1==int(str.index(my_choices[0])) or user_choice1==int(str.index(my_choices[1])):
    print("Please select from the remaining superheroes\n")
    exit()

user_choice2 = int(input())
if user_choice2==int(str.index(my_choices[0])) or user_choice2==int(str.index(my_choices[1])):
    print("Please select from the remaining superheroes\n")
    exit()

def power(p):
    if p == 0:
        return 32
    elif p == 1:
        return 28
    elif p == 2:
        return 16
    elif p == 3:
        return 20
    elif p == 4:
        return 18
    elif p == 5:
        return 22
    elif p == 6:
        return 33
    elif p == 7:
        return 21
    elif p == 8:
        return 34
    elif p == 9:
        return 30
    else:
        print("Please enter valid numbers\n")
        return 0
        exit()


pow_team = power(user_choice1) + power(user_choice2) + power(int(str.index(my_choices[0]))) + power(int(str.index(my_choices[1])))

pow_thanos = 100
if pow_team > pow_thanos:
    print("\t\tHola!!Your choice was BEST\n")
    print("\t\t WE DEFEATED THANOS :) :)\n")
elif pow_team < pow_thanos:
    print("\t\t UH-OH!! TEAM WAS INEFFICIENT :( :(\n"
          "\t\t    LET'S TRY AGAIN!! :)\n")