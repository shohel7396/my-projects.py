import random

secret_number = random.randint(1,100)
attempts = 0

print("Welcome to number guessing game!")
print("Guess number between 1 to 100")

while True:
    guess = int(input("Enter your guess : "))
    attempts += 1

    if guess > secret_number:
        print("Its higher")
    elif guess < secret_number:
        print("Its lower")    
    else:
        print("CORRECT!!")    
        print("You won!!!")
        print("attempts =",attempts)
        break