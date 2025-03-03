import os.path
from os import path

def main():
    print("Welcome to the Fruit Section!")
    AskFruit()
    
def AskFruit():
    global whichfruit
    print("We have the following fruits:\n"
          "1.Apple:$0.98 for each\n"
          "2.Pear: 0.99 for each\n"
          "3.Orange: $0.96 each\n"
          "4.Pomegranate: $7.50 for each\n"
          "5.Durian Fruit: $25.99 for each\n"
          "Typy 0 to go back to Main Menu")
    whichfruit=str(input("Which type fruit you want to buy?"))
    CheckFruit()
    
def CheckFruit():
    match(whichfruit):
        case "0":
            MainMunu()
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
        case default:
            print("It's an invalid selection, please try again")
def MainMunu():
    fileDir=os.path.dirname(os.path.realpath("__file__"))
    filepath=fileDir+"\MainMenu.py"
    filenamepath={
                "__file__":filepath,
                "__name__":"__main__",
                }
    with open(filepath,"rb") as file:
        exec(compile(file.read(), filepath, "exec"), filenamepath)

def Apple():
    AskNum()

def Pear():
    AskNum()

def Orange():
    AskNum()
    
def Pomegranate():
    AskNum()
    
def DurianFruit():
    AskNum()

def AskNum(fruits):
    howmany=str(input("How many fruits you want to buy"))

if __name__ == "__main__":
    main()
