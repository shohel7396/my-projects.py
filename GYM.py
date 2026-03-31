filename = "gym-list.txt"

def load_names():
    try:
        with open(filename, "r") as f:
            return[line.strip().split(",") for line in f]
    except FileNotFoundError:
        return[]

def save_names(names):
    with open(filename,"w") as f:
        for name in names:
            f.write(",".join(map(str,name)) + "\n")


def create_name(names):
    subscirption_plans = ""
    name = input("Enter your name ❤️ :")
    age = int(input("enter your age 🪫 : "))
    if age >= 18:
        print("Select your subscription plan :  \n 1.monthly : 2500 \n 2. yearly : 10000")
        choice = input("Enter your choice (1/2) : ")
        if choice == "1":
            subscirption_plans = "monthly"
            print("You have selected monthly subscription plan✈️. Your subscription will be renewed every month.")
        elif choice == "2":
            subscirption_plans = "yearly"
            print("You have selected yearly subscription plan🚀. Your subscription will be renewed every year.")    
        names.append([name,age,subscirption_plans])
        save_names(names)
        print(f"name : {name}, age : {age}, subscription plan : {subscirption_plans}")
        print("Your name is added!\n Start from tommorow😊")
    else:
        print("Sorry😢, you must be at least 18 years old to join the gym.")    

def check_names(names):
    search_name = input("Enter your name to check : ")
    for name in names:
        if search_name.lower() == name[0].lower():
            print(f"name : {name[0]}, age : {name[1]}, subscription plan : {name[2]}")
            return
    print("Name not found!")


def view_names(names):
    if not names:
        print("List is empty!😒")
    else:
        for name in names:
            print(f"name : {name[0]}, age : {name[1]}, subscription plan : {name[2]}")

def delete_name(names):
    search_name = input("Enter name to delete : ")            
    for name in names:
        if search_name.lower() == name[0].lower():
            select = int(input("How many days it has since u join the gym? :"))
            if select > 5:
                print("WARNING!! \n Your money wil not be refunded \n Do you want to proceed?")
                choice = input("Enter (yes/no) : ")
                if choice.lower() == "yes":
                    names.remove(name)
                    save_names(names)
                    print("Name deleted successfully!😎")
                elif choice.lower() == "no":
                    print("Deletion cancelled!😌")    
                    break
            else:
                names.remove(name)        
                save_names(names)
                print("Name deleted successfully!😎")
    print("Name not found!")


names = load_names()

while True:
    print("\nWelcome to the gym management system!💪")
    print("1. Create name")
    print("2. Check name")
    print("3. View names")
    print("4. Delete name")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5) : ")

    if choice == "1":
        create_name(names)
    elif choice == "2":
        check_names(names)
    elif choice == "3":
        view_names(names)
    elif choice == "4":
        delete_name(names)
    elif choice == "5":
        print("Thank you for using the gym management system!👋")
        break
    else:
        print("Invalid choice! Please try again.")
            