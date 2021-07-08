print("****** Welcome to the tip calculator ********")
try:
    total_bill = int(input("What was the total bill?"))
    percent = int(
        input("What percentage of bill would you like to give 10,12 or 15 or No tip? "))
    no_of_people = int(input("How many people should split the bill? "))
except ValueError:
    print("Please enter a number")
    exit()

if percent not in [10, 12, 15]:
    print("Tip can be either 10,12,15 or 0")
    exit()

if percent != 0:
    print(
        f"Each person should pay: Rs {round(((total_bill/no_of_people)*(percent/100)), 2)}")
else:
    print("Thank you.")


# print("****** Love Calculator ********")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")

# combined_string = name1+name2


# combined_string.lower()

# total1 = 0
# total2 = 0
# for v1, v2 in zip(["t", "r", "u", "e"], ["l", "o", "v", "e"]):
#     total1 += combined_string.count(v1)
#     total2 += combined_string.count(v2)

# love_rate = str(total1)+str(total2)
# print(f"Youir compatibility is {love_rate}%")
