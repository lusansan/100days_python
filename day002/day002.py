print("Welcome to the tip calculator.")
bill_amout = input("What was the total bill? $")
bill_people = input("How many people to split the bill? ")
bill_tip_rate = input("What percentage tip would you like to give? 10, 12, or 15? ")
tip = float(bill_amout)*(1 + int(bill_tip_rate)/100)/int(bill_people)
print("Each person should pay: ${:.2f}".format(tip))