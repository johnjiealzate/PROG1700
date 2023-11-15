# Creating a list 
my_list = [1, 2, 3, 4, 5] 
print("Original List:", my_list) 

# Accessing elements of a list
print("Element at index 0:", my_list[0]) 
print("Element at index 2:", my_list[2]) 

# Slicing a list
subset = my_list[1:4] 
print("Subset of the list:", subset) 

###
# Modifying elements 
my_list[2] = 10 
print("Modified List:", my_list) 

#Adding elements 
my_list.append(6) 
print("List after adding an element:", my_list) 

# Removing elements 
my_list.remove(4) 
print("List after removing an element:", my_list) 

# List operations 
length = len(my_list) 
print("Length of the list:", length) 

# Concatenating lists 
new_list = my_list + [7, 8, 9] 
print("Concatenated list:", new_list) 

# Adds element 5 to the end of the list 
my_list.append(5) 
print("List after appending 5:", my_list) 

# Counts the number of the same elements in the list 
count_of_5 = my_list.count(5) 
print("Count of the number 5 in the list:", count_of_5)

# Gets the index of the number 3 in the list 
index_of_3 = my_list.index(3) 
print("Index of the number 3 in the list:", index_of_3)
