# import modules
import random

# declare global variables
upper_limit = 10
lower_limit = 1
range_number = range(lower_limit, upper_limit)
computer_input = random.choice(range_number)
guess_attempts = 1
invalid_input_attempts = 5
tries_remaining = 5

# start of the game
name = input ("Hello, what's your name?")
print ("Hi", name, ", this is a guessing game. You will guess a number from 1 to 10, and you will attempt to guess my number. You have 5 attempts to guess my number to win.")

# program control for guessing game
while invalid_input_attempts > 0:
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
                guess_attempts = guess_attempts +1
                tries_remaining = tries_remaining -1
                # return true if with valid number of tries
                while tries_remaining != 0:
                    print ("You have", tries_remaining, "tries left.")
                    break
                # return false if no more tries left
                else:
                    print ("Sorry, try your luck next time.")
                    break
            #return false if the player guessed the correct number             
            else:
                print ("Congratulations! You're right! My number is", computer_input)
                print ("You guessed it in", guess_attempts, "tries.")
                break             
        # return false if value is more than 10
        else:
            print("Please enter a valid number.")
            invalid_input_attempts = invalid_input_attempts -1
            print ("You have", invalid_input_attempts, "attempts")
    # return false if value in not a number
    else:
        print("Please enter a valid number.")
        invalid_input_attempts = invalid_input_attempts -1
        print ("You have", invalid_input_attempts, "attempts left.")
#return false if the player repeatedly entered wrong input type
else:
    print ("I'm tired. You repeatedly entered a wrong input!")
