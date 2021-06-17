# LAB STEP 1 IS OPENING AND SAVING FILE

# LAB STEP 2
grocery_list = {"chicken": 1.59, "beef" : 1.99, "cheese" : 1.00, "milk": 2.50 }
# LAB STEP 3: MAKE SURE TO CUSTOMIZE DICTIONARY NAME, KEY AND VALUE
coffee_prices = {"latte" : 4.25, "machiatto" : 2.80, "cappucino" : 3.60, "americano" : 3.20}

# LAB STEP 4: ACESSING PRICES
latte_price = coffee_prices["latte"]
machiatto_price = coffee_prices["machiatto"]
cappucino_price = coffee_prices["cappucino"]
americano_price = coffee_prices["americano"]
# 
#print(coffee_prices["latte"])
#print(coffee_prices["machiatto"])

#add two items together to know the cost
def total_price (item1, item2):
    price = grocery_list[item1] + grocery_list[item2]
    return price 

def price_difference (item1, item2):
    price = grocery_list[item1] - grocery_list[item2]
    return price 

#print(price_difference("beef", "cheese"))
#print("The total price of beef and cheese is:" , total_price("cheese", "beef"))
   

# LAB STEP 5: ACESSING PRICES PT 2
chicken_price = grocery_list["chicken"]
# accesses the grocery list dictionary, finds the key "chicken" and returns the value
beef_price = grocery_list["beef"]
cheese_price = grocery_list["cheese"]
milk_price = grocery_list["milk"]


# STEP 5.2
coffee_prices["latte"] -= 1.0
coffee_prices["machiatto"] = 2.0
coffee_prices["cappucino"] -= 0.5 
coffee_prices["americano"] -= 1.25

#print(coffee_prices["latte"])
#print(coffee_prices["machiatto"])

# STEP 6
shoe_inv = {"Jordan 13": 1, "Yeezy" : 8, "Foamposite" : 10, "Air Max": 5, "SB Dunk": 20}
#print(shoe_inv)

def restock (multiplier):
    for shoe in shoe_inv:
        total_items = (shoe_inv[shoe] * multiplier)
        shoe_inv[shoe] = total_items
    return total_items

def clearance_sale(shoe_name, clearance_amount):
    new_price = shoe_inv[shoe] / clearance_amount # new price
    shoe_inv[shoe_name] = new price # SB DUNK = 20/5 = 4

#restock(3)
clearance_sale("SB Dunk", 5)
print(shoe_inv)

# STEP 7 
shoe_inv["SB Dunk"] -= 2
shoe_inv["Yeezy"] += 1
#print(shoe_inv)

shoe_inv["Pegasus"] = 6
#print(shoe_inv)