'''
decomposition
declare varibles
enter loop
determine which burger the user wants
if statement leads to ask how many that user wants
does math for subtotals and totals
ask if user wants cheese
if statement for that
if yes do math then ask user if they want to quit
if no just ask if user wants to quit
if user doesn't enter quit repeat loop
print out subtotals and total

inputs and output
input burger type
input cheese decision
input if user wants to quit
output the subtotals
output the total

What condition needs to exist in order for your loop to end?
if choose does not equal 'quit' the loop contines
when the user inputs 'quit' the loop ends
'''
cheese = str()
burger = str()
choose = str()
quantity = int()
sub1 = float()
sub2 = float()
sub3 = float()
total = float()

while choose != "quit":
    burger = input("Please enter what burger you want, singleburger, deluxeburger, extremeburger:")
    if burger == "singleburger":
        quantity = int(input("Enter how many burger of this type you want: "))
        sub1 = sub1 + quantity * 5.50
        total = total + quantity * 5.50
        cheese = input("would you like cheese on those burgers yes or no: ")
        if cheese == "yes":
            sub1 = sub1 + quantity * 2
            total = total + quantity * 2
            choose = input("If you would like to end your order enter quit: ")
        else:
            choose = input("If you would like to end your order enter quit: ")
    elif burger == "deluxeburger":
        quantity = int(input("Enter how many burger of this type you want: "))
        sub2 = sub2 + quantity * 8.00
        total = total + quantity * 8.00
        cheese = input("would you like cheese on those burgers yes or no: ")
        if cheese == "yes":
            sub2 = sub2 + quantity * 2
            total = total + quantity * 2
            choose = input("If you would like to end your order enter quit: ")
        else:
            choose = input("If you would like to end your order enter quit: ")
    elif burger == "extremeburger":
        quantity = int(input("Enter how many burger of this type you want: "))
        sub3 = sub3 + quantity * 10.00
        total = total + quantity * 10.00
        cheese = input("would you like cheese on those burgers yes or no: ")
        if cheese == "yes":
            sub3 = sub3 + quantity * 2
            total = total + quantity * 2
            choose = input("If you would like to end your order enter quit: ")
        else:
            choose = input("If you would like to end your order enter quit: ")
    else:
        print("you didn't enter a name correctly")
print("Here is your first subtotal:", sub1)
print("Here is your second subtotal:", sub2)
print("Here is your third subtotal:", sub3)
print("Here is your total:", total)