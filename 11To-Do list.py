# TO - DO list

to_dolist=[]

def show():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Exit")

def add_task():
    task=input("Enter the task you want to add: ")
    to_dolist.append(task)
    print(f"Task '{task}' is added in the list")

def view_task(to_dolist):
    if len(to_dolist) == 0:
        print("Your to-do list is empty!")
    else:
        print("\n Your to-do list : ")
        for i,to_dolist in enumerate(to_dolist,start=1):
            print(f"{i}. {to_dolist}")
    
def remove_task():
    if len(to_dolist) == 0:
        print("Your to-do list is empty!")
        return
    
    view_task(to_dolist)
    task_num=int(input("Enter the number which you want to remove the task: "))
    if(1 <= task_num <= len(to_dolist)):
        removed_task = to_dolist.pop(task_num-1)
        print(f" Task '{removed_task}' has been removed")
    else:
        print("Invalid number")

def exit():
    print("GOODBYE !")

def main_():
    while True:
        show()
        choice= input("Enter your choice (1-4): ")

        match choice:
            case "1":
                add_task()
            case "2":
                view_task(to_dolist)
            case "3":
                remove_task()
            case "4":
                exit()
                break
            case _:
                print("Invalid choice.Please try again ")

main_()



