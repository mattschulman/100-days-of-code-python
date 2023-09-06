from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menu = Menu()

is_off = False
while not is_off:
    choice = input(f"What would you like? ({my_menu.get_items()}): ").lower()
    if choice == "off":
        is_off = True
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = my_menu.find_drink(choice)
        if drink != None:
            #print(drink.name)
            #print(drink.cost)
            #print(drink.ingredients)
            can_make_drink = my_coffee_maker.is_resource_sufficient(drink)
            if can_make_drink:
                print(f"A {drink.name} costs ${drink.cost:.2f}")
                payment_complete = my_money_machine.make_payment(drink.cost)
                if payment_complete:
                    my_coffee_maker.make_coffee(drink)
            else:
                print(f"There are not enough resources to make a {drink.name}")
