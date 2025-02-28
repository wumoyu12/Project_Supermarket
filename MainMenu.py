import sys
import os.path
from os import path

def main():
    fileDir=os.path.dirname(os.path.realpath("__file__"))
    whichchscreen=str(input("Which screen will you open? Type 1 or 2:"))

    match(whichchscreen):
        case "1":
            filepath=fileDir+"\Fruit.py"
        case default:
            print("Houston...we have a problem")
            sys.exit()
    filenamepath={
                "__file__":filepath,
                "__name__":"__main__",
                }
    with open(filepath,"rb") as file:
        exec(compile(file.read(), filepath, "exec"), filenamepath)
    main();

if __name__=="__main__":
    main()
