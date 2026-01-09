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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resouces_sufficent(Order_ingrediant):
    for item in Order_ingrediant:
       if Order_ingrediant[item] > resources[item]:
           print(f"Sorry there is not enough {item}.")
           return False
    return True     
def process_coin():
    print("insert coins please ")
    total = int(input("Enter the no of quarters")) * 0.25
    total += int(input("Enter the no of dimes:")) * 0.1
    total += int(input("Enter the no of Nickles:")) * 0.05
    total += int(input("Enter The no of Pennines:")) * 0.01
    return total 
def check_transaction(payment,drink_cost):
    if payment >= drink_cost: 
        global profit
        profit += drink_cost     
        extra_money = round(payment - drink_cost,2)
        profit = drink_cost
        if extra_money > 0: 
            print(f"Here is your extra change ${extra_money}")
        return True  
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False 

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your Coffee {drink_name}")             


while True:
    print("Welcome To the Digital Coffee Machine")
    choice = input("What would you like (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("The Coffee Machine is Turned Off")
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
        continue
    else:
        drink = MENU[choice]
        if is_resouces_sufficent(drink["ingredients"]):     
            payment = process_coin()
            if check_transaction(payment,drink['cost']):
                make_coffee(choice,drink["ingredients"])
