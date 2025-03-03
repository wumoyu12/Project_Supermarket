import sys
import os.path
from os import path

def main():
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
