from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()


choice = "on"
while choice != "off":
	drink = input("What would you like? (espresso(Rs 30) / latte(Rs 85) / cappuccino(Rs 175)) : ")
	
	if drink.lower( ) == "off":
		break
	
	elif drink.lower() == "report":
		coffeemaker.report()
		moneymachine.report()
	
	elif drink.lower() in [ "espresso", "latte", "cappuccino" ]:
		d = menu.find_drink(drink)
		if coffeemaker.is_resource_sufficient(d):
			if moneymachine.make_payment(d.cost):
				coffeemaker.make_coffee(d)
