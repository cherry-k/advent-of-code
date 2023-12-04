# aoc202001.py

from aocd.models import Puzzle
import math

YEAR = 2023
DAY = 4

def parse(puzzle_input):
    return [[set(map(int, card_side.split()))
             for card_side in line.split(': ')[1].split(' | ')]
            for line in puzzle_input.split('\n')]

def part1(lines):
    card_points = 0
    for line in lines:
        card_points += int(math.pow(2, len(line[0] & line[1])-1))
    return card_points

def part2(lines):
    #store the current card index
    [line.insert(0, line_index+1) for line_index, line in enumerate(lines)]
    #store the number of occurrences in line[3]
    [line.append(1) for line in lines]
    for index, line in enumerate(lines):
        num_copied_cards = len(line[1] & line[2])
        for i in range(index+1, min(index+1+num_copied_cards, len(lines))):
            # number of occurrences doubles
            lines[i][3] += line[3]
    return sum([line[3] for line in lines])

if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    print(part1(lines))
    print(part2(lines))
