# import the advent of code puzzle
from aocd.models import Puzzle

# parse the puzzle input data
def parse(puzzle_input) :
    # split the string
    return puzzle_input.split()


 # combine the first digit and the last digit in each string to get the calibration values
def part1(strings):
    # for each string, find the first and last digit
    digit_strings=[]
    for string in strings:
        digit_string = ''
        digit_string += next((c for c in string if c.isdigit()), '0')
        digit_string += next((c for c in string[::-1] if c.isdigit()), '0')
        digit_strings.append(int(digit_string))
    return sum(digit_strings)

def part2(numbers):
    # calculate the sum total of each elf's calories, save in the list ElfCaloriesSum
    return numbers


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=1)
    puzzle_input = parse(puzzle.input_data)
    sumCalibrationValues = part1(puzzle_input)
    print(sumCalibrationValues)

