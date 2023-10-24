# Declare global variables
chicken_in_box = 20
days_counter = 1
chicken_eaten_daily = 0
chicken_eaten_when_ill = 0

# Program control for fried chicken dinosaur
while days_counter < 60:
    # Start of the program
    # Cast the input
    days_counter = int (days_counter)
    print ("Fried chicken eaten on day", days_counter, "is", days_counter*1, "lb.")
    if days_counter < 1:
        
        break
        
        
