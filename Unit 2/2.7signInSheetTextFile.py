John = "signinsheetfile.txt"

def writeToFile(content):
    try:
        with open(John, 'a') as file:
            content = content+"\n"
            file.write(content)
            print("Name added")
            file.close()
    except:
        print("An error has occured")
def readFromFile():
    try:
        with open(John, 'r') as file:
            content = file.read()
            print(content)
            file.close()
    except:
        print("An error has occured!")
    
while True:
    print("Welcome to the sign up sheet")
    choice = input("If your adding your name type y \nIf you want to see the list type n")
    if choice == "y":
        content = input("Type your name  ")
        writeToFile(content)
    if choice == "n":
        print("The list so far is:")
        readFromFile()
