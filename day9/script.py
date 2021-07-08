from replit import clear
# Name and value as key-value paris

print("The bidding has started..........")


def get_highest_bid(bidding_records):
    largest_bid = 0
    bids = 0
    name = ""
    for key, value in bidding_records.items():
        if value > largest_bid:
            bids = value
            name = key

    return bids, name


data_dict = {}
bid_inprocess = True
while bid_inprocess:
    name = str(input("What is your name? "))

    try:
        bid_value = int(input("What is you bid? "))
        if bid_value == "" or bid_value is None or name == "" or name is None:
            print("Enter values")
            exit()
    except ValueError:
        print("Enter only numeric value for bid")
        exit()
    data_dict[name] = bid_value
    continue_bid = input("Continue bidding? Type yes or no: ")
    if continue_bid == "yes":
        bid_inprocess = True
        clear()
    elif continue_bid == "no":
        bid_inprocess = False
    else:
        print("Enter yes or no")
        exit()

value, name = get_highest_bid(data_dict)
print(f"{name} is the highest bidder with Rupees {value}")
