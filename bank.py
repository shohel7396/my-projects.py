import random
import string

characters = string.ascii_letters.upper() + string.digits
filename = "Bank.txt"

def gen_accid():
    account_id = ""
    for i in range(12):
        account_id += random.choice(characters)
    return account_id

def load_accounts():
    try:
        with open(filename, "r") as f:
            return[line.strip().split(",") for line in f]
    except FileNotFoundError:
        return[]
    
def save_accounts(accounts):
    with open(filename,"w") as f:
        for account in accounts:
            f.write(",".join(map(str,account)) + "\n")
            
def create_account(accounts):
    name = input("Enter name for account : ")
    balance = float(input("Enter intial balance : "))
    account_id = gen_accid()
    accounts.append([name,account_id,balance])
    save_accounts(accounts)
    print("Account created succesfully!")
    print(f"name : {name}, Account_id : {account_id}, Balance : {balance}")

def check_balance(accounts):
    name = input("Enter name of account : ")
    for account in accounts:
        if name.lower() == account[0].lower():
            print(f"Name : {account[0]}, Account_id : {account[1]}, Balance : {account[2]}")
            return
    print("Account not found!")

def deposit_amount(accounts):
    name = input("Enter name of account : ")
    for account in accounts:
        if name.lower() == account[0].lower():
            print(f"current balance is : {account[2]}")
            amount = float(input("Enter amount to deposit : "))
            account[2] = str(float(account[2]) + amount)
            save_accounts(accounts)
            print("Deposited succesfully!")
            print(f"Updated balance is : {account[2]}")
            return
    print("\nNo account match this name!")    

def withdraw_amount(accounts):
    found = False
    name = input("Enter name of account : ")
    for account in accounts:
        if name.lower() == account[0].lower():
            found = True
            amount = float(input("Enter amount to withdraw : "))
            if amount > float(account[2]):
                print("Amount exceeds current balance!")
            else:
                account[2] = str(float(account[2]) - amount)
                print(f"Withdraw succesfull : {amount}")
                print(f"Remaining balnace : {account[2]}")
                break
    if not found:
        print("\nNo account match this name!")

def delete_account(accounts):
    name = input("Enter name to delete : ")
    for account in accounts:
        if name.lower() == account[0].lower():
            print(f"Name : {account[0]}, Account_id : {account[1]}, Balance : {account[2]}")
            confirm = input("Type 'yes' to confrim : ")
            if confirm == "yes":
                accounts.remove(account)
                save_accounts(accounts)
                print("Account deleted successfully!")
            else:
                print("Request Declined!")
                return
    print("No name match this account")

accounts = load_accounts()    

while True:
    print("\nWelcome to HUHUVA BANK")
    print("\n1.Create account. \n2.Check balance. \n3.Deposit amount. \n4.Withdraw amount. \n5.Delete account. \n6.Exit")
    choice = input("Plz enter your choice : ")

    if choice == "1":
        create_account(accounts)
    elif choice == "2":
        check_balance(accounts)
    elif choice == "3":
        deposit_amount(accounts)
    elif choice == "4":
        withdraw_amount(accounts)
    elif choice == "5":
        delete_account(accounts)
    elif choice == "6":
        print("Thank you..\n Visit again!")
        break
    else:
        print("Inavlid choice!")