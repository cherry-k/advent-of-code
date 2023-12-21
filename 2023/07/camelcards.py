from operator import itemgetter

from aocd.models import Puzzle
import pathlib
from collections import defaultdict

YEAR = 2023
DAY = 7
PUZZLE_DIR = pathlib.Path(__file__).parent

CARD_LABELS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'T', 'J', 'Q', 'K', 'A']
CARD_VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
CARD_VALUES_JOKER = {'J':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'Q':11, 'K':12, 'A':13}



def parse(puzzle_input):
    return [line.split() for line in puzzle_input.split('\n')]

def check_full_house(hand):
    values = [i for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if sorted(value_counts.values()) == [2,3]:
        return True
    return False

def check_two_pairs(hand):
    values = [i for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if sorted(value_counts.values()) == [1,2,2]:
        return True
    return False

def count_equals(hand):
    values = [i for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    return max(value_counts.values())


def check_hand_type(hand):
    # hand values:
    # five of a kind: 7
    # four of a kind: 6
    # full house: 5
    # three of a kind: 4
    # two pairs: 3
    # one pair: 2
    # high card: 1
    if check_full_house(hand):
        return 5
    if check_two_pairs(hand):
        return 3
    else:
        equals = count_equals(hand)
        if equals > 3:
            return equals + 2
        if equals > 2:
            return equals + 1
        else:
            return equals

def check_full_house_joker(hand):
    values = [i for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    if 'J' not in value_counts.keys():
        if sorted(value_counts.values()) == [2,3]:
            return True
    if value_counts['J'] == 1:
        value_counts.pop('J')
        if sorted(value_counts.values()) == [2, 2]:
            return True
    return False

def check_two_pairs_joker(hand):
    values = [i for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 'J' not in value_counts.keys() and sorted(value_counts.values()) == [1,2,2]:
        return True
    return False

def count_equals_joker(hand):
    values = [i for i in hand]
    value_counts = defaultdict(lambda:0)
    for v in values:
        value_counts[v]+=1
    joker_count = value_counts['J']
    if joker_count > 3:
        return 5
    else:
        value_counts.pop('J')
        return max(value_counts.values())+joker_count

def check_hand_type_joker(hand):
    # hand values:
    # five of a kind: 7
    # four of a kind: 6
    # full house: 5
    # three of a kind: 4
    # two pairs: 3
    # one pair: 2
    # high card: 1
    if check_full_house_joker(hand):
        return 5
    if check_two_pairs_joker(hand):
        return 3
    else:
        equals = count_equals_joker(hand)
        if equals > 3:
            return equals + 2
        if equals > 2:
            return equals + 1
        else:
            return equals

def check_card_values(last_hand, this_hand):
    last_values = [CARD_VALUES_JOKER[i] for i in last_hand]
    this_values = [CARD_VALUES_JOKER[i] for i in this_hand]
    for i in range(0,len(last_values)):
        if last_values[i] > this_values[i]:
            return True
        if last_values[i] < this_values[i]:
            return False
    return False

def check_card_values_joker(last_hand, this_hand):
    last_values = [CARD_VALUES_JOKER[i] for i in last_hand]
    this_values = [CARD_VALUES_JOKER[i] for i in this_hand]
    for i in range(0,len(last_values)):
        if last_values[i] > this_values[i]:
            return True
        if last_values[i] < this_values[i]:
            return False
    return False

def check_greater(last_hand, this_hand):
    hand_types = defaultdict(lambda:0)
    hand_types[last_hand] = check_hand_type(last_hand)
    hand_types[this_hand] = check_hand_type(this_hand)
    if hand_types[last_hand] == hand_types[this_hand]:
        if check_card_values(last_hand, this_hand):
            return True
        else:
            return False
    else:
        if hand_types[last_hand] > hand_types[this_hand]:
            return True
        else:
            return False

def check_greater_joker(last_hand, this_hand):
    hand_types = defaultdict(lambda:0)
    hand_types[last_hand] = check_hand_type_joker(last_hand)
    hand_types[this_hand] = check_hand_type_joker(this_hand)
    if hand_types[last_hand] == hand_types[this_hand]:
        if check_card_values_joker(last_hand, this_hand):
            return True
        else:
            return False
    else:
        if hand_types[last_hand] > hand_types[this_hand]:
            return True
        else:
            return False

def swapPositions(lis, pos1, pos2):
    temp=lis[pos1]
    lis[pos1]=lis[pos2]
    lis[pos2]=temp
    return lis


def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if check_greater_joker(arr[j][0], arr[j + 1][0]):
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return
def part1(hands):
    n = len(hands)
    swapped = True
    while swapped:
        swapped = False
        for num in range(1, n):
            last_hand = hands[num-1][0]
            this_hand = hands[num][0]
            if check_greater(last_hand, this_hand):
                hands = swapPositions(hands, num-1, num)
                swapped = True
        n = n-1
    winnings = 0
    for hand in hands:
        winnings += (hands.index(hand)+1)*int(hand[1])
    return winnings
def part2(hands):
    bubbleSort(hands)
    winnings = 0
    for hand in hands:
        winnings += (hands.index(hand)+1)*int(hand[1])
    return winnings

if __name__ == "__main__":
    puzzle = Puzzle(year=YEAR, day=DAY)
    puzzle_input = puzzle.input_data
    lines = parse(puzzle_input)
    #print(part1(lines))
    print(part2(lines))
    