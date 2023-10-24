# Determinate loops

#1 loops that counts from 0 to 9
print ("Loop that counts from 0 up to 9")
for x in range(9):
    print (x)

#2 loop that counts from 1, up to and including 100
print ("Loop that counts from 1, up to and including 100")
for x in range (1, 101):
    print (x)

#3 loop that counts from 10, up to 50, stepping by valuaes of 5 each iterations
print ("Loop that counts from 10, up to 50, stepping by valuaes of 5 each iterations")
for x in range (10, 50, 5):
    print (x)

#4 loop that counts from 25, down to and including 0
print ("Loop that counts from 25, down to and including 0")
for x in range (25,-1, -1):
    print (x)

#5 loop that counts backwards from 50 down to -50, stepping by values of -5 each iteration
print("loop that counts backwards from 25 down to and including 0")
for x in range(50, -50, -5):
  print(x)

#6 for the loop that count 10 times. Each iteration you are to ask the user to enter a number. Using that number add it to a running total. At the end of the loop, print out the total of all the numbers added together
total = 10
userinput = 10
for i in range (0, 10):
    userinput = int (input("Please enter a number:"))
    total += userinput
print ("The computed total is:",  total)

#7 user to enter a number. Write a for loop that runs an amount of times based on that number. Within the loop body, multiply the iterator variable by 3, then tell the user if the result of that multiplication is an even or odd number.
total = 0
userinput = int(input("Please enter a number:"))
userinput = userinput + 1
# userinput = userinput + 1 is same as userinput
for i in range(1, userinput): 
    total = userinput * 3

if total % 2 == 0:
    print("The number you entered is even.")
    print(total)
else:
    print("The number you entered is odd.")
    print(total)

#8 - nested for loop. The outer loop should run 10 iterations, the nested loop should run 5 iterations. Print out the value of the iterator variable in each loop body.

outer_loop = 11
inner_loop = 6
for i in range(1, outer_loop):
    print("Outer Loop Iteration #", i)
    for a in range(1, inner_loop):
        print("Inner Loop Iteration #", a)

#9 - nested for loop. The outer loop should run 10 iterations, the nested loop should run 5 iterations. Print out the value of the iterator variable in each loop body.

outer_loop = 10
inner_loop = 10
for a in range(0, outer_loop):
    #print("Outer Loop Iteration #", i)
    for b in range(0, inner_loop):
        first_letter = str(a)
        second_letter = str(b)
        combined_letters = first_letter + second_letter
        print(combined_letters)

for i in range(0, 11):
    print("Outer Loop Iteration #", i)
    for a in range(10, -1, -1):
        print("Inner Loop Iteration #", a)

film_name = input("Please eneter your favorite film:")
film =film_name.strip()
for i in range (0, len(film), 0):
    print (film[i])