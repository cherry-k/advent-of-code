import pytest
import dicegames
import pathlib
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return dicegames.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == ['3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
                        '1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
                        '8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
                        '1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
                        '6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

def test_part1_example1(example1):
    assert dicegames.part1(example1) == 8

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert dicegames.part2(example1) == 2286