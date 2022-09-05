#declare variables
days = int()
people = int()
total = float()
ticket = float()
#Ask user for the number of people and the number of days
days = int(input("Enter the number of days you will be in the park:  "))
people = int(input("Enter the number of people in your party:  "))
#Determine ticket price
if days == 1:
    price = 40
if days == 2:
    price = 35
else:
    price = 25
#Determine total cost
total = people * price * days
#print price per day and total
print("Price per day:  $", price)
print("Total for your trip:  $", total)