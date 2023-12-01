# import the advent of code puzzle
from aocd.models import Puzzle
import re

# parse the puzzle input data
def parse(puzzle_input) :
    # split the string
    return puzzle_input.split()

# replace first occurrence of 'one' with '1' etc
def find_first_number(string):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # check if string contains the number, if yes, return True, otherwise return False
    pat = re.compile('|'.join([re.escape(s) for s in numbers]))
    match = pat.search(string)
    if match is None:
        return -1
    else:
        #the corresponding number is the string modulo 9 because after 'nine' it starts with 1 again
        number = numbers.index(match.group())%9 +1
        return str(number)

def find_last_number(string):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # check if string contains the number, if yes, return True, otherwise return False
    pat = re.compile('|'.join([re.escape(s[::-1]) for s in numbers]))
    match = pat.search(string[::-1])
    if match is None:
        return -1
    else:
        #the corresponding number is the string modulo 9 because after 'nine' it starts with 1 again
        number = numbers.index(match.group()[::-1])%9+1
        return str(number)


 # combine the first digit and the last digit in each string to get the calibration values
 # return the sum of all calibration values
def part1(strings):
    # for each string, find the first and last digit
    digit_strings=[]
    for string in strings:
        digit_string = ''
        digit_string += next((c for c in string if c.isdigit()), '0')
        digit_string += next((c for c in string[::-1] if c.isdigit()), '0')
        digit_strings.append(int(digit_string))
    return sum(digit_strings)

 # combine the first digit and the last digit in each string to get the calibration values
 # return the sum of all calibration values
 # digits spelled as words ('one', 'two' etc.) also count
def part2(strings):
    # first, replace the digits spelled as words with digits
    digit_strings = []
    for string in strings:
        digit_string=''
        digit_string += find_first_number(string)
        digit_string += find_last_number(string)
        digit_strings.append(int(digit_string))
    return sum(digit_strings)


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=1)
    puzzle_input = parse(puzzle.input_data)
    sumCalibrationValues = part2(puzzle_input)
    print(sumCalibrationValues)

