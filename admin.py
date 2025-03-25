import sys
import os.path
from os import path

def main():
    ChooseDepartment();
    
def ChooseDepartment():
    global whichdepartment,fileDir,AllDepartmentsFile,whichdepartment
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    
    AllDepartmentsFile = "alldepartments.txt";
    CreateFile(AllDepartmentsFile);
    
    Departments = ["1. Fruit","2. Poultry","3. Meat","4. Beverage","5. Frozen Foods","6. Dietary Food","7. Kosher","8. Halal"]
    for i in range(len(Departments)):
        print(Departments[i]);
    whichdepartment = str(input("Type a number from 1 - 8 to choose a department and enter information for the department: "));
    MatchDepartment();

def CreateFile(thefilename):
    global fileexist;
    fileexist = bool(path.exists(thefilename));
    if(fileexist == False):
        adminfile = open(thefilename,"x");
        adminfile.close();
    
def MatchDepartment():
    global whichfilename;
    match(whichdepartment):
        case "1":
            whichfilename = "Fruit.txt";
        case "2":
            whichfilename = "Poultry.txt";
        case "3":
            whichfilename = "Meat.txt";
        case "4":
            whichfilename = "Beverage.txt";
        case "5":
            whichfilename = "Frozen Foods.txt";
        case "6":
            whichfilename = "Dietary Food.txt";
        case "7":
            whichfilename = "Kosher.txt";
        case "8":
            whichfilename = "Halal.txt";
        case default:
            print("Invalid, please enter a number from 1 - 8.");
            ChooseDepartment();
    
    CheckFileExist();

def AddInfo(filename,info):
    adminfile = open(filename,"a");
    adminfile.write(info + ",")
    adminfile.close();
        
def CheckFileExist():
    global pricefilename
    CreateFile(whichfilename);
    pricefilename = "Price "+ whichfilename;
    CreateFile(pricefilename);
    
    if(fileexist == False):
        AddInfo(AllDepartmentsFile,whichdepartment)
        
    CollectInfo();
    
def CollectInfo():
    global count
    count = str(input("How many products would you like to add?"));
    CheckNum(count);
    if(ifcorrect != 0):
        print("Invalid input, please try again");
        CollectInfo();
    else:
        CollectProductInfo();

def CheckNum(item):
    global ifcorrect
    ifcorrect = 0;
    numberlist = list(item)
    length = len(numberlist);
    if(length == 0 or item == "0"):
        ifcorrect = ifcorrect + 1;
    else:
        for i in range(length):
            checkitem = ord(numberlist[i])
            if(checkitem >= 48 and checkitem <= 57):
                ifcorrect = ifcorrect + 0;
            else:
                ifcorrect = ifcorrect + 1;

def CollectProductInfo():
    for i in range (0,int(count)):
        ProductName();
        ProductPrice();
    NextStep();

def ProductName():
    global Name;
    Name = str(input("Enter the product name: "));
    CheckProduct(Name);
    if(truefalse == "false"):
        print("Invalid input, please try again");
        ProductName();
    else:
        AddInfo(whichfilename,Name);

def CheckProduct(item):
    global truefalse;
    if(item == ""):
        truefalse = "false";
    else:
        truefalse = "true";

def ProductPrice():
    global Price;
    Price = str(input("Enter the product price: "));
    CheckPrice(Price);
    if(iscorrect != 0 or decimalnum > 1):
        print("Invalid input, please try again");
        ProductPrice();
    else:
        AddInfo(pricefilename,Price);

def CheckPrice(item):
    global iscorrect, decimalnum
    iscorrect = 0;
    decimalnum = 0;
    numberlist = list(item)
    length = len(numberlist);
    if(length == 0 or item == "0"):
        iscorrect = iscorrect + 1;
    else:
        for i in range(length):
            checkitem = ord(numberlist[i])
            if(checkitem >= 48 and checkitem <= 57):
                iscorrect = iscorrect + 0;
            else:
                if(checkitem == 46):
                    decimalnum = decimalnum + 1;
                else:
                    iscorrect = iscorrect + 1;

def NextStep():
    choice = str(input("Choose from:" + 
                       "\n1. Choose another department" +
                       "\n2. Log out" +
                       "\n3. End the program"+
                       "\nenter a number from 1 - 3:"));

    match(choice):
        case "1":
            ChooseDepartment();
            
        case "2":
            print("You successfully log out!");
            filepath = fileDir + "\\Login.py";
            filenamepath = {
                "__file__":filepath,
                "__name__":"__main__",
                };
            with open(filepath,"rb")as file:
                exec(compile(file.read(),filepath,"exec"),filenamepath);
            
        case "3":
            print("Thank you, goodbye!");
            sys.exit();
            
        case default:
            print("Invalid, please enter a number from 1 - 3.");
            NextStep();

if __name__ == "__main__":
    main();
