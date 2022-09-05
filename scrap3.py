

def PrintCupcakes(cupcakes):
    #variables
    one_cupcake = float()
    print("Cupcake Monthly Sales")
    print("******************************")

    for index in range(0, 6):
        print(cupcakes[index])

    print()

def FindHighest(cupcakes):
    #variables
    high = float()
    one_cupcake = float()

    high = cupcakes[0]

    for index in range(0, len(cupcakes)):
        one_cupcake = cupcakes[index]
        if one_cupcake > high:
            high = one_cupcake
    return high

def main():
    #variables
    cupcakes = [0] * 6
    high_sales = float()
    cupcakes = [200, 350, 185, 765, 452, 211]
    
    PrintCupcakes(cupcakes)
    high_sales = FindHighest(cupcakes)
    
    print("Highest sales:  ", high_sales)
main()

