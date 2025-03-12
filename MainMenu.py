import sys
import os.path
from os import path

def main():
    Askname()

def Askname():
    adminuser=str(input("Are you admin, if yes enter 1, no enter 2"))
    match(adminuser):
        case"1":
            AskEdit()
        case "2":
            AskDepartments()
        case default:
            print("It's an invalid selection, please try again")

def AskUserInfo():
    global filename
    username=str(input("Please Enter Username:"))
    password=str(input("Please Enter Password:"))

    if (useremail == "" or password == ""):
        print("Your username or password is invalid, please enter something")
        AskUserInfo()
    else:
        filename="username.doc"
        

    FileConnectivity()

def FileConnectivity():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    fileexist = bool(path.exists(filename))
    if (fileexist == True):
        CheckName()
    else:
        AskNewUser()

def AskNewUser();
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
    fileDir=os.path.dirname(os.path.realpath("__file__"))
    departments=()
    whichchscreen=str(input("Welcome to Supermarket, choose one of the Departments you are interested in.\n"
                            "1-Fruit\n"
                            "2-Poultry\n"
                            "3-Meat\n"
                            "4-Beverage\n"
                            "5-Frozen Foods\n"
                            "6-Dietary Food (Vegetables, Salad)\n"
                            "7-Kosher\n"
                            "8-Halal"))
    CheckDepartments()

def CheckDepartments():
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
