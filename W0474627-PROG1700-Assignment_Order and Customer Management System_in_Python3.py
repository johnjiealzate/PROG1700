"""
Auhor: Johnjie Alzate
Student ID: W0474627
Course: IT Generalist
Programming Language: Python
Date: 11-22-23
Version: 3
"""

# Create empty dictionary
customers = {}

# Initial customer ID from an empty customers distionary
customer_id = 0

# Menu
while True:
    print ("Order and Customer Management Menu:\n",
        "1. Add Customer\n",
        "2. Place Order\n",
        "3. Generate Customer Report\n",
        "4. Generate aAll Customer Report\n",
        "5. Exit\n", 
        "\n",
        )
    # Input for menu selection
    menu_choice = int(input("Enter your choice (1-5): "))

    # Add customer Menu #1
    if menu_choice == 1:
        def add_customer():
            global customers
            global customer_id
            customer_name = input("Enter customer name: ")
            Customer_contact_number = input("Enter customer contact number: ")
            customer_id = customer_id + 1
            customers[customer_id] = {"name": customer_name, "contact": Customer_contact_number, "orders": []}
            print("Customer added successfully!")
            print (customers)
        add_customer()
        
    # Place order Menu #2
    elif menu_choice == 2:
        customer_id = int(input("Enter customer ID: "))
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        unit_price = float(input("Enter the unit price:"))
        def place_order(customer_id, product_name, quantiy, unit_price):
            global customers
            order_id = len(customers[customer_id]["Orders"]) + 1
            total_cost = quantiy * unit_price
            order = {"order_id": order_id, "product_name": product_name, "quantity": quantiy, "total_cost": total_cost}
            customers[customer_id]["orders"].append(order)
            print("Order placed successfully!")
            print(customers)
        place_order(customer_id, product_name, quantity, unit_price)
        
            
    # Add new customer menu #1       
    '''elif menu_choice == 2:'''