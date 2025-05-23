import random

def guess_number():
    while True:
        number = random.randint(1, 100)
        while True:
            guess = int(input("Guess a number between 1 and 100: "))
            if guess == number:
                print("You guessed the number!")
                break
            elif guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Invalid input! Please enter a valid number.")
        
        again = input("Do you want to play again? (Y/N)")
        if again == "Y":
            continue
        elif again == "N":
            break
        else:
            print("Invalid input! Please enter Y or N.")
            continue
        
guess_number()