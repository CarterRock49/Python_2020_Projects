"""
Decomposition
Ask for name input
Ask for number input
Do math
Display name
Display number result

Algorithm
Input name
Input season1 numbers
Input season2 numbers
Input season3 numbers
Find the percent for season1
Find the percent for season2
Find the percent for season3
Find total games played and won
Find total percent
Output season1 numbers
Output season2 numbers
Output season3 numbers
Output total numbers
"""

name = input("Please enter your team name: ")
played1 = int(input("Please enter total games played in season 1: "))
won1 = int(input("Please enter total games won in season 1: "))
played2 = int(input("Please enter total games played in season 2: "))
won2 = int(input("Please enter total games won in season 2: "))
played3 = int(input("Please enter total games played in season 3: "))
won3 = int(input("Please enter total games won in season 3: "))

result1 = won1 / played1
result2 = won2 / played2
result3 = won3 / played3
total = played3 + played2 + played1
totalwon = won3 + won2 + won1
totalper = totalwon / total
result1 = result1 * 100
result2 = result2 * 100
result3 = result3 * 100
totalper = totalper * 100

print("Teamname: ", name)
print("Season 1 games played:", played1)
print("Season 1 games won:", won1)
print("Percent won:", result1, "%")
print("Season 2 games played:", played2)
print("Season 2 games won:", won2)
print("Percent won:", result2, "%")
print("Season 3 games played:", played3)
print("Season 3 games won:", won3)
print("Percent won:", result3, "%")
print("Total games played:", total)
print("Total games won:", totalwon)
print("Total percent won:", totalper, "%")