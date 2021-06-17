US_cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
#city_names[0] = "San Francisco"
#city_names[2] = "Brooklyn"
#city_names[7] = "Hollywood"
#city_names[5] = "Tampa"

fruits = ["Strawberry", "Apple", "Watermelon", "Orange", "Pear", "Banana", "Kiwi", "Blueberry", "Raspberry", "Mango"]
fruits[1] = "Lemon"

US_cities.append("New Jersey")
US_cities.extend(["Santa Cruz", "Selma", "Chicago"])
US_cities.insert(7, "Washington, DC")

del US_cities[7]
US_cities.pop(0)
US_cities.remove("Boston")

print(US_cities)