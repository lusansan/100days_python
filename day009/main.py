import os
from material import logo

auction_info = {}

run = True
while run:
    print(logo)
    print("Welcome to the pravite bidding auction.\n")
    name = input("What is your name?\n")
    bid_price = float(input("How much would you like to bid?\n$"))
    auction_info[name] = bid_price
    choice = input("Are there any other bidders for this auction?\nType 'Yes' or 'No': ").lower()
    if choice == "no":
        run = False
    else:
        i = os.system("clear")

winner_name = ''
highest_bidder = 0

for name,price in auction_info.items():
    if price > highest_bidder:
        winner_name = name
        highest_bidder = price

print("\n")
print(f"The highest bidder is {winner_name} with a ${highest_bidder}")
print("Thank you for your participation.")
