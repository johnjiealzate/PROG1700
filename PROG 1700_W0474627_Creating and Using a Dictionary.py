# Prompt the user to input a student's name
student_name = input ("Enter the student's first name: ")


# Create a dictionary called `student_scores
student_score = {
    'Alice': '90',
    'Bob': '85',
    'Charlie' : '78',
    'David' : '92',
    'Eve': "88"
}

# Output the 'student_score' dictionary to display the student names and their scores.
for key, value in student_score.items():
    print(f'{key}: {value}')
print('\n')

# Calculate and print the average test score of all the students in the 'student_scores' dictionary.

# Check if the student exists in the dictionary
# Student name is in the list, print name ans score
while True:
    if student_name not in student_score:
        print ("Your name is not in the file system!")
        score = input ("What's your score? ")
        student_score [student_name] = score
        for key, value in student_score.items():
            print(f'{key}: {value}')
        print('\n')
        break
    # Otherwise outputs a message "Student name Not Found!"
    else:
        print ("Your name is found in the file system!")
        for key, value in student_score.items():
            print(f'{key}: {value}')
        print('\n')
        print ("You've been successfully added in the file system! ")
        break
