import pytest
import scratchcards
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return scratchcards.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == [[{41, 48, 17, 83, 86}, {6, 9, 48, 17, 83, 53, 86, 31}], [{32, 13, 16, 20, 61}, {32, 68, 17, 82, 19, 24, 61, 30}],
     [{1, 44, 53, 21, 59}, {1, 69, 72, 14, 16, 82, 21, 63}], [{69, 73, 41, 84, 92}, {5, 76, 51, 84, 83, 54, 58, 59}],
     [{32, 83, 87, 26, 28}, {36, 70, 12, 82, 22, 88, 93, 30}], [{72, 13, 18, 56, 31}, {35, 67, 36, 74, 10, 11, 77, 23}]]

def test_part1_example1(example1):
    assert scratchcards.part1(example1) == 13

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert scratchcards.part2(example1) == 30