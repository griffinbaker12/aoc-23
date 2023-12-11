file_path = 'input.txt'

inputs = []

with open(file_path, 'r') as file:
    parsed = file.read().strip().split('\n')
    for l in parsed:
        hand, value = l.split()
        inputs.append((hand, int(value)))

cards = '-J23456789TQKA'

def key(item):
    hand, _ = item
    if hand == "JJJJJ":
        return (25, [1, 1, 1, 1, 1])
    mode = max([card for card in hand if card != "J"], key=hand.count)
    sub = hand.replace("J", mode)
    s = sum(sub.count(card) for card in sub)
    l = [cards.index(card) for card in hand]
    return (s, l)

inputs.sort(key=key)
print(sum([rank * value for rank, (hand, value) in enumerate(inputs, 1)]))
