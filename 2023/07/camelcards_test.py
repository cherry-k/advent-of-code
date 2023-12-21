import pytest
import camelcards
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return camelcards.parse(puzzle_input)

@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    assert example1 == [['32T3K', '765'], ['T55J5', '684'], ['KK677', '28'], ['KTJJT', '220'], ['QQQJA', '483']]

def test_part1_example1(example1):
    assert camelcards.part1(example1) == 6440

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert camelcards.part2(example1) == ...