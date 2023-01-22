age = input("What is your current age? ")
remain_years = 90 - int(age)
remain_days = remain_years * 365
remain_weeks = remain_years * 52
remain_months = remain_years * 12

res_message = f"You have {remain_days} days, {remain_weeks} weeks, and {remain_months} months left."

print(res_message)