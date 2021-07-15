""" 
    This was initially started as coffee machine but changed into a type of any drinking machine
    Drink is generated based on the resources available in resources.json
    To add a new drink, add as the next sequence numbered stat to resources and include neccessary resources in resources object
"""


import json
import time

with open("resources.json", "r") as fp:
    data = json.loads(fp.read())


def get_report():
    """ Returns the resources data from resource.json"""
    msg = ''
    try:
        resources_available = data["resources"]
        status = True
        for k, v in resources_available.items():
            msg += f"\n {k}: {v}"
    except KeyError as e:
        status = False
        msg = "There is no resource compartment"
    return msg


def update_resources(new_data):
    """ Update the resources.json with new updated data"""
    with open("resources.json", "w") as f:
        json.dump(new_data, f)


def dispatch_drink(drink_type, ingredients):
    """ Prepare drink with given ingredients - sample hardware part"""
    completed = True
    if completed:
        return completed, f"Here is your {data['stats'][drink_type]['type']} !!!!"
    else:
        completed = False
        return completed, "Something is wrong. Failed to dispatch"


def prepare_drink(drink_type, ingredients, amount):
    proceed = True
    unavailable_resources = []
    while proceed is True and len(unavailable_resources) == 0:
        for k, v in ingredients.items():
            try:
                rs_value = data["resources"][k] - ingredients[k]
                if rs_value <= 0:
                    unavailable_resources.append(k)
                    break
                else:
                    data["resources"][k] = rs_value
            except KeyError:
                unavailable_resources.append(k)
        proceed = False

    change = amount
    if not unavailable_resources:
        if amount >= data["stats"][str(drink_type)]["cost"]:
            change = round(amount - data["stats"][str(drink_type)]["cost"], 2)
            status, msg = dispatch_drink(drink_type, ingredients)
            data["money"] = data["money"] - \
                data["stats"][str(drink_type)]["cost"]
            update_resources(data)
        else:
            msg = "Sorry that's not enough money. Money refunded."

    else:
        status = False
        msg = "Low or insufficient resources" + \
            "-" + ",".join(unavailable_resources)
    return msg, change


def get_drink(user_input, payment):
    rsc_no = str(user_input)
    drink_ingredient = data["stats"][rsc_no]["ingredients"]

    msg = prepare_drink(rsc_no, drink_ingredient, payment)
    return msg


power_state = True

inputs = len(data["stats"])
drinks_available = [data["stats"][str(s)]["type"]
                    for s in range(1, inputs + 1)]

message_string = "What would you like?" + \
    "(" + ",".join(drinks_available) + ")"
input_strings = []
for i in range(1, inputs + 1):
    input_strings.append(
        f"{i}. {data['stats'][str(i)]['type']}    Cost: {data['stats'][str(i)]['cost']} INR")


report_id = str(inputs + 1)
power_off_id = str(inputs + 2)
input_strings.append(f"{inputs+1}. Report")
input_strings.append(f"{inputs+2}. Power Off")
final_input = message_string + "\n" + \
    "\n".join(input_strings) + "\n" + "Enter a number: "


j = 0
while power_state:
    user_input = input(final_input)
    if user_input == report_id:
        msg = get_report()
        print("*" * 10 + "Available Resources" + "*" * 10)
        print(msg)
        print("\n")
    elif user_input == power_off_id:
        power_state = False
        print("Machine Powered Down....")
    else:
        try:
            payment = int(input("Please Enter amount: "))
            if int(user_input) > inputs + 3:
                print("Choose from the available numbers")
                print("\n")
            else:
                time.sleep(3)
                msg, change = get_drink(int(user_input), payment)
                print("\n")
                print("Preparing your Drink...")
                print(msg)
                print("Balance: ", change, "\n")

        except ValueError:
            print("Enter only numbers")
            print("\n")
