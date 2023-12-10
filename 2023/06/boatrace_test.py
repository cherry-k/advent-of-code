import pytest
import boatrace
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return boatrace.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == [[7, 15, 30], [9, 40, 200]]

def test_part1_example1(example1):
    assert boatrace.part1(example1) == 288

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert boatrace.part2(example1) == ...