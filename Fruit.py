import os.path
from os import path

def main():
    print("Welcome to the Fruit Section!")
    AskFruit()
    
def AskFruit():
    global whichfruit, allfruit, fruitnum, fruitprice
    allfruit = []
    fruitnum = []
    fruitprice = []
    menu="We have the following fruits:\n1.Apple:$0.98 for each\n2.Pear: 0.99 for each\n3.Orange: $0.96 each\n4.Pomegranate: $7.50 for each\n5.Durian Fruit: $25.99 for each\nType 01 to check what did you bought in Fruit Section\nTypy 0 to go back to Main Menu"
    print(menu)
    whichfruit=str(input("Which type fruit you want to buy?"))
    CheckOption()
    
def CheckOption():
    match(whichfruit):
        case "0":
            MainMunu()
        case "01":
            CheckFruit()
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
            AskFruit()
            
def MainMunu():
    fileDir=os.path.dirname(os.path.realpath("__file__"))
    filepath=fileDir+"\MainMenu.py"
    filenamepath={
                "__file__":filepath,
                "__name__":"__main__",
                }
    with open(filepath,"rb") as file:
        exec(compile(file.read(), filepath, "exec"), filenamepath)

def CheckFruit():
    if len(allfruit) == 0:
        print("You didn't bought anything")
    else:
        DisplayInfo()

def Apple():
    fruit = "Apple"
    price = 0.98
    AskNum(fruit, price)
    
def Pear():
    fruit = "Pear"
    price = 0.99
    AskNum(fruit, price)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(fruitprice)
    
def Orange():
    fruit = "Orange"
    price = 0.96
    AskNum(fruit, price)
    
def Pomegranate():
    fruit = "Pomegranate"
    price = 7.50
    AskNum(fruit, price)
    
def DurianFruit():
    fruit = "DurianFruit"
    price = 25.99
    AskNum(fruit, price)

def AskNum(fruit, price):
    global howmany, fruitprice
    howmany=str(input("How many " + fruit + "you want to buy"))
    CheckNum(howmany)
    fruitprice = int(howmany) * price
    fruitprice = str(fruitprice)
    
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(fruitprice)

    
def CheckNum(num):
    length=len(num)
    if (length == 0 or num == "0"):
        print("It's invalid input, please try again")
        AskNum()
    else:
        numlist=list(num)
        for i in range(0,len(numlist)):
            newnum=ord(numlist[i])
            if(newnum < 49 or newnum >58):
                print("invalid")
                AskNum()
            else:
                return(num)

def DisplayInfo():
    totalprice = 0
    totalnum = len(allfruit)
    for i in range(0, totalnum):
        totalprice=fruitprice[i]

if __name__ == "__main__":
    main()
