MENU = {
    "espresso": {   
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    },
}

resources = {
    "water": 300,   
    "milk": 200,
    "coffee": 100,
}


def make_cofee():
    machise_is_on = True
    money=0
    while machise_is_on:
        
        customer_choice =input("What would you like? (espresso/latte/cappuccino)").lower()
        if customer_choice == "off":
            print("machine is turned off")
            machise_is_on = False
        elif customer_choice == "report":
            print(f"Water = {resources["water"]} ml")
            print(f"milk ={resources["milk"]}ml")
            print(f"coffee = {resources["coffee"]}g")
        elif customer_choice=="resourcefill":
            resources["water"]=300
            resources["milk"]=200
            resources["coffee"]=100
            print("resources filled")
        else:
            drink=MENU[customer_choice]
            if resources["water"]>=drink["ingredients"]["water"]and resources["coffee"]>=drink["ingredients"]["coffee"]and resources["milk"]>=drink["ingredients"]["milk"]:
                print("please insert coins")
                quarters=int(input("how many quarters?"))*0.25
                dimes=int(input("how many dimes?"))*0.10
                nickels=int(input("how many nickels?"))*0.05
                pennies=int(input("how many pennies?"))*0.01
                total_inserted=int(quarters+dimes+nickels+pennies)
                if total_inserted>drink["cost"]:
                    change =int(total_inserted-drink["cost"])
                    print(f"here is ${change} in change")
                    resources["water"]-=drink["ingredients"]["water"]
                    resources["coffee"]-=drink["ingredients"]["coffee"] 
                    resources["milk"]-=drink["ingredients"]["milk"]
                    money+=drink["cost"]
                    print(f"here is your {customer_choice}☕️. Enjoy!")
                elif total_inserted==drink["cost"]:
                    resources["water"]-=drink["ingredients"]["water"]
                    resources["coffee"]-=drink["ingredients"]["coffee"] 
                    resources["milk"]-=drink["ingredients"]["milk"]
                    money+=drink["cost"]
                    print(f"here is your {customer_choice}☕️. Enjoy!")  
                else:
                    print("sorry that's not enough money. Money refunded.") 
            else:
                print("sorry there is not enough resources")
make_cofee()