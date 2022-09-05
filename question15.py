'''
decomposition
declare four functions
call main function
within the main function
declare variables
take carpet inputs
call function to receive back an area, pass in variables if needed
within the area function
preform math and return a number
call next function for cost, pass in variables if needed
preform math
return total cost
print the area
call function for waste, pass in variables if needed
preform math
output the waste, return no varible
print the total cost

inputs and output
input length
input width
output area
output waste
output cost
'''
def area(leng, wid):
    airea = float()
    airea = leng * wid
    return airea

def cost(area):
     total_cost = float()
     total_cost = area * 3.5
     return total_cost

def waste(area):
    total_waste = float()
    total_waste = area * 0.10
    print("The total waste is:", total_waste)

def main():
    returned_area = float()
    length = float()
    width = float()
    total_cost_main = float()

    length = float(input("Enter room length in feet: "))
    width = float(input("Enter room width in feet: "))

    returned_area = area(length, width)
    total_cost_main = cost(returned_area)
    print("The area needed is:", returned_area)
    waste(returned_area)
    print("The total cost is:", total_cost_main)

main()