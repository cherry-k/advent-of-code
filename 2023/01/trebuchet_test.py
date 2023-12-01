import pytest
import trebuchet
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return trebuchet.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

@pytest.mark.skip(reason="Not implemented")

def test_part1_example1(example1):
    assert trebuchet.part1(example1) == [12, 38, 15, 77]

@pytest.mark.skip(reason="Not implemented")

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert trebuchet.part2(example1) == 45000