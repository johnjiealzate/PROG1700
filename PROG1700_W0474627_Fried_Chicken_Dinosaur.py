# Declare global variables
chicken_in_box = 20
days_counter = 0
chicken_eaten_daily = 0
chiecken_eaten_when_ill = 0

# Program control for fried chickhen dinosaur
while chicken_in_box > 0:
    # Start of the program
    # Input the numbeof days the dinosaur has been eating fried chickhen
    days_input = input ("Please enter the count of days the dinosaur is eating the fried chicken:")

    if days_input == 1:
        # Cast the input
        days_input = int (days_counter)
        print ("Fried chickhen eaten on day 1 is 1.00." )
        print ("Chickhen remaining in the box is", chicken_in_box-1)
    elif days_input == 7:
        print ()
else:
    print ("Number of days it took to run out of chikhen is")    