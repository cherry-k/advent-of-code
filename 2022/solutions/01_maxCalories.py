# open the text file input
inventory = open('input','r')
# read contents into a list inventoryLines
inventoryLines = inventory.readlines()
# close the file again
inventory.close()
# create a nested list elfInventory in which each list corresponds to one elf's inventory entries
elfInventory = [[]]
elfIndex = 0
# in inventoryLines, an empty line (just containing '\n') is the delimiter where another elf's entry begins
for inventoryLine in inventoryLines:
    if inventoryLine == '\n':
        elfIndex += 1
        elfInventory.append([])
    else:
        elfInventory[elfIndex].append(int(inventoryLine.strip('\n')))
# calculate the sum total of each elf's calories, save in the list ElfCaloriesSum
elfCaloriesSum = []
for elfCalories in elfInventory:
    elfCaloriesSum.append(sum(elfCalories))
print(elfCaloriesSum)
# get the the biggest entry in elfCaloriesSum, save in the variable maxElfCalories
maxElfCalories = max(elfCaloriesSum)
print ('most calories carried by one elf is', maxElfCalories)