#Variables
daily_price = float()
average_week = float()
weekly_price = float()
monthly_price = float()
average_month = float()
days = int()
weeks = int()

days = 1
weeks = 1

while weeks < 5:
    while days < 8:
        daily_price = float(input("Enter today's gas price:  "))
        weekly_price = weekly_price + daily_price
        days = days + 1
    average_week = weekly_price/7
    print("The average per gallon cost for gas this week is:  ", average_week)
    monthly_price = monthly_price + weekly_price
    weekly_price = 0
    days = 1
    weeks = weeks + 1
average_month = monthly_price/28
print("The average per gallon cost for gas this month is:  ", average_month)




