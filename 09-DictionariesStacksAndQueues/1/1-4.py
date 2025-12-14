person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

print("Name: ", person["name"] + " " + person["surname"])
for item in person["hobby"]:
    print('Hobby: ', item)
print(person['hobby'])
print(person)

person["surname"] = "Nowak"
print(person["surname"])
print(person)

person["married"] = False
print(person)

person["gender"] = "male"
print(person)

person["hobby"].append("bicycle")
print(person['hobby'])

person['phone']['work'] = '313131444'
print(person["phone"])

for key, value in person.items():
    print(f"{key}: {value}")