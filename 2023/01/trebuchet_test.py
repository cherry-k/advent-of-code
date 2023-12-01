import pytest
import trebuchet
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return trebuchet.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR/'example2.txt').read_text().strip()
    return trebuchet.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

def test_parse_example2(example2):
    assert example2 == ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

def test_part1_example1(example1):
    assert trebuchet.part1(example1) == 142

def test_part2_example1(example2):
    """Test part 2 on example input."""
    assert trebuchet.part2(example2) == 281