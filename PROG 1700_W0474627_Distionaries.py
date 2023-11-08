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
print(student)

# dictionary methods
keys = student.keys()
values = student.values()
items = student.items()
courses = student.get()