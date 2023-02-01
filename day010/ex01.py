def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return month_days[month-1]
year = int(input("Enter a year:\n"))
month = int(input("Enter a month:\n"))
days = days_in_month(year, month)
print(days)