# import the advent of code puzzle
from aocd.models import Puzzle

# parse the puzzle input data
def parse(puzzle_input) :
    # split the string into a list inventoryLines
    lines=puzzle_input.split('\n')
    return lines

def part1(numbers):
    # create a nested list elfInventory in which each list corresponds to one elf's inventory entries
    elfInventory = [[]]
    elfIndex = 0
    # in inventoryLines, an empty line (just containing '\n') is the delimiter where another elf's entry begins
    for number in numbers:
        if number == '':
            elfIndex += 1
            elfInventory.append([])
        else:
            elfInventory[elfIndex].append(int(number))
    # calculate the sum total of each elf's calories, save in the list ElfCaloriesSum
    elfCaloriesSum = []
    for elfCalories in elfInventory:
        elfCaloriesSum.append(sum(elfCalories))
    print(elfCaloriesSum)
    # get the biggest entry in elfCaloriesSum, save in the variable maxElfCalories
    maxElfCalories = max(elfCaloriesSum)
    return(maxElfCalories)

if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=1)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    print (part1(lines))