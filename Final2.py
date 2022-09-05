"""
Decomposition
declare four functions
call main function
within the main function
declare variables
give array contents
call function to find total, pass in variables if needed
use loop to add array into total
return total
call function to receive the highest amount of cans and accompanying grade, pass in variables if needed
declare variables
use loop to find highest amount and accompanying grade
print highest amount and accompanying grade
print total
call function to receive the average and amount of varibles above average, pass in variables if needed
declare variables
use loop to find average
print average
use loop to find amount above average
print amount of cans above average

Inputs and outputs
No inputs
Output the grade and their highest cans
Output the total
Output the average
Output how many above average
"""

def highest(can):
    #declare varibles
    high = float()
    temp = float()
    temp2 = int()

    high = can[0]
    #loop to find the highest
    for index in range(0, len(can)):
        temp = can[index]
        if temp > high:
            temp2 = index
            high = temp
    #returning the highest to print
    print("Grade", temp2, "had the highest cans with", high)

def averages(can):
    #declare varibles
    avg = float()
    totalcans = float()
    count = int()
    #loop to find the average from the total
    for index in range(0, len(can)):
        totalcans = totalcans + can[index]
    avg = totalcans / len(can)
    print("This is the average number of cans collected is: ", avg)
    for index2 in range(0, len(can)):
        if (can[index2] > avg):
            count = count + 1
    print("This many classrooms were above average:", count)
    


def total(can):
    #declare varibles
    totalcan = float()
    #loop to find the total
    for index in range(0, len(can)):
        totalcan = totalcan + can[index]
    return totalcan

def main():
    #declare varibles
    largest = int()
    returntotal = int()
    cans = [248, 379, 189, 457, 274, 532, 279, 296, 359]
    #calling functions
    returntotal = total(cans)
    highest(cans)
    #printing varible
    print("This is the total number of cans collected is: ", returntotal)
    #calling final function
    averages(cans)

main()