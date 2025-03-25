import sys
import os.path
from os import path

def main():
    ChooseDepartment();
    
def ChooseDepartment():
    global whichdepartment,fileDir,existingdepartments
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    
    departmentlist = [];
    departmentFile = open("alldepartments.txt","r+");
    departmentlist = departmentFile.read().split(",");
    
    Departments = ["Fruit","Poultry","Meat","Beverage","Frozen Foods","Dietary Food","Kosher","Halal"]
    existingdepartments = []
    
    length = len(departmentlist)-1;
    for i in range(length):
        num = departmentlist[i]
        dep = Departments[int(num)-1]
        print(str(i+1)+ ". " + dep);
        existingdepartments.append(dep);
        
    whichdepartment = str(input("Type a number to choose a department: "));
    CheckNum(whichdepartment);
    if(ifcorrect != 0):
        print("Invalid input, please try again");
        ChooseDepartment()
    else:
        if(int(whichdepartment) > length):
            print("Invalid input, please try again");
            ChooseDepartment()
        else:
            MatchDepartment();
    
def CheckNum(item):
    global ifcorrect
    ifcorrect = 0;
    checkitem = ord(item)
    if(checkitem >= 49 and checkitem <= 56):
        ifcorrect = ifcorrect + 0;
    else:
        ifcorrect = ifcorrect + 1;
              
def MatchDepartment():
    number = int(whichdepartment)-1
    whichdep = existingdepartments[number];
    filepath = fileDir + "\\" + whichdep + ".py";
    
    filenamepath = {
        "__file__":filepath,
        "__name__":"__main__",
        };
    with open(filepath,"rb")as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);

if __name__ == "__main__":
    main();
