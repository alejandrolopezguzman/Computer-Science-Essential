#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06
burger = " "
side = " "
drink = " "
#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: KFC Double Down + Big Mac $10.99")
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)
            burger = ("Hamburger")

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)
            burger = ("Cheeseburger")

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
            burger = ("Western Burger")
        
        #BURGER 4: ADD ONE HERE
            #ADD A NEW BURGER OPTION AND UPDATE ALL CODE ABOVE TO MAKE IT WORK
        elif burgerChoice == "4":
            totalCost = totalCost+10.99
            print("You added KFC Double Down + Big Mac to your order")
            print("Your total cost so far: $", totalCost)
            burger = ("KFC Double Down + Big Mac")


            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid choice")
        
    elif menu == "Sides":
        print("We offer the following sides:")
        print("1: 10 Wcnuggets $7.99")
        print("2: Mac n' Cheese $6.99 ")
        print("3. 1 Carrot $20.99 ")
        sidesChoice = input("What would you like (input a number 1-3): ")
        #Add your Code/Comments Here for sides
        if sidesChoice == "1":
            totalCost = totalCost + 7.99
            print("You added 10 Wcnuggets to your order")
            print("Your total cost so far: S", totalCost)
            side = ("10 Wcnuggets")
        elif sidesChoice == "2":
            totalCost = totalCost + 6.99
            print("You added Mac n' Cheese to your order")
            print("Your total cost so far: S", totalCost)
            side = ("Mac n' Cheese")
        elif sidesChoice == "3":
            totalCost = totalCost + 20.99
            print("You added 1 Carrot to your order")
            print("Your total cost so far: $", totalCost)
            side = ("1 Carrot")
        else:
            print("please make a valid choice")

    elif menu == "Drinks":
        print("drinks")
        print("1: Maple Syrup $9.99")
        print("2: Vodka $0.01")
        print("3: Chocolate Milk $499.99")
        drinksChoice = input("What would you like (input a number 1-3): ")
        #Add Your code/Comments here for Drinks
        if drinksChoice == "1":
            totalCost = totalCost + 9.99
            print("You added Maple Syrup to your order")
            print("Your total cost so far: S", totalCost)
            drink = ("Maple Syrup")
        elif drinksChoice == "2":
            totalCost = totalCost + 0.01
            print("You added Vodka to your order")
            print("Your total cost so far: S", totalCost)
            drink = ("Vodka")
        elif drinksChoice == "3":
            totalCost = totalCost + 499.99
            print("You added Chocolate Milk to your order")
            print("Your total cost so far: $", totalCost)
            drink = ("Chocolate Milk")
        else:
            print("please make a valid choice")
        
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        print("order finished")
        print("You have ordered")
        print(burger)
        print(side)
        print(drink)
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        print("Grand Total: $", totalCost + totalTax)
        #Finish this section to give you a grand total as well as print your complete order
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")
