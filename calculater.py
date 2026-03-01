def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def division(a,b):
    if b == 0:
        return "Error : Division by zero"
    return a / b

print("Simple calculator")
print("1 .Add")
print("2.Subtract")
print("3.Multiply")
print("4.Division")

choice = input("Enter your choice (1/2/3/4):")

num1 = float(input("Enter frist number:"))
num2 = float(input("Enter second number:"))

if choice == "1":
    print("result :", add(num1 , num2))
elif choice == "2":
    print("result : ", subtract(num1 , num2))
elif choice == "3":
    print("result : ", multiply(num1 , num2))        
elif choice == "4":
    print("result :", division(num1 , num2))
elif choice > "4":
    print("Invalid choice")    

       