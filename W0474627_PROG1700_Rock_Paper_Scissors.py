# import modules
import random

# declare global variable
rock = 1
paper = 2
scissors = 3
invalid_attempts = 3

# program control for rock paper scissors
while invalid_attempts > 0:
    """ Main Program """
    user_input = input("Press 1 for rock, 2 for paper or 3 for scissors:")
    # validate the input to ensure the program does not return invalid value
    # return true if a digit is entered, otherwise return if false.
    if user_input.isdigit():
        if len (user_input) == 1:
            # cast the input to an integer
            user_input = int(user_input)
            # calculate the  computer value
            computer_input = random.randrange(1, 4, 1)
            # print computer value
            if user_input <= 3:
                if user_input == 1:
                    print ("User: rock vs")
                if user_input == 2:
                    print("User: paper vs")
                if user_input ==3:
                    print("User: scisssor vs")
                if computer_input == 1:
                    print("Computer: rock")
                if computer_input == 2:
                    print("Computer: paper")
                if computer_input == 3:
                    print("Computer: scissor")           
                if user_input != computer_input:
                    # Computer wins
                    if (user_input == 1 and computer_input == 2) or (user_input == 2 and computer_input == 3) or (user_input == 3 and computer_input == 1):
                        print ("Computer wins")
                    # User wins
                    else:
                        print("User Wins")            
                else:
                    print("Tie game")
            else:
                print ("Wrong input. Please press 1 for rock, 2 for paper or 3 for scissors:")
                invalid_attempts = invalid_attempts -1
                print ("You have", invalid_attempts, "attempts")
        else:
            print ("Enter a single digit")
            invalid_attempts = invalid_attempts -1
            print ("You have", invalid_attempts, "attempts")
    else:
        print("Please enter a valid number.")
        invalid_attempts = invalid_attempts -1
        print ("You have", invalid_attempts, "attempts")
else:
    print ("You are not playing fairly.... Bye!!!")

