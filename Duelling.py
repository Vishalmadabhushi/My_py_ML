import random

print("\t\t   DUELLING\n")
print("\t LET'S START THE GAME\n")
print("  HARRY POTTER vs DRACO MALFOY\n")
print("Select your character\nType 1 for HARRY POTTER, 2 for DRACO MALFOY\n")
ip_char = int(input())
if(ip_char==1):
    print("You are now HARRY POTTER\n")
elif(ip_char==2):
    print("You are now DRACO MALFOY\n")
else:print("Select Again")
user_power = 100
my_power = 100
print("\t Your power = ",user_power)
print("\t Opponent's power = ",my_power)
print("\n\t USE THE FOLLOWING SPELLS \n")
print("\t1   =   RIDDIKULUS\n\n" \
      "\t2   =   EXPELLIARMUS\n\n" \
      "\t3   =   SECTUM SEMPRA\n\n" \
      "\t4   =   EXPECTO PATRONUM\n\n" \
      "\t5   =   STUPEFY\n\n" \
      "\t6   =   REDUCTO\n\n" \
      "\t7   =   CRUCIO\n\n" \
      "\t8   =   PETRIFICUS TOTALUS\n\n")
def power(p):

    if p == 1:
        return 11
    elif p == 2:
        return 8
    elif p == 3:
        return 36
    elif p == 4:
        return 43
    elif p == 5:
        return 24
    elif p == 6:
        return 31
    elif p == 7:
        return 45
    elif p == 8:
        return 39
    else:
        print("enter valid spell number\n")
        exit()
i = 1

while user_power>0 and my_power>0 and i <= 8:
    my_spell = random.randint(1,8)
    print("Choose Your Spell\n")
    user_spell = int(input())
    print("\t",user_spell,"vs",my_spell)

    userspell_power = power(user_spell)
    myspell_power = power(my_spell)
    my_power = my_power - userspell_power
    user_power = user_power - myspell_power
    if user_power<=0:
        print("uh-oh!! Your power is completely drained")
    if my_power<=0:
        print("Hola!! Opponent is dead!!")
    if my_power>0 and user_power>0:
        print("\tOpponent's power left now = ",my_power)
        print("\n\tYour power now = ",user_power)
    i=i+1

if user_power > my_power:
    print("\tYOU WIN\n")
    exit()
elif user_power < my_power:
    print("\tYOU LOSE\n")
    exit()
else:
    print("\tEQUALITY WINS\n")
exit()

