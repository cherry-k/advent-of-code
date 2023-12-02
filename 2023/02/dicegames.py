# import the advent of code puzzle
from aocd.models import Puzzle
import numpy as np
import re

# parse the puzzle input data
def parse(puzzle_input) :
    # split the string into a list of games, then split every game into single draws
    #game_data = np.fromiter([[int(lineNumber) for lineNumber in elfString.split('\n')]
    #                         for elfString in puzzle_input.split('\n\n')])
    game_data = []
    for game in puzzle_input.split('\n'):
        #draws = re.split('; |, |\*|\n', game.split(': ')[1])
        draws = game.split(': ')[1]
        game_data.append(draws)
    return game_data

def isValid(game):
    blue_total = 14
    red_total = 12
    green_total = 13
    blue_dice = re.findall(r'(\d+) blue', game) if 'blue' in game else 0
    if sum([int(i) for i in blue_dice]) > blue_total:
        return False
    green_dice = re.findall(r'(\d+) green', game) if 'green' in game else 0
    if sum([int(i) for i in green_dice]) > green_total:
        return False
    red_dice = re.findall(r'(\d+) red', game) if 'red' in game else 0
    if sum([int(i) for i in red_dice]) > red_total:
        return False
    return True

def part1(game_data):
    valid_games = []
    for i, game in enumerate(game_data):
        if isValid(game[1:]):
            valid_games.append(i+1)
    return sum(valid_games)

def part2(game_data):
    # in each game, find out the maximum number of dice of each color
    game_powers = []
    for game in game_data:
        blue_dice = re.findall(r'(\d+) blue', game) if 'blue' in game else 0
        blue_max = max([int(i) for i in blue_dice])
        green_dice = re.findall(r'(\d+) green', game) if 'green' in game else 0
        green_max = max([int(i) for i in green_dice])
        red_dice = re.findall(r'(\d+) red', game) if 'red' in game else 0
        red_max = max([int(i) for i in red_dice])
        game_powers.append(blue_max*green_max*red_max)
    return sum(game_powers)

if __name__ == '__main__':
    puzzle = Puzzle(year=2023, day=2)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    #print(part1(lines))
    print(part2(lines))
