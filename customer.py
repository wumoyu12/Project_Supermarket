import sys
import os.path
from os import path

def main():
    customer_shopping()

def customer_shopping():
    base_dir = os.path.dirname(os.path.realpath("__file__"))
    
    with open("alldepartments.txt", "r") as f:
        available_depts = []
        for num in f.read().split(","):
            if len(num) > 0:
                available_depts.append(int(num))
    
    department_names = ["Fruit", "Poultry", "Meat", "Beverage", 
                       "Frozenfood", "Dietfood", "Kosher", "Halal"]
    
    while True:
        print("\n=== MAIN MENU ==="
              "\nAvailable Departments:")
        idx = 1
        while idx <= len(available_depts):
            print(f"{idx}. {department_names[available_depts[idx-1]-1]}")
            idx += 1
        
        print("\n9. View Cart"
              "\n0. Logout")
        
        choice = str(input("\nSelect department or option (1-9, 0): "))

        match (choice):
            case "0":
                print("Logging out...")
                execute_script("login.py")
                return
            case "9":
                execute_script("receipt.py")
                return
            case _ if choice.isdigit() and 1 <= int(choice) <= len(available_depts):
                selected_dept = department_names[available_depts[int(choice)-1]-1]
                execute_script(f"{selected_dept.lower()}.py")
                return
            case default:
                print("Invalid selection! Please try again.")

def execute_script(filepath):
    script_path = os.path.dirname(os.path.realpath("__file__"))

    namepath={"__file__":file
              ""
              }
    
    with open(script_path, "rb") as f:
        exec(compile(f.read(), script_path, "exec"), exec_vars)

if __name__ == "__main__":
    main()
