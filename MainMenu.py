import sys
import os
from os import path

def main():
    AskUser()

def AskUser():
    global filename, username, password
    adminuser = input("1-Sign in\n2-Sign up\n")
    match(adminuser):
        case "1":
            AskUserInfo()
        case "2":
            CreateAccount()
        case default:
            print("It's an invalid selection, please try again.")
            AskUser()

def CreateAccount():
    username = input("Please create a username: ")
    filename = username + ".doc"
    FileConnectivity(filename)
    if fileexist == "true":
        print("This username has been used, please create a new one.")
        CreateAccount()
    else:
        AskPassword()

def AskPassword():
    password = input("Please create a password: ")
    lenpassword = len(password)
    
    repassword = input("Please repeat your password: ")
    if password == repassword:
        pyfile = open(filename, "w")
        pyfile.write(username + "," + password)
        pyfile.close()
    else:
        print("Passwords do not match. Please try again.")
        AskPassword()

def AskUserInfo():
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    if (lenpassword <= 4):
        print("At least 4 digit, please try again")
        AskUserInfo()
    else:  
        filename = username + ".doc"
        FileConnectivity(filename)
        lenpassword = len(password)
        
        if username == "" or lenpassword <= 4 or fileexist=="false":
            print("You have entered incorrect username or password(At least 4 digit), please try again.")
            AskUserInfo()
        else:
            #Go to Menu
            print("Both are correct")       

def FileConnectivity(filename):
    global fileexist
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    if path.exists(filename):
        fileexist = "true"
    else:
        fileexist = "false"

def AskDepartments():
    global whichchscreen
    departments = ("Welcome to Supermarket, choose one of the Departments you are interested in.\n"
                   "1-Fruit\n2-Poultry\n3-Meat\n4-Beverage\n5-Frozen Foods\n6-Dietary Food (Vegetables, Salad)\n7-Kosher\n8-Halal\n")
    whichchscreen = input(departments)
    CheckDepartments()

def CheckDepartments():
    global whichchscreen
    fileDir = os.path.dirname(os.path.realpath("__file__"))

    match(whichchscreen):
        case "1":
            filepath = os.path.join(fileDir, "Fruit.py")
        case "2":
            filepath = os.path.join(fileDir, "Poultry.py")
        case "3":
            filepath = os.path.join(fileDir, "Meat.py")
        case "4":
            filepath = os.path.join(fileDir, "Beverage.py")
        case "5":
            filepath = os.path.join(fileDir, "FrozenFoods.py")
        case "6":
            filepath = os.path.join(fileDir, "DietaryFood.py")
        case "7":
            filepath = os.path.join(fileDir, "Kosher.py")
        case "8":
            filepath = os.path.join(fileDir, "Halal.py")
        case default:
            print("It's an invalid selection, please try again.")
            main()
                
    ExecuteDepartmentFile(filepath)

def ExecuteDepartmentFile(filepath):
    if os.path.exists(filepath):
        filenamepath = {
            "__file__": filepath,
            "__name__": "__main__",
            }
        with open(filepath, "rb") as file:
            exec(compile(file.read(), filepath, "exec"), filenamepath)
        main()
    else:
        print(f"The department file at {filepath} does not exist.")
        main()

if __name__ == "__main__":
    main()
