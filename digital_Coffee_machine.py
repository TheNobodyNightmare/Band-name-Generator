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

machine_water = resources["water"]
machine_milk = resources["milk"]
machine_coffee = resources["coffee"]

while True:
    print("Welcome To the Digital Coffee Machine")
    choice = input("What would you like (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("The Coffee Machine is Turned Off")
        break

    if choice == "report":
        print(f"Water: {machine_water}")
        print(f"Milk: {machine_milk}")
        print(f"Coffee: {machine_coffee}")
        continue
