info = {
    'first_name': 'Johnjie',
    'last_name': 'Alzate',
    'hometown': 'Lipa City',
    'favfood': 'burger',
    'bestsport': 'tennis',
    'topbands':  ('lifehouse', 'Switchfoot', 'One Republic', 'Muse', 'Nightly', 'Coldplay')
}

info['favsong'] = 'sick cycle carrousel'
print(info['favfood'])
print(info)

# creating dictionaries
student = {
    'name': 'Johnjie Alzate',
    'age': 25,
    'major' : 'IT Generalist',
    'address' : 'Philippines'
}

# update disctionaries
student['courses'] = 'DBAS1007', 'NETW1027', 'OSYS1200'

# output dictionaries
print(student['courses'])
print('\n')
print(student)

# dictionary methods
keys = student.keys()
values = student.values()
items = student.items()
courses = student.get('courses', 'undeclared')

# output  dictionary methods
print(keys)
print('\n')
print(values)
print('\n')
print(items)
print('\n')

# iterating through a dictionary
for key in student:
    print(f'{key}: {student[key]}')
# \n is new line
print('\n')

for key in student:
    print(key,":", " ",  student[key])
print('\n')

# using a for loop with items
for key, value in student.items():
    print(f'{key}: {value}')
