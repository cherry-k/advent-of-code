# import the advent of code puzzle
from aocd.models import Puzzle
import re


def parse(puzzle_input):
    return puzzle_input.split('\n')


def has_special_characters(string):
    pat = re.compile('[@_!#$%^&*()<>=?/\|}{~:+-]')
    if pat.search(string):
        return True
    else:
        return False

def part1(lines):
    partNumbers = []
    for row, line in enumerate(lines):
        matches = re.finditer(r'\d+', line)
        for match in matches:
            number = match.group()
            s_rows = lines[max(row-1,0):min(row+2, len(lines))]
            searchstring = ''
            for s_row in s_rows:
                searchstring += s_row[max(match.start()-1,0):min(match.end()+1, len(line))]
            if has_special_characters(searchstring):
                partNumbers.append(int(number))
    return sum(partNumbers)

def part2(numbers):
    ...


if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=3)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    print(part1(lines))
    # print(part2(lines))
