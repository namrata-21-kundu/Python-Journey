def display_tasks(tasks):
    if not tasks:
        print("No Tasks!")
    else:
        for no, task in enumerate(tasks, 1):
            status = "[X]" if task["done"] else "[ ]"
            print(f"{no}. {task['task_name']} - {status}")

def main():
    tasks = []
    while(True):
        print("\n1. Add Tasks\n2. Completed\n3. Delete Tasks\n4. Show Tasks\n5. Quit")
        yourChoice = int(input("Enter your choice: "))
        match yourChoice:
            case 1:
                tsk = input("Enter the task that you want to add")
                tasks.append({       
                    #stored as a dictionary with (task, status) as(key,value)
                    "task_name" : tsk,
                    "done" : False
                })
                print("task added")
            case 2:
                display_tasks(tasks)
                indexNo = int(input("enter the number to be marked as Done")) - 1 
                #enumerate starts from 1, but list is zero indexed
                tasks[indexNo]["done"]= True
            case 3:
                display_tasks(tasks)
                indexNo = int(input("enter the number to be marked as Done")) - 1 
                #enumerate starts from 1, but list is zero indexed
                tasks.pop(indexNo)
            case 4:
                display_tasks(tasks)
            case 5:
                print("--exiting--")
                break
            case _:
                print("Wrong choice")
main()