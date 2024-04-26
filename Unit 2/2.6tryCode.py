print("Welcome, here you will need to type a number")
while True:
    try:
        john = float(input("Type your number"))
        print("Your number is",john, "continue to use only numbers")
    except:
        print("You used free will and broke the loop")
        break


