import pytest
import mirage_maintenance
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return mirage_maintenance.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == [[0,3,6,9,12,15],[1,3,6,10,15,21],[10,13,16,21,30,45]]

def test_part1_example1(example1):
    assert mirage_maintenance.part1(example1) == 114

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert mirage_maintenance.part2(example1) == ...