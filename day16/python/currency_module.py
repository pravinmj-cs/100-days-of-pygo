from drink_module import DrinkMaker


class MoneyMaker():

    CURRENCY = "$"

    COIN_VALUES = [0.25, 0.10, 0.05, 0.01]

    def __init__(self):
        self.money_received = 0

    def __process_coins(self, coins):
        """Returns the total calculated from coins inserted."""
        total_cost = 0
        print(coins, "***********")
        for value, coin in zip(self.COIN_VALUES, coins):
            print(value, coin)
            total_cost += value * coin

        self.money_received += total_cost

        return total_cost

    def process_payment(self, coins, drink_cost):
        """Returns True when payment is accepted, or False if insufficient."""
        paid_cost = self.__process_coins(coins)
        if paid_cost >= drink_cost:
            change = round(paid_cost - drink_cost)
            status = True
        else:
            change = 0
            status = False
            print("Sorry that's not enough money. Money refunded.")
        return status, paid_cost, change
