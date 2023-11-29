import pytest
import maxCalories
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return maxCalories.parse(puzzle_input)

# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    assert example1 == [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10000]]

def test_part1_example1(example1):
    assert maxCalories.part1(example1) == 24000

@pytest.mark.skip(reason="Not implemented")

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert maxCalories.part2(example1) == ...