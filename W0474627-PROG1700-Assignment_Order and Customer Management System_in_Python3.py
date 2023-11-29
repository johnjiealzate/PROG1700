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
        "4. Generate All Customer Report\n",
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
    
    # Generate customer report Menu#3
    elif menu_choice == 3:
        customer_id = int(input("Enter customer ID: "))
        def generate_customer_report(customer_id):
            global customers
            customer_name = customer_name.get(customer_id)
            if customer_name:
                print(f"\nCustomer Report for {customer_name["name"]}:")
                print(f"Contact: {customer_name["contact"]}")
                total_spending = sum(order["total_cost"])
                print(f"Total spending: ${total_spending: 2f}")
                print("Orders:")
                for order in customer_name['orders']:
                    print(f" Order ID: {order["order_id"]} | Product: {order["product_name"]} | Quantity: {order["quantity"]}")
            else:
                print("Customer not found.")
        generate_customer_report(customer_id)
                
    # Generate all customer report Menu4
    elif menu_choice == 4:
        def generate_all_customer_reports():
            global customers
            for customer_id, _ in customers.items():
                generate_all_customer_reports(customer_id)
        generate_all_customer_reports(customer_id)
    
    # Exit Menu5
    elif menu_choice == 5:
        print("Thank you for using the Order and Customer Management System (OCMS).")
        break
    
    else:
        print("Invalid choice. Please enter a valid number between 1 and 5.")