from json import loads, dump


class DrinkMaker:
    """Models the machine that makes the drink"""

    def __init__(self):
        self.required_items = ["stats", "resources",
                               "money", "total_orders", "stored_password"]
        with open("resources.json", "r") as fp:
            self.data = loads(fp.read())

        if len(list(self.data.keys())) == len(self.required_items):
            self.is_ready = True
        else:
            self.is_ready = False

    def report(self):
        """Prints a report of all resources."""
        resources_available = self.data["resources"]
        status = True
        msg = ""
        for k, v in resources_available.items():
            msg += f"\n {k}: {v}"
        return msg

    def __check_admin(self, password):
        """ Validate input password with stored password in resources.json """
        if password is None or password == "":
            print("Admin Login failed")
            return False

        print(self.data)
        stored_password = self.data["stored_password"]
        if stored_password == password:
            return True
        else:
            return False

    def admin_report(self, password):
        """Prints a report of all resources with overall order status, profits and amount available"""
        status = self.__check_admin(password)
        if status:
            report = self.report()
            report = "\n"
            for k, v in self.data["resources"].items():
                report += f"\n {k}:{v}"
            report += "\n" + \
                f"Total Money Available: {self.data['money_available']}" + "\n"
            for k, v in self.data["total_orders"]:
                report += "\n" + f"{k}: {v}"

            return report
        else:
            return "Failed Authentication"

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        ingredients_required = self.data['stats'][str(drink)]["ingredients"]
        can_make = True
        for item, value in self.data["resources"].items():
            if item in ingredients_required and (value - ingredients_required.get(item)) < 0:
                can_make = False
                print(f"Sorry there is not enough {item}.", "\n")
        return can_make

    def __update_resources(self):
        """ Update the resources.json with new updated data"""
        with open("resources.json", "w") as f:
            dump(self.data, f)

    def make_drink(self, order, total_cost):
        """Deducts the required ingredients from the resources."""
        ingredients = self.data['stats'][str(order)]['ingredients']
        for item, value in ingredients.items():
            resource_name = self.data['resources']
            self.data['resources'][item] -= value
        self.data['money_available'] -= total_cost
        self.data['total_orders'] += 1
        print(
            f"Here is your {self.data['stats'][str(order)]['type']} 🍶 Enjoy!")
        self.__update_resources()

    def menu(self):
        drinks = self.data["stats"]
        inputs = len(drinks)
        self.drinks_available = [
            drinks[str(s)]["type"] for s in range(1, inputs + 1)]
        message_string = "What would you like?" + \
            "(" + ",".join(self.drinks_available) + ")"
        input_strings = []
        menu_id = {}
        for i in range(1, inputs + 1):
            drink_type = drinks[str(i)]["type"]
            menu_id[drink_type] = int(i)
            input_strings.append(
                f"{i}. {drinks[str(i)]['type']}    Cost: {drinks[str(i)]['cost']} INR")
        report_id = str(inputs + 1)
        menu_id["report"] = int(report_id)
        power_off_id = str(inputs + 2)
        menu_id["power_off"] = int(power_off_id)
        admin_login_id = str(inputs + 3)
        menu_id["admin_login"] = int(admin_login_id)
        input_strings.append(f"{inputs+1}. report")
        input_strings.append(f"{inputs+2}. power off")
        input_strings.append(f"{inputs+3}. admin")
        final_input = message_string + "\n" + \
            "\n".join(input_strings) + "\n" + "Enter a number: "

        return menu_id, final_input
