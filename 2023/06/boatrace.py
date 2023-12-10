# aoc202001.py

from aocd.models import Puzzle
import math

YEAR = 2023
DAY = 6


def parse(puzzle_input):
    return [[int(member) for member in line.split(':')[1].split()] for line in puzzle_input.split('\n')]

def parse2(puzzle_input):
    return [int(line.split(':')[1].replace(" ", "")) for line in puzzle_input.split('\n')]

def charge(milliseconds):
    speed = 0
    speed += milliseconds
    return speed

def get_charging_times(race_time, distance):
    charging_time_1 = (race_time + math.sqrt(math.pow(race_time, 2) - 4*distance))/2
    charging_time_2 = (race_time - math.sqrt(math.pow(race_time, 2) - 4*distance))/2

    charging_time_1 = math.floor(charging_time_1) if not charging_time_1.is_integer() else charging_time_1-1
    charging_time_2 = math.ceil(charging_time_2) if not charging_time_2.is_integer() else charging_time_2+1

    return 1 + charging_time_1 - charging_time_2
def part1(lines):
    times = lines[0]
    distances = lines[1]
    number_of_ways = []
    for race_time, distance in zip(times, distances):
        ways = get_charging_times(race_time, distance)
        number_of_ways.append(ways)
    return math.prod(number_of_ways)
    #return number_of_ways


def part2(lines):
    race_time = lines[0]
    distance = lines[1]
    return get_charging_times(race_time, distance)


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle_input = puzzle.input_data
    #lines = parse(puzzle_input)
    #print(part1(lines))
    print(part2(parse2(puzzle_input)))
