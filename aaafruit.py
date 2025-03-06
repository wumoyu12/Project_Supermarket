import os.path
from os import path

def main():
    print("Welcome to the Fruit Section!")
    AskFruit()
    
def AskFruit():
    global whichfruit
    allfruit = []
    fruitnum = []
    fruitprice = []
    menu="We have the following fruits:\n1.Apple:$0.98 for each\n2.Pear: 0.99 for each\n3.Orange: $0.96 each\n4.Pomegranate: $7.50 for each\n5.Durian Fruit: $25.99 for each\nType 01 to check what did you bought in Fruit Section\nType 0 to go back to Main Menu"
    print(menu)
    whichfruit=str(input("Which type fruit you want to buy?"))
    CheckFruit()
    
def CheckFruit():
    match(whichfruit):
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
            print("It's an invalid selection, please try again")
            AskFruit()

def MainMenu():
    fileDir=os.path.dirname(os.path.realpath("__file__"))
    filepath=fileDir+"\MainMenu.py"
    filenamepath={
                "__file__":filepath,
                "__name__":"__main__",
                }
    with open(filepath,"rb") as file:
        exec(compile(file.read(), filepath, "exec"), filenamepath)

def Apple():
    fruit = "Apple"
    price = 0.98
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)
    
def Pear():
    fruit = "Pear"
    price = 0.99
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)
    
def Orange():
    fruit = "Orange"
    price = 0.96
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)
    
def Pomegranate():
    fruit = "Pomegranate"
    price = 7.50
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)
    
def DurianFruit():
    fruit = "DurianFruit"
    price = 25.99
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)

def AskNum(fruit):
    global howmany, price
    howmany=str(input("How many " + fruit + " you want to buy? "))
    CheckNum(howmany)
    howmany = int(howmany)
    price = howmany * price

def CheckNum(num):
    length=len(num)
    if (length == 0 or num == "0"):
        print("It's invalid input, please try again")
        AskNum(fruit)
    else:
        numlist=list(num)
        for i in range(0,len(numlist)):
            newnum=ord(numlist[i])
            if(newnum < 49 or newnum >58):
                print("invalid")
                AskNum(fruit)
            else:
                return(num)

if __name__ == "__main__":
    main()
