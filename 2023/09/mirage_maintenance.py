from aocd.models import Puzzle
YEAR = 2023
DAY = 9

def parse(puzzle_input):
    return [[int(e) for e in line.split()] for line in puzzle_input.split('\n')]


def fill_lines(line):
    lines = [line]
    while lines[-1] != [0]*len(lines[-1]):
        lines.append([])
        for idx in range(0, len(lines[-2])-1):
            lines[-1].append(lines[-2][idx+1]-lines[-2][idx])
    return lines
def extrapolate(line):
    filled_lines = fill_lines(line)
    # add a 0 to the last line
    filled_lines[-1].append(0)
    # reverse list
    filled_lines = list(reversed(filled_lines))
    # append (last element - last element of line above)
    for idx, line in enumerate(filled_lines[1:]):
        line.append(line[-1]+filled_lines[idx][-1])
    extrapolated_value = filled_lines[-1][-1]
    return extrapolated_value

def part1(lines):
    sum_extrapolated_values = 0
    for line in lines:
        sum_extrapolated_values += extrapolate(line)
    return sum_extrapolated_values

def part2(lines):
    ...
    return 0

if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    print(part1(lines))
    #print(part2(lines))
    