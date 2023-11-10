# Create a empty dictionary called 'student_scores'
student_scores = {}

# Add student names and their test scores in the dictionary
student_scores ['Alice'] = 90
student_scores ['Bob'] = 85
student_scores ['Charlie'] = 78
student_scores ['David'] = 92
student_scores ['Eve'] = 88

# Output/print the initial 'student_score' dictionary to display the student names and their scores
for key, value in student_scores.items():
    print(f'{key}: {value}')
print('\n')

# Calculate and print the average test score of all the students in the 'student_scores' dictionary
average = sum (student_scores.values())/len(student_scores)
print("The average test score of all the students is", average)

# Prompt the user to input a student's name
student_name = input ("Enter the student's first name: ")

# Check if the student exists in the dictionary
# Output if student name is not in the dictionary
if student_name not in student_scores:
    print ("Your name is not found in the file system!")
    # Modify the dictionary and add the score of the name that is not in the file system
    score = input ("What's your test score? ")
    # Update the dictionary accordingly and print the updated 'student_scores'
    student_scores [student_name] = score
    for key, value in student_scores.items():
        print(f'{key}: {value}')
    print('\n')
    print ("You've been successfully added in the file system!")
# Otherwise outputs a message "Your name is found in the file system!"
else:
    print("Your name is found in the file system!")
    # Output/print the student name and the score that is found in the dictionary
    print("Your test score is", student_scores.get(student_name))
    print('\n')
    # Prompt the student to update test score
    update_score = input ("Enter your updated test score: ")
    # Cast the updated score
    update_score = int(update_score)
    student_scores [student_name] = update_score
    # Output/print the updated 'student scores' dictionary
    for key, value in student_scores.items():
        print(f'{key}: {value}')
    print('\n')
    # Print message stating that test score has been updated
    print ("Your test score has been updated.")
    # Remove one student form the 'student scores' dictionary
    # Prompt the user to input the student name to be removed.
    remove_name = input ("Enter the name of the student to be removed from the file system: ")
    del student_scores [remove_name]
    # Output/print the updated 'student scores' dictionary
    for key, value in student_scores.items():
        print(f'{key}: {value}')
    print('\n')
    # Print message stating that student name has been removed from the dictionary
    print (remove_name, "has been deleted from the file system!")
    for key, value in student_scores.items():
        print(f'{key}: {value}')
    # Get the student name with the highest score
    name_highest_score = max (student_scores, key=student_scores.get)     
    highest_score = max (student_scores.values())
    print('\n')
    # Output/print the highest score and the student name who achieved it
    print (name_highest_score, "has the highest score", "of", highest_score)

