"""
Auhor: Johnjie Alzate
Student ID: W0474627
Course: IT Generalist
Programming Language: Python
Date: 11-22-23
Version: 3
"""
customer_id = 0

# Create empty dictionary
customers = {}
customer_details = {}
order_details = []
order_information = {}

for key, value in customers.items():
        print(f'{key}: {value}')

# Output
print ("Order and Customer Management Menu:\n",
       "1. Add Customer\n",
       "2. Place Order\n",
       "3. Generate Customer Report\n",
       "4. Generate aAll Customer Report\n",
       "5. Exit\n", 
       "\n",
       )
menu_choice = int(input("Enter your choice (1-5): "))

while customer_id >= 0:
    # Add new customer menu #1
    if menu_choice == 1:
        print ("Enter customer details:")
        new_customer = input("Name: ")
        new_contact = input("Contact: ")
        print("\n")
        print("Customer added successfully!")

        # add name in the customer deatils dictionary
        customer_details['Name'] = new_customer
        customer_id = customer_id + 1
        customers[customer_id] = {"name"}

        # add contact in the customer deatils dictionary
        customer_details['contact'] = new_contact

        print(customer_id)

        for key, value in customer_details.items():
            print(f'{key}: {value}')




'''
        def new_customer (new):
            print(f"{new} is the new customer.")
        new_customer("emil")
'''

'''
set to store multiplke customer
customers={customer1, customer 2, }

list to store customer information
'''