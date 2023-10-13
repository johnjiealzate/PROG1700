# import modules
import random

# declare global variables
upper_limit = 10
lower_limit = 1
range_number = range(lower_limit, upper_limit)
computer_input = random.choice(range_number)
guess_attempts = 5
invalid_attempts = 10
name = input ("Hello, what's your name?")
print ("Hi", name, ", this is a guessing game. I will guess a number from 1 to 10, and you will attempt to guess my number. You have 5 attempts to guess my number to win")

# program control for guessing game
while guess_attempts > 0:
    """ Main Program """
    user_input = input("What is your guess, 1-10?")
    # validate the input to ensure the program does not return invalid value
    # return true if a digit is entered, otherwise return if false.
    if user_input.isdigit():
        # cast the input to an integer
        user_input = int(user_input)
        #return true if a digit is between 1 to 10
        if user_input <= 10:
            if user_input != computer_input:
                if user_input > computer_input:
                    print ("Your guess is too high.")
                if user_input < computer_input:
                    print ("Your guess is too low.")
            else:
                print ("you're right!")
                guess_attempts = guess_attempts + 1
                print ("You guessed the number in", guess_attempts, "tries.")
                break
        # return false if value is more than 10
        else:
            print("Please enter a valid number.")
            invalid_attempts = invalid_attempts -1
            print ("You have", invalid_attempts, "attempts")
    # return false if value in not a number
    else:
        print("Please enter a valid number.")
        invalid_attempts = invalid_attempts -1
        print ("You have", invalid_attempts, "attempts")
else:
    print ("I'm tired. You repeatedly entered a wong input!")