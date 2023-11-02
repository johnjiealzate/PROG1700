planet = {
    "name" : "Mars",
    "moons" : 2

}

print (planet.get("name"))

print((planet["name"]), "has", planet["moons"], "moon(s)")

my_details = {
    "first_name" : "Johnjie",
    "last_name" : "Alzate",
    "city" : "Lipa City PH",
}

print (my_details["first_name"], my_details["last_name"])



print (f'{my_details["first_name"]} {my_details["last_name"]}')

planet['circumference (km)'] = {'polar': 6751, 'equitorial': 6792}
print(f'{planet}')