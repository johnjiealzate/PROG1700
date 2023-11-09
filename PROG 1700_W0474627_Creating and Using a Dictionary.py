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
    if student_name in student_score:
        print ("Found")
    # Otherwise  outputs a message "Student name Not Found!"
    else:
        print ("Student name Not Found!")
    


# If they do, print their name and score

# otherwise, print a message indicating that the student is not found.
