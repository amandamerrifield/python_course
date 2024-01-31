import random

magic_number = random.randint(1,10)

#TODO
#1. prompt the user to guess the magic number (use input)
#2. convert the number input by the user to an int (use int())
#3. code an if statement to determine if the user guessed correctly and write an appropriate msg
#4. ideally th euser would get 3 guesses and we would provide more feedback (eg too high/low) if user guesses wrong

inputs = 0
guesses = 3
while inputs <= guesses:
    your_guess = input("Guess the magic number: ")
    your_guess = int(your_guess)
    if your_guess == magic_number:
        print("Great! You guessed the number")
        break
    else:
        if your_guess < magic_number:
            if (guesses - inputs) >= 2:
                print("Your guess was too low. You have", guesses - inputs, " more tries. Try again.")
            elif (guesses - inputs) == 1:
                print("Your guess was too low. This is your last attempt")
            else:
                print("That was your last attempt. Try again later!")
                break
        else:
            if (guesses - inputs) >= 2:
                print("Your guess was too high. You have", guesses - inputs, " more tries")
            elif (guesses - inputs) == 1:
                print("Your guess was too high. This is your last attempt")
            else:
                 print("That was your last attempt. Try again later!")
                 break
    inputs += 1