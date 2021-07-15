from drink_module import DrinkMaker
from currency_module import MoneyMaker
from time import sleep


POWER_ON = True
print("\n", "-" * 20 + "TURNED ON" + "-" * 20)

COINS = [1, 2, 5, 10]

drink_maker = DrinkMaker()
money_maker = MoneyMaker()
if not drink_maker.is_ready:
    print("****************Incomplete configuration. Failed to start machine*******************")
    exit()


menu_ids, menu_input = drink_maker.menu()

resources = drink_maker.data["resources"]
drinks_available = drink_maker.data["stats"]
order_stats = {}
for resource in resources:
    order_stats[resource] = 0
while POWER_ON:
    try:
        print("\n")
        user_input = int(input(menu_input))
        print("\n")
        if user_input == menu_ids["report"]:
            print("\n", "-" * 20 + "Available Resources" + "-" * 20)
            print(drink_maker.report())
            print("\n")
        elif user_input == menu_ids["power_off"]:
            loading = "Powering Down Machine"
            for i in range(35):
                if i <= 20:
                    print(loading[i], sep="", end="", flush=True)
                elif i > 20:
                    print(".", sep=" ", end=" ", flush=True)
                sleep(0.1)
            print("\n", "-" * 20 + "TURNED OFF" + "-" * 20)
            POWER_ON = False
        elif user_input == menu_ids["admin_login"]:
            password = input("Enter Password: ")
            print(drink_maker.admin_report(password))
            print("\n")
        else:
            if drink_maker.is_resource_sufficient(user_input):
                total_coins = []
                for i in COINS:
                    print(i, "****", total_coins)
                    coin = int(input(f"How many {i} ruppee coin? "))
                    if coin == "" or coin is None:
                        coin = 0
                    elif isinstance(coin, str):
                        coin = 0
                    total_coins.append(coin)
                required_cost = drinks_available[str(user_input)]["cost"]
                status, total_cost, change = money_maker.process_payment(
                    total_coins, required_cost)

                if status:
                    print(drink_maker.make_drink(
                        user_input, total_cost))
                    print(f"Balance: {change}")
                else:
                    print()

            else:
                print("Low on resources. Please contact your admin")

    except ValueError as e:
        print("Wrong input. Please enter number", "\n")
