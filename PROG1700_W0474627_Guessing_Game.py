# import modules
import random

# declare global variable
upper_limit = 10
lower_limit = 1
range_number = range(lower_limit, upper_limit)
computer_input = random.choice(range_number)
loop_counter = 0
guess_attempts = 0
invalid_attempts = 10


# program control for guessing game
while guess_attempts < 10:
    """ Main Program """
    user_input = input("What is your guess, 1-10?")
    # validate the input to ensure the program does not return invalid value
    # return true if a digit is entered, otherwise return if false.
    if user_input.isdigit():
        # cast the input to an integer
        user_input = int(user_input)
        # calculate the  computer value
        print(computer_input)
        # print computer value
        if user_input <= 10:
            if user_input != computer_input:
                if user_input > computer_input:
                    print ("Your guess is too high.")
                if user_input < computer_input:
                    print ("Your guess is too low.")
            else:
                guess_attempts += 1
                loop_counter += 1
                print ("You guessed the number in", loop_counter, "tries.")
                break
        else:
            print("Please enter a valid number.")
            invalid_attempts = invalid_attempts -1
            print ("You have", invalid_attempts, "attempts")
    else:
        print("Please enter a valid number.")
        invalid_attempts = invalid_attempts -1
        print ("You have", invalid_attempts, "attempts")
else:
    print ("You are not playing fairly.... Bye!!!")
