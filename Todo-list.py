filename = "TODO.txt"

def load_tasks():
    try:
        with open(filename,"r") as f:
            tasks = f.readlines()
            return[task.strip() for task in tasks]
    except FileNotFoundError:
        return[]
    
def save_task(tasks):
    with open(filename,"w") as f:
        for task in tasks:
            f.write(task + "/n")

def show_tasks(tasks):
    if not tasks:
        print("List is empty!")
    else:
        for index, task in enumerate(tasks, start = 1):
            print(f"{index} : {task}")

tasks = load_tasks()            

while True:

    print("______TO DO LIST______")
    print("1.Add list")
    print("2.View tasks")
    print("3.delete task")
    print("4.Exit")

    choice = input("Enter your choice : ")

    if choice == "1":
        new_task = input("Enter task  : ")
        tasks.append(new_task)
        save_task(tasks)
        print("Task added!")

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        show_tasks(tasks)
        task_no = int(input("Enter task number : "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print("Task deleted succesfully!")

    elif choice == "4":
        print("Good bye!!")
        break

    else:
        print("Invalid choice!")