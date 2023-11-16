"""
Auhor: Johnjie Alzate
Student ID: W0474627
Course: IT Generalist
Programming Language: Python
Date: 11-16-23
Version: 3
"""


# Import random function
import random

# Step 1: Create two separatae lists
programming_languages = ['Python', 'JvaScript', 'C++', 'Ruby', 'Java']
difficulty_levels = [1, 2, 3, 4, 5]

# Step 2: Combine the two list into a list of tuples
quiz_data = list(zip(programming_languages, difficulty_levels))

# Step 3: Shuffle the list for a random quiz order
random.shuffle (quiz_data)

score = 0
for language, difficulty_levels in quiz_data:
    quess = int(input (f"What is the difficuly level of {language}? Enter a number from 1 to 5. : "))
    # Check if the guess is correct
    if quess == difficulty_levels:
        print ("You're correct!")
        score += 1
    else:
        print (f"You're incorrrect! the difficulty level of {language} is {difficulty_levels}.")
print (f"Quiz Complete! Your final score is {score}.")




