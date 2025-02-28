import os.path
from os import path

def AskNum():
    global howmany, count
    print("1.Apple:$0.98 for each\n2.Pear: 0.99 for each\n3.Orange: $0.96 each \n4.Pomegranate: $7.50 for each\n5.Durian Fruit: $25.99 for each")
    howmany=str(input("How many type of fruits do you want to buy?"))
    CheckNum()
    count = int(howmany)
    Askfruits()
def CheckNum():
    numlen = len(howmany)
    if numlen != 1:
        print("Enter a valid number!")
        AskNum()
    else:
        numlist = list(howmany)
        for i in range(0,len(numlist)):
            newnum = ord(numlist[i])
            if (newnum < 49 or newnum > 53):
                print("Enter a valid number!")
                AskNum()
def Askfruits():
    global fruits, count
    while count != 0:
        fruits = str(input("What type of fruits do you want to buy?(Please enter the number representing the fruit you want to buy)"))
        Checkfruits()
        count - 1

def Checkfruits():
    fruitlen = len(fruits)
    if fruitlen != 1:
        print("Enter a valid number!")
        Askfruits()
    else:
        fruitlist = list(fruits)
        for i in range(0,len(fruitlist)):
            newfruit = ord(fruitlist[i])
            if (newfruit < 49 or newfruit > 53):
                print("Enter a valid number!")
                Askfruits()


def main():
    print("Welcome to the grocery store! We have the following fruits:")
    AskNum()

if __name__ == "__main__":
    main()
