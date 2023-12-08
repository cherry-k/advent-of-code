import pytest
import foodproduction
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return foodproduction.parse(puzzle_input)

@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    assert example1 == [[[50, 98, 2], [52, 50, 48]], [[0, 15, 37], [37, 52, 2], [39, 0, 15]], [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]], [[88, 18, 7], [18, 25, 70]], [[45, 77, 23], [81, 45, 19], [68, 64, 13]], [[0, 69, 1], [1, 0, 69]], [[60, 56, 37], [56, 93, 4]]]

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    assert foodproduction.part1(example1[0], example1[1]) == 35

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert foodproduction.part2(example1[0], example1[1]) == 46