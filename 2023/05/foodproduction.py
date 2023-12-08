# aoc202001.py

from aocd.models import Puzzle

YEAR = 2023
DAY = 5


def parse(puzzle_input):
    groups = puzzle_input.split('\n\n')
    seeds = [int(seed) for seed in groups[0].split(':')[1].split()]
    maps = [group.split('\n') for group in groups[1:]]
    maps = [[[int(map_value) for map_value in line.split()] for line in elfmap[1:]] for elfmap in maps]
    return seeds, maps

def map_structure(elfmaps):
    for i,elfmap in enumerate(elfmaps):
        source_ranges = []
        for line in elfmap:
            source_ranges.append([line[1], line[1] + line[2], line[0]])
        source_ranges.sort()
        elfmaps[i] = source_ranges
    return elfmaps
def part1(seeds, maps):
    maps = map_structure(maps)
    items = seeds
    for elfmap in maps:
        for index, item in enumerate(items):
            for line in elfmap:
                if line[0] <= item < line[1]:
                    items[index] = line[2] + (item-line[0])
                    break
    return min(items)

def range_contains(element, start, stop, step=1):
    return start <= element < stop and (element - start) % step == 0

def part2(seeds, maps):
    maps = map_structure(maps)
    #group seeds into pairs
    item_ranges = list(zip(*[iter(seeds)] * 2))
    for elfmap in maps:
        for index, item_range in enumerate(item_ranges):
            for line in elfmap:
                if range_contains(item_range[0], line[0], line[1]):
                    if range_contains((item_range[0] + item_range[1]), line[0], line[1]):
                        item_ranges[index] = (line[2] + (item_range[0] - line[0]), item_range[1])
                        break
                    else:
                        # first part of the range is converted with this line of the map
                        # this means from item_range[0] to line[1]
                        start_conversion = item_range[0]
                        end_conversion = line[1]
                        item_ranges[index] = (line[2] + (start_conversion - line[0]), end_conversion - start_conversion)
                        # and append the rest of the range to the item ranges i guess...
                        leftover_range = (end_conversion, item_range[1]+item_range[0]-end_conversion)
                        item_ranges.append(leftover_range)
                        break
                if range_contains(item_range[1] + item_range[0], line[0], line[1]):
                    # second part of the range is converted with this line of the map
                    start_conversion = line[0]
                    end_conversion = item_range[1]+item_range[0]
                    item_ranges[index] = (line[2] + (start_conversion - line[0]), end_conversion - start_conversion)
                    # and append the rest of the range to the item ranges i guess...
                    leftover_range = (item_range[0], start_conversion - item_range[0] -1)
                    item_ranges.append(leftover_range)
                    break
        item_ranges.sort()
    return item_ranges[0][0]


if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle_input = puzzle.input_data
    seeds, maps = parse(puzzle_input)
    #print(part1(seeds, maps))
    print(part2(seeds, maps))
