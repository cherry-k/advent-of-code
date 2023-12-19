#from aocd.models import Puzzle
import pathlib
YEAR = 2023
DAY = 3
PUZZLE_DIR = pathlib.Path(__file__).parent

CARD_LABELS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'T', 'J', 'Q', 'K', 'A']


def parse(puzzle_input):
    return [line.split() for line in puzzle_input.split('\n')]

def sort_by_label(hands, labelcounts):
    sorted_hands = []
    while len(hands) > 0:
        if len(hands) == 1:
            sorted_hands.append(hands[0])
            hands.pop(0)
            labelcounts.pop(0)
        else:
            #add the indices and check for highest sum
            sum_indices = [sum([(i+1)*num for i, num in enumerate(labelcount) if num >0]) for labelcount in labelcounts]
            index_hand = sum_indices.index(max(sum_indices))
            sorted_hands.append(hands[index_hand])
            hands.pop(index_hand)
            labelcounts.pop(index_hand)
            print(hands)
    return sorted_hands

def sort_by_type(hands, winning_hands, of_a_kind):
    # first, find out how often each card type appears
    if not hands:
        return winning_hands
    label_occurrence_per_hand = [[] for k in hands]
    # how often does each card type occur per hand?
    for card_label in CARD_LABELS:
        for index, line in enumerate(hands):
            label_occurrence_per_hand[index].append(line[0].count(card_label))
    count_of_a_kind = [hand.count(of_a_kind) for hand in label_occurrence_per_hand]
    if count_of_a_kind == [0 for k in hands]:
        of_a_kind -= 1
        sort_by_type(hands, winning_hands, of_a_kind)
    labelcounts_with_type = []
    if of_a_kind == 3:
        hands_with_type = []
        labelcounts_with_type = []
    # if there is three equals, we have to check for full house
        for index_hand, count in enumerate(count_of_a_kind):
            count_of_2 = [hand.count(2) for hand in label_occurrence_per_hand]
            if count_of_2[index_hand] == 1 and count == 1:
                print("Hand", hands[index_hand], "has a full house")
                #add it to the hands to be sorted in next step
                hands_with_type.append(hands[index_hand])
                labelcounts_with_type.append(label_occurrence_per_hand[index_hand])
                #remove it from the hands
                hands.pop(index_hand)
        if hands_with_type:
            sorted_hands = sort_by_label(hands_with_type, labelcounts_with_type)
            winning_hands.extend(sorted_hands)
            sort_by_type(hands, winning_hands, of_a_kind)
    if of_a_kind == 2:
        hands_with_type = []
        labelcounts_with_type = []
    # if there is two of a kind, we have to check for two pairs
        for index_hand, count in enumerate(count_of_a_kind):
            if count == 2:
                print("Hand", hands[index_hand], "has two pairs")
                hands_with_type.append(hands[index_hand])
                labelcounts_with_type.append(label_occurrence_per_hand[index_hand])
                #remove it from the hands
        if hands_with_type:
            sorted_hands = sort_by_label(hands_with_type, labelcounts_with_type)
            winning_hands.extend(sorted_hands)
            for hand in sorted_hands:
                hands.remove(hand)
            sort_by_type(hands, winning_hands, of_a_kind)
    hands_with_type = []
    labelcounts_with_type = []

    for index_hand, count in enumerate(count_of_a_kind):
        if count > 0 and hands[index_hand] not in winning_hands:
            print("Hand", hands[index_hand], "has ", of_a_kind, " of a kind")
            hands_with_type.append(hands[index_hand])
            labelcounts_with_type.append(label_occurrence_per_hand[index_hand])
    if hands_with_type:
        sorted_hands = sort_by_label(hands_with_type, labelcounts_with_type)
        winning_hands.extend(sorted_hands)
        of_a_kind -= 1
        for hand in sorted_hands:
            hands.remove(hand)
        sort_by_type(hands, winning_hands, of_a_kind)

def part1(lines):
    winning_hands = []
    winning_hands = sort_by_type(lines, winning_hands, 5)
    return 0

def part2(lines):
    ...
    return 0

if __name__ == "__main__":
    #puzzle = Puzzle(year=YEAR, day=DAY)
    #puzzle_input = puzzle.input_data
    puzzle_input = (PUZZLE_DIR / 'example.txt').read_text().strip()
    lines = parse(puzzle_input)
    print(part1(lines))
    #print(part2(lines))
    