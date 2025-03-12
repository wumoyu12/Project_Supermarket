import sys
import os.path
from os import path

def main():
    AskUser()

def AskUser():
    adminuser=str(input("1-Sign in\n2-Sign up"))
    match(adminuser):
        case"1":
            AskUserInfo()
        case "2":
            CreateAccount()
        case default:
            print("It's an invalid selection, please try again")
            Askname()

def CreateAccount():
    username=str(input("please create a  user name:"))
    FileConnectivity()
    if (fileexist=="true")
        print("This username has been used, please create another username")
        CreateAccount()
    else:
        AskPassword()

def AskPassword():
    password=str(input("please create a password:"))
    repassword=str(input("please repeat your password:"))
    if(password == repassword):
        print("Account Create")
    else:
        AskPassword()

def AskUserInfo():
    global filename
    username=str(input("Please Enter Username:"))
    password=str(input("Please Enter Password:"))

    if (useremail == "" or password == ""):
        print("you have incorrect username or password, please try again.")
        AskUserInfo()
    else:
        filename=username + ".doc"
        
    FileConnectivity()

def FileConnectivity():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(filename))
    if (fileexist == True):
        fileex = "true"
    else:
        fileex = "false"

def AskNewUser():
    new=str(input("Are you a new user if yes enter 1, no enter 2"))
    match(new):
        case"1":
            AskEdit()
        case "2":
            AskDepartments()
        case default:
            print("It's an invalid selection, please try again")

def AskDepartments():
    global whichchscreen
    departments=("Welcome to Supermarket, choose one of the Departments you are interested in.\n1-Fruit\n2-Poultry\n3-Meat\n4-Beverage\n5-Frozen Foods\n6-Dietary Food (Vegetables, Salad)\n7-Kosher\n8-Halal")
    whichchscreen=str(input(departments))
    CheckDepartments()

def CheckDepartments():
    fileDir=os.path.dirname(os.path.realpath("__file__"))
    match(whichchscreen):
        case "1":
            filepath=fileDir+"\Fruit.py"
        case "2":
            filepath=fileDir+"\Poultry.py"
        case "3":
            filepath=fileDir+"\Meat.py"
        case "4":
            filepath=fileDir+"\Beverage.py"
        case "5":
            filepath=fileDir+"\FrozenFoods.py"
        case "6":
            filepath=fileDir+"\DietaryFood.py"
        case "7":
            filepath=fileDir+"\Kosher.py"
        case "8":
            filepath=fileDir+"\Halal.py"
        case default:
            print("It's an invalid selection, please try again")
            main()
    filenamepath={
                "__file__":filepath,
                "__name__":"__main__",
                }
    with open(filepath,"rb") as file:
        exec(compile(file.read(), filepath, "exec"), filenamepath)
    main()

if __name__=="__main__":
    main()
