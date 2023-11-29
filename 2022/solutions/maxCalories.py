# import the advent of code puzzle
from aocd.models import Puzzle

# parse the puzzle input data
def parse(puzzle_input) :
    # split the string into a list of lines, then split every line into single numbers and convert them into an integer
    return [[int(lineNumber) for lineNumber in elfString.split('\n')] for elfString in puzzle_input.split('\n\n')]

def part1(numbers):
    # calculate the sum total of each elf's calories, save in the list ElfCaloriesSum
    elfCaloriesSum = [sum(e) for e in numbers]    # get the biggest entry in elfCaloriesSum, save in the variable maxElfCalories
    maxElfCalories = max(elfCaloriesSum)
    return(maxElfCalories)

def part2(numbers):
    # calculate the sum total of each elf's calories, save in the list ElfCaloriesSum
    elfCaloriesSum = [sum(e) for e in numbers]
    # sort the list
    elfCaloriesSum.sort(reverse=True)
    return sum(elfCaloriesSum[0:3])


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=1)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    print(part1(lines))
    print(part2(lines))
