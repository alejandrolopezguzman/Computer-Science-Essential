#This is a text based game about escaping a set of rooms

#Rock Paper Scizzor Generator
import random

#Variables
key = False
knife = False
end = True
shotgun = False
rts = -1

#generate 1,2, or 3 for RPS
def RPS ():
    NM = round(float(random.randint(1,3)))
    return NM

#Code
print("Welcome to Wish.com Saw")
print("")
print("You wake up.")
while end == True:
    #Starting room
    print("Your locked in a room with no doors, with a key on the left wall and a shotgun on the right, and a hole in the ceiling ")
    choice=input("Do you A. Grab the key  B. Jump up through the hole C.Cry in a corner and do nothing D. Grab the shotgun (Use capital letters)")
    if choice == "D":
        if knife == True:
            print("You got the shotgun")
            shotgun = True
        else:
            print("You couldn't grab the shotgun, you need to cut it free")
    if choice == "A":
        if knife == True:
            print("You got the key")
            key = True
        else:
            print("You couldn't grab the key, you need to cut it free")
    if choice == "C":
        print("You stayed in the room and cried yourself to death.")
        print("THE END")
        break
    if choice == "B":
        while(True):
            #Middle room
            print("You climbed out the room.There is a room to your left and right")
            choice = input("Do you  A. Go to the right room  B. Go to the left room C. Go back")
            if choice == "A":
                #Right room
                print("There is a guy blocking the door")
                choice = input("Do you A.Play him in Rock Paper Scizzors or B. Fight him")
                if choice == "A":
                    J = RPS()
                    #print(J)
                    print("You entered a Rock Paper Scizzors Battle")
                    rts = int(input("1. Rock   2. Paper   3. Scizzors (Use the numbers)"))
                    if rts == J:
                        print("You won and he despawned")
                        print("You entered the room he was guarding, it is a small closet with a knife on a pedestal")
                        choice = input("Do you A. pick up the knife or B. just leave the room")
                        if choice == "A":
                            print("You picked up the knife and left")
                            knife = True
                        if choice == "B":
                            print("You left the room without the knife")
                        print("The guy respawned")
                    else:
                        print("You lost, better luck next time")
                        
                if choice == "B":
                    if shotgun == True:
                       print("You took him out, but there is nothing left in the room, so you left")
                       print("The guy respawned")

                    else:
                        print("He's to strong, you'll need a long range weapon")  
            if choice == "C":
                #Go back to OG room
                print("You went back down the hole into the first room")
                break              
            if choice == "B":
                #Left room
                print("You go in the room and there is nothing but a hypnotizing room and a locked door that says exit")
                choice = input("Do you A. stay or B. leave or C. Try the lock")
                if choice == "A":
                    while(True):
                        print("You go Insane")
                        print("")
                        print("The End")
                        breakpoint
                if choice == "B":
                    print("You left the room")
                if choice == "C":
                    if key == True:
                        print("Concratulations, You Escaped The Death Trap")
                        print("You achieved the TRUE ENDING")
                        end = False
                        break
                    else:
                        print("The door's locked, you will need a key.")


print("Made by Alejandro")
