import os.path
from os import path

def main():
    print("Welcome to the Fruit Section!")
    FileConnectivity()
    AskFruit()

def FileConnectivity():
    global filename
    filename = "fruit.doc"
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(filename))
    if (fileexist == True):
        print("1-Continue/n2-Back")
    else:
       pyfile=open(filename, "w")
       pyfile.write("Fruit Section\n")
       pyfile.close()

def AskFruit():
    global whichfruit
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
    AddToFile(fruit)
    
def Pear():
    fruit = "Pear"
    price = 0.99
    AskNum(fruit, price)
    AddToFile(fruit)
    
def Orange():
    fruit = "Orange"
    price = 0.96
    AskNum(fruit, price)
    AddToFile(fruit)
    
def Pomegranate():
    fruit = "Pomegranate"
    price = 7.50
    AskNum(fruit, price)
    AddToFile(fruit)
    
def DurianFruit():
    fruit = "DurianFruit"
    price = 25.99
    AskNum(fruit, price)
    AddToFile(fruit)

def AskNum(fruit, price):
    global howmany, fruitprice
    howmany=str(input("How many " + fruit + " you want to buy"))
    CheckNum(howmany)
    fruitprice = int(howmany) * price
    fruitprice = str(fruitprice)
    
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

def AddToFile():
    pyfile=open(filename, "a")
    item = (fruit + "-" + howmany + "   " + fruitprice + "\n")
    pyfile.write(item)
    pyfile.close()

    AskFruit()

def Display():
    pyfile=open(filename, "r")
    print(pyfile.readline())
    pyfile.close()
    

if __name__ == "__main__":
    main()
