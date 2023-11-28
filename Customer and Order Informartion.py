customers = {}

def add_customer():
    global customers
    name = input("Enter customer name: ")
    contact = input("ENter customer contact number: ")
    customer_id = len(customers) + 1
    customers[customer_id] = {"name": name, "contact": contact, "orders": []}
    print("Customer added successfully")
    
def place_order(customer_id, product_name, quantiy, unit_price):
    global customers
    order_id = len(customers[customer_id]["Orders"]) + 1
    total_cost = quantiy * unit_price
    order = {"order_id": order_id, "product_name": product_name, "quantity": quantiy, "total_cost": total_cost}
    customers[customer_id]["orders"].append(order)
    print("Order placed successfully!")
    print(customers)
    
def generate_customer_report(customer_id):
    global customers
    customer = customers.get(customer_id)
    if customer:
        print(f"\nCustomer Report for {customer['name']}:")
        print(f"Contact: {customer['contact']}")
        
        total_spending = sum(order['total_cost'])
            
        print(f"Total spending: ${total_spending: 2f}")
        print("Orders:")
        for order in customer['orders']:
            print(f" Order ID: {order['order_id']} | Product: {order['product_name']} | Quantity: {order['quantity']}")
    else:
        print("Cutomer not found.")
    
    def generate_all_reports():
        global customers
        for customer_id, _ in customers.items():
            generate_all_reports(customer_id)
            
# Menu Setup
while True:
    print("\nOrder and Cutomer Management System Menu:")
    print("1. Add CUstomer")
    print("2. Place Order")
    print("3. Generate Cutomer Report")
    print("4. Generate All Customer Reports")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_customer()
    elif choice == '2':
        customer_id = int(input("Enter customer ID: "))
        product_name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        unit_price = float(input("Enter the unit price:"))
        place_order(customer_id, product_name, quantity, unit_price)
    elif choice == '3':
        customer_id = int(input("Enter customer ID: "))
        generate_customer_report(customer_id)
    elif choice == '4':
        generate_customer_report(customer_id)
    elif choice == '5':
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid number between 1 and 5.")
        
    
