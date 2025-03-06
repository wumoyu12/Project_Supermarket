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
    menu="We have the following fruits:\n1.Apple:$0.98 for each\n2.Pear: 0.99 for each\n3.Orange: $0.96 each\n4.Pomegranate: $7.50 for each\n5.Durian Fruit: $25.99 for each\nType 01 to check what did you bought in Fruit Section\nTypy 0 to go back to Main Menu"
    print(menu)
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
    fruit = "Apple"
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)
    
def Pear():
    fruit = "Pear"
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)
    
def Orange():
    fruit = "Orange"
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)
    
def Pomegranate():
    fruit = "Pomegranate"
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)
    
def DurianFruit():
    fruit = "DurianFruit"
    AskNum(fruit)
    allfruit.append(fruit)
    fruitnum.append(howmany)
    fruitprice.append(price)


def AskNum(fruit):
    global howmany, price
    howmany=str(input("How many " + fruit + "you want to buy"))
    CheckNum(howmany)
    howmany = int(howmany)
    price = howmany * price

    
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

if __name__ == "__main__":
    main()
