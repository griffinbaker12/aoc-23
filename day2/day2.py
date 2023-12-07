# Python code to read from 'input.txt'
file_path = 'input.txt'

input = []

with open(file_path, 'r') as file:
    input = file.read().strip().split('\n')

# max cubes per turn
valid_dict = {'RED': 12, 'GREEN': 13, 'BLUE':14}

def part1():
    valid = []
    i = 1
    for game in input:
        _g, turns = game.split(':')
        turns = turns.split(";")
        trimmed_turns = list(map(lambda x: x.strip(), turns))
        print(trimmed_turns)
        valid_round = True
        for turn in trimmed_turns:
            rounds = turn.split(",")
            trimmed_rounds = list(map(lambda x: x.strip(), rounds))
            print(trimmed_rounds, 'round')
            # number, colro = trimmed_rounds 
            for round in trimmed_rounds:
                num, color = round.split(" ")
                color = color.upper()
                if int(num) > valid_dict[color]:
                    valid_round = False
        if valid_round:
            valid.append(i)
        i += 1
    print(valid)
    return sum(valid)

print(part1())

def part2():
    valid = []
    i = 1
    for game in input:
        _g, turns = game.split(':')
        turns = turns.split(";")
        trimmed_turns = list(map(lambda x: x.strip(), turns))
        print(trimmed_turns)
        max = { 'red': 0, 'blue': 0, 'green': 0 }
        for turn in trimmed_turns:
            rounds = turn.split(",")
            trimmed_rounds = list(map(lambda x: x.strip(), rounds))
            print(trimmed_rounds, 'round')
            # number, colro = trimmed_rounds 
            for round in trimmed_rounds:
                num, color = round.split(" ")
                num = int(num)
                if num > max[color]:
                    max[color] = num
        valid.append((max['red'], max['blue'], max['green']))

    print(valid)

    return sum (a * b * c for (a, b, c) in valid)

print(part2())
