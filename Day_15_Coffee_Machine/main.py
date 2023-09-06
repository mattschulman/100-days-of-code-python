
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def check_transaction(cost):
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    amount_input = (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)
    #print(f"Amount input is ${amount_input}")
    #print(f"Amount needed is ${cost}")
    if amount_input < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif amount_input > cost:
        amount_refunded = amount_input - cost
        print(f"Here is ${amount_refunded:.2f} in change.")
        return True
    else:
        print("You put in the exact amount needed!")
        return True

def sufficient_resources(ingredients):
    have_all_ingredients = True
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            #print(f"Available {ingredient} - {resources[ingredient]}.  Needed: {ingredients[ingredient]}")
            print(f"Sorry, We do not have enough {ingredient}")
            have_all_ingredients = False
    if have_all_ingredients:
        #print("Returning True")
        return True
    else:
        #print("Returning False")
        return False


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    if "money" in resources.keys():
        print(f"Money: ${resources['money']:.2f}")
        
machine_off = False
while not machine_off:
    #response = action(resources)
    response = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if response == "off":
        machine_off = True
    elif response == "report":
        print_report()
    elif response == "espresso" or response == "latte" or response == "cappuccino":
        if sufficient_resources(MENU[response]["ingredients"]):
            if check_transaction(MENU[response]["cost"]):
                print(f"Here is your {response} ☕️.  Enjoy!")
                if "money" not in resources.keys():
                    resources["money"] = MENU[response]["cost"]
                else:
                    resources["money"] += MENU[response]["cost"]
                #print(f"Money - ${resources['money']:.2f}")
                for ingredient in MENU[response]["ingredients"]:
                    resources[ingredient] -= MENU[response]["ingredients"][ingredient]
                    #print(f"{ingredient} - {resources[ingredient]}")
