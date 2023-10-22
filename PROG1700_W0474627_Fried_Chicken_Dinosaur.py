# Declare global variabale
chicken_in_box = 20
days_counter1 = 1
days_counter2 = 7
chicken_eaten_daily = 0
chicken_eaten_when_ill = 0
increase_in_eaten_chicken = 1
remaining_chicken = chicken_in_box - 1

# Main program control
# Return true if chicken in a box in more than 0
while chicken_in_box > 0: 
    # Output the chicken eaten per day and the remaining chicken in the box
    print ("Fried chicken eaten on day", round(days_counter1, 2), "=", round(increase_in_eaten_chicken, 2))
    print ("Fried chicken remaining: =", round(remaining_chicken, 2))
    # Continue the loop until days 6 
    if days_counter1 == 6:
        while True:
            # return true and continue to output the remaining chicken in a box when the dinosaur becomes ill and does not eat chicken on day 7
            if days_counter2 == 7:
                print ("Fried chicken eaten on day", round(days_counter2, 2), "=", round(chicken_eaten_when_ill, 2))
                print ("Fried chicken remaining: =", round((remaining_chicken - chicken_eaten_when_ill), 2))
                if days_counter2 == 14:
                    break
                days_counter2 += 1
                remaining_chicken -= 1
            # return false and output the remaining chicken per day after day 7 until remaining chicken in a box becomes zero   
            else:
                print ("Fried chicken eaten on day", round(days_counter2, 2), "=", round(increase_in_eaten_chicken, 2))
                print ("Fried chicken remaining: =", round((remaining_chicken - chicken_eaten_when_ill), 2))
                if remaining_chicken <= 0:
                    print (chicken_in_box == 0)
                    print("The number of days it took to run out of chicken is", days_counter2, "days.")
                    break
       
                days_counter2 += 1
                increase_in_eaten_chicken += 0.05
                remaining_chicken -= 1.05
                chicken_in_box == 0
              
        break
    days_counter1 += 1
    increase_in_eaten_chicken += 0.05
    remaining_chicken -= 1.05 