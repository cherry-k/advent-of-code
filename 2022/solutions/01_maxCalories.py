# import the advent of code puzzle
from aocd.models import Puzzle
puzzle = Puzzle(year=2022, day=1)
# open the puzzle input data
inventory = puzzle.input_data
# split the string into a list inventoryLines
inventoryLines = inventory.split('\n')
# create a nested list elfInventory in which each list corresponds to one elf's inventory entries
elfInventory = [[]]
elfIndex = 0
# in inventoryLines, an empty line (just containing '\n') is the delimiter where another elf's entry begins
for inventoryLine in inventoryLines:
    if inventoryLine == '':
        elfIndex += 1
        elfInventory.append([])
    else:
        elfInventory[elfIndex].append(int(inventoryLine))
# calculate the sum total of each elf's calories, save in the list ElfCaloriesSum
elfCaloriesSum = []
for elfCalories in elfInventory:
    elfCaloriesSum.append(sum(elfCalories))
print(elfCaloriesSum)
# get the biggest entry in elfCaloriesSum, save in the variable maxElfCalories
maxElfCalories = max(elfCaloriesSum)
print('most calories carried by one elf is', maxElfCalories)
