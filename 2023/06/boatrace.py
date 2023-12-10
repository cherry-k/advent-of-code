# aoc202001.py

from aocd.models import Puzzle
import math

YEAR = 2023
DAY = 6


def parse(puzzle_input):
    return [[int(member) for member in line.split(':')[1].split()] for line in puzzle_input.split('\n')]

def charge(milliseconds):
    speed = 0
    speed += milliseconds
    return speed

def part1(lines):
    times = lines[0]
    distances = lines[1]
    number_of_ways = []
    for time, distance in zip(times, distances):
        charging_times = range(1, time-1, 1)
        my_distances = [(time - charging_time) * charging_time for charging_time in charging_times]
        number_of_ways.append(sum(i > distance for i in my_distances))
    return math.prod(number_of_ways)


def part2(lines):
    ...
    return 0


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    print(part1(lines))
    print(part2(lines))
