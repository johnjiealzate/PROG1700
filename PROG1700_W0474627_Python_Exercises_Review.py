# String: Concatenation: Create two string variables, str1 and str2, and concatenate them into a third variable result_str.
str1 = "John"
str2 = "Alzate"
result_str = str1 + str2

# String: Substring: Given a string sentence, extract and print the first five characters.
print(result_str[0:5])

# String: Formatting: Create a string that includes variables. Use string formatting to insert values into the string.
print (f"{str1} {str2}")

# Loops: Print Numbers: Using a for loop, print the numbers from 1 to 10.
for i in range(1, 11):
    print (i)

# Loops: Factorial: Write a function to calculate the factorial of a number using a while loop.
import math
print(math.factorial(9))

'''
n = 9
result = 9
while result > 0:
    print (n * result)
    result = result - 1
    break
'''

# Sets: Intersection: Create two sets, set1 and set2, and find and print their intersection.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection_set = set1.intersection(set2)
print(intersection_set)

# List: List Operation: Create a list of numbers. Perform the following operations and print the result
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (sum(list1) / len(list1))
print (max(list1))
print (min(list1))

# List comprehention: Generate a list of squares of numbers from 1 to 10 using list comprehension.
squares = []
for x in range (1, 11):
    squares += [x**2]
print (squares)

# Tuples unpacking: Create a tuple with three values. Unpack the tuple into three variables and print them.
tuples1 = ("John", "Bob", "Eve")
(name1, name2, name3) = tuples1
print (name1, name2, name3)

# Disctionaries: DIctionary Operations: Create a dictionary representing a person with keys like 'name', 'age', and 'city'. Print each key-value pair.
person = {
    "name" : "John",
    "Age": 25,
    "City": "Manila"
}
for key, value in person.items():
    print(f"{key}: {value}")

# Nested Dictionary: Create a nested dictionary representing information about students and their grades. Print the average grade for each student.
student_information = {
    "Student_1": {
        "Math": 90,
        "English": 78
    },
    "Student_2": {
        "Math": 88,
        "English": 95
    },
    "Student_3": {
        "Math": 99,
        "Grade": 97
    }
}

for student, grades in student_information.items():
    average_grade = sum (grades.values()) / len(grades)
    print(f"{student}'s average grade: {average_grade}.")

# Functions: Functions Basics: Write a function that takes two arguments and returns their sum.
def my_function(name, surname):
    print(name + surname)
my_function("Johnjie", "Alzate")

# Default Values: Modify the previous function to have default values for the arguments.
def phil_cities (city = "Pasig"):
    print("One of the Philippine cities is " + city)

phil_cities()
phil_cities("Manila")
phil_cities("Taguig")





