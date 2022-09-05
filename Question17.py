"""
Decomposition
declare varibles
ask for user input
perform math
perform if statement
within each statement print the amount
"""



ppl = int()
hd = float()
find = float()

ppl = int(input('How many people are comeing to the party: '))

hd = ppl * 1.5
find = hd % 10

if find >= 5:
    hd = hd - find
    hd = hd / 10
    hd = hd + 1
    print('Please purchase this many packs of hotdogs: ', + hd)
else:
    hd = hd - find
    hd = hd / 10
    print('Please purchase this many packs of hotdogs: ', + hd)