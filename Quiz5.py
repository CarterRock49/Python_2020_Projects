'''
decomposition
declare four functions
call main function
within the main function
declare variables
give array contents
call function to receive back the lowest, pass in variables if needed
within the lowest function
declare varibles
loop through to find lowest
return lowest
print the lowest
call function to receive back the highest, pass in variables if needed
within the highest function
declare varibles
loop through to find highest
return highest
print the highest
call function for average, pass in variables if needed
declare varibles
loop through to add to total
return average
pritn average
'''
def lowest(nitrogen):
    low = float()
    allnitro = float()

    low = nitrogen[0]
    for index in range(0, len(nitrogen)):
        allnitro = nitrogen[index]
        if allnitro < low:
            low = allnitro
    return low

def highest(nitrogen):

    high = float()
    allnitro = float()

    high = nitrogen[0]
    for index in range(0, len(nitrogen)):
        allnitro = nitrogen[index]
        if allnitro > high:
            high = allnitro
    return high
    


def average(nitrogen):
    avg = float()
    total = float()
    for index in range(0, len(nitrogen)):
        total = total + nitrogen[index]
    avg = total / len(nitrogen)
    return avg
    

def main():
    days = [''] * 6
    nitrogen = [0.0] * 7
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    nitrogen = [0.8, 1.63, 1.75, 0.6, 1.5, 0.87, 1.1]
    low_nitro = float()
    high_nitro = float()
    averagereturn = float()

    low_nitro = lowest(nitrogen)
    print(low_nitro)
    high_nitro = highest(nitrogen)
    print(high_nitro)
    averagereturn = average(nitrogen)
    print(averagereturn)


main()