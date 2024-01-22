import math
from functools import reduce
from itertools import cycle
from aocd.models import Puzzle
from collections import defaultdict
import re
YEAR = 2023
DAY = 8

def parse(puzzle_input):
    return [puzzle_input.split('\n\n')[0], puzzle_input.split('\n\n')[1].split('\n')]

def lcm(numbers):
    return reduce(lambda x, y: x * y // math.gcd(x, y), numbers, 1)

def part1(lines):
    pattern = lines[0]
    nodes = defaultdict(lambda: 0)
    for line in lines[1]:
        nodes[line[0:3]] = [line[7:10], line[12:15]]
    dir_values = {'L': 0, 'R': 1}
    node_name = 'AAA'
    steps = 0
    for direction in cycle(pattern):
        node_name = nodes[node_name][dir_values[direction]]
        steps += 1
        if node_name == 'ZZZ':
            break
    return steps

def part2(lines):
    pattern = lines[0]
    nodes = defaultdict(lambda: 0)
    for line in lines[1]:
        nodes[line[0:3]] = [line[7:10], line[12:15]]
    dir_values = {'L': 0, 'R': 1}
    node_names = []
    for node_name in nodes.keys():
        if node_name[2] == 'A':
            node_names.append(node_name)
    steps = []
    for node_name in node_names:
        this_steps = 0
        for direction in cycle(pattern):
            node_name = nodes[node_name][dir_values[direction]]
            this_steps += 1
            if node_name[2] == 'Z':
                steps.append(this_steps)
                break
    return lcm(steps)

if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    #print(part1(lines))
    print(part2(lines))