import pytest
import haunted
import pathlib

PUZZLE_DIR = pathlib.Path(__file__).parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR/'example.txt').read_text().strip()
    return haunted.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR/'example2.txt').read_text().strip()
    return haunted.parse(puzzle_input)

def test_parse_example1(example1):
    assert example1 == ['RL', ['AAA = (BBB, CCC)', 'BBB = (DDD, EEE)', 'CCC = (ZZZ, GGG)', 'DDD = (DDD, DDD)',
                              'EEE = (EEE, EEE)', 'GGG = (GGG, GGG)', 'ZZZ = (ZZZ, ZZZ)']]

def test_part1_example1(example1):
    assert haunted.part1(example1) == 2

def test_part1_example2(example2):
    assert haunted.part1(example2) == 6

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert haunted.part2(example1) == ...