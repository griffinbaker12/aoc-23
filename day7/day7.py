file_path = 'input.txt'

input = []
hands_and_bids = []

rank = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}

def strength(hand):
    # part 1 sort

    counts = {}
    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    vals = list(counts.values())

    if 5 in vals:
        return 6
    elif 4 in vals:
        return 5
    elif 3 in vals:
        if 2 in vals:
            return 4
        else:
            return 3
    elif 2 in vals:
        if vals.count(2) == 2:
            return 2
        else:
            return 1
    else:
        return 0

def translate(hand):
    str = ""
    for c in hand:
        if c in rank:
            str += rank[c]
        else:
            str += c
    return str

# the insight is that you only need to store the ranges, and not the values themselves
with open(file_path, 'r') as file:
   input = file.read().strip().split('\n')

def part1():
    for line in input:
        hand, bid = line.split()
        hands_and_bids.append((hand, bid))

    hands_and_bids.sort(key = lambda hand_and_bid: (strength(hand_and_bid[0]), translate(hand_and_bid[0])))

    sum = 0
    for i, (hand, bid) in enumerate(hands_and_bids):
        sum += int(bid) * (i + 1)

    return sum
print(part1())
