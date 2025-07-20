import random

secret_number = random.randint(1, 95)
secret_number = 45

print("My secret number lies between 1 and 95 ")
#prompt the user to guess a number
guess = int(input("Please make guess:"))
#Check if guess is not as secret_number
while guess != secret_number:
    #while guess is less tha secret_number
    if guess < secret_number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    print("")# prints an empty line and begins the guessing again
    guess = int(input("Try again: "))
print(f"Congratulations! {secret_number} is your secret_number. ")