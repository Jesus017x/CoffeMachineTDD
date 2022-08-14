import sys

print("Welcome to Jesus' Coffee Machine")

def get_sugar():
    sugar = input('How much sugar (in grams)? ')
    return int(sugar)

ssugar = str(get_sugar())
sugar = int(ssugar)

DATA = {
    "small": {
        "ingredients": {
            "coffee": 10,
            "sugar" : sugar,
            "small_cup": 1
        },
        "cost": 2,
    },
    "medium": {
        "ingredients": {
            "coffee": 15,
            "sugar": sugar,
            "medium_cup": 1
        },
        "cost": 3,
    },
    "large": {
        "ingredients": {
            "coffee": 20,
            "sugar": sugar,
            "large_cup": 1,
        },
        "cost": 4,
    }
}

profit = 0
resources = {
    "coffee": 1000,
    "sugar": 600,
    "small_cup": 50,
    "medium_cup": 50,
    "large_cup": 50,
}

def is_resource_sufficient(inputs):
    for item in inputs:
        if inputs[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            sys.exit()
    return True

def process_coin():
    total = int(input('How many quarters (25 cents)? ')) * 0.25
    total += int(input('How many dimes (10 cents)? ')) * 0.1
    total += int(input('How many nickels (5 cents)? ')) * 0.05
    total += int(input('How many pennies (1 cent)? ')) * 0.01
    return total

def is_transaction_okay(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money, Money refunded!")
        return False

def get_coffee(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name} 🍵")

on = True
while on:
    choice = input('What would you like (small/medium/large/sugar/report/off): ')
    if choice == 'sugar':
        get_sugar()
        continue 
    if choice == 'off': 
        on = False
    elif choice == 'report':
        print(f'Coffee: {resources["coffee"]}ml')
        print(f'Sugar: {resources["sugar"]}gr')
        print(f'Small cup: {resources["small_cup"]} units')
        print(f'Medium cup: {resources["medium_cup"]} units')
        print(f'Large cup: {resources["large_cup"]} units')
        print(f'Profit: ${profit}')
    else:
        drink = DATA[choice]
        if is_resource_sufficient(drink['ingredients']):
            pay = process_coin()
            if is_transaction_okay(pay, drink['cost']):
                get_coffee(choice, drink['ingredients'])
        