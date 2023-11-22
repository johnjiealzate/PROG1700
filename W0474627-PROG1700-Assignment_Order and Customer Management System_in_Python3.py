"""
Auhor: Johnjie Alzate
Student ID: W0474627
Course: IT Generalist
Programming Language: Python
Date: 11-22-23
Version: 3
"""

customers = {
    1: {"name" : "Alice", "contact" : "123-456-7890","orders" : []},
    2: {"name" : "Bob", "contact" : "987-654-3210","orders" : []}
}
for key, value in customers.items():
        print(f'{key}: {value}')

# Output
print ("Order and Customer Management Menu:\n",
       "1. Add Customer\n",
       "2. Place Order\n",
       "3. Generate Customer Report\n",
       "4. Generatae aAll Customer Report\n",
       "5. Exit\n", 
       "\n",
       )
menu_choice = int(input("Enter your choice (1-5): "))

# Add new customer
def new_customer (new):
    print(f"{new} is the new customer.")
new_customer("emil")

