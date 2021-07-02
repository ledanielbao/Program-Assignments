city_names = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]
#city_names[0] = "San Francisco"
#city_names[2] = "Brooklyn"
#city_names[7] = "Hollywood"
#city_names[5] = "Tampa"

# while loop to access all values
# access value with index
# check to make sure that index is less than list length

def printCityNames(cities_list):
    counter = 0
    while counter < len(cities_list):
        print(cities_list[counter])
        counter += 1
    return "completed"

#printCityNames(city_names)

# [longer names ... shorter names]
# get the length of listitem1, listitem2
#check if len[listitem1] > len[listitem2]
#    move on 
#else
#    remove listitem
#    put list item at end 
# return list

#return new list

#def organize_cities(cities_list):
    counter = 0
    for city in cities_list:
        print(city)
        if (len(cities_list[counter]) > len(cities_list[counter +1])):
            print()
            counter+=1
        else: 
            cities_list.remove(city)
            cities_list.append(city)
            counter+=1

    return cities_list

def organize_cities(cities_list):
    for index in range(len(cities_list)-1):
        if cities_list[index] >= cities_list[index + 1]:
            continue
        else:
            city = cities_list[index]
            cities_list.pop(index)
            cities_list.append(city)
    return cities_list

print(city_names)
print(organize_cities)

#organize_cities(city_names)


#fruits = ["Strawberry", "Apple", "Watermelon", "Orange", "Pear", "Banana", "Kiwi", "Blueberry", "Raspberry", "Mango"]
#fruits[1] = "Lemon"

#city_names.append("New Jersey")
#city_names.extend(["Santa Cruz", "Selma", "Chicago"])
#city_names.insert(7, "Washington, DC")

#del city_namess[7]
#city_names.pop(0)
#city_names.remove("Boston")