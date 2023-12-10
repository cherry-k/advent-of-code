import pytest
import boatrace
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return boatrace.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return boatrace.parse2(puzzle_input)

@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    assert example1 == [[7, 15, 30], [9, 40, 200]]

def test_parse_example2(example2):
    assert example2 == [71530, 940200]

def test_part1_example1(example1):
    assert boatrace.part1(example1) == 288

def test_part2_example1(example2):
    """Test part 2 on example input."""
    assert boatrace.part2(example2) == 71503