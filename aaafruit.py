import os
from os import path

# Global variable to store the fruit choice
whichfruit = ""

def main():
    print("Welcome to the Fruit Section!")
    AskFruit()
    
def AskFruit():
    global whichfruit
    print("We have the following fruits:\n"
          "1. Apple: $0.98 for each\n"
          "2. Pear: $0.99 for each\n"
          "3. Orange: $0.96 each\n"
          "4. Pomegranate: $7.50 for each\n"
          "5. Durian Fruit: $25.99 for each\n"
          "Type 0 to go back to Main Menu")
    whichfruit = str(input("Which type of fruit do you want to buy? "))
    CheckFruit()
    
def CheckFruit():
    match whichfruit:
        case "0":
            MainMenu()
        case "1":
            Apple()
        case "2":
            Pear()
        case "3":
            Orange()
        case "4":
            Pomegranate()
        case "5":
            DurianFruit()
        case _:
            print("It's an invalid selection, please try again.")
            AskFruit()  # Re-prompt for fruit choice

def MainMenu():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    filepath = os.path.join(fileDir, "MainMenu.py")  # Ensure path uses os.path.join
    filenamepath = {
        "__file__": filepath,
        "__name__": "__main__",
    }
    try:
        with open(filepath, "rb") as file:
            exec(compile(file.read(), filepath, "exec"), filenamepath)
    except FileNotFoundError:
        print("MainMenu.py not found. Returning to Fruit Section...")
        AskFruit()

def Apple():
    AskNum("Apple", 0.98)

def Pear():
    AskNum("Pear", 0.99)

def Orange():
    AskNum("Orange", 0.96)

def Pomegranate():
    AskNum("Pomegranate", 7.50)

def DurianFruit():
    AskNum("Durian Fruit", 25.99)

def AskNum(fruit_name, price):
    try:
        howmany = int(input(f"How many {fruit_name}(s) would you like to buy? "))
        if howmany < 1:
            print("Please enter a valid number greater than 0.")
            AskNum(fruit_name, price)
        else:
            total_cost = howmany * price
            print(f"Total cost for {howmany} {fruit_name}(s): ${total_cost:.2f}")
            go_back = input("Do you want to buy another fruit? (y/n): ")
            if go_back.lower() == 'y':
                AskFruit()
            else:
                print("Thank you for shopping! Returning to Main Menu.")
                MainMenu()
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        AskNum(fruit_name, price)

if __name__ == "__main__":
    main()
