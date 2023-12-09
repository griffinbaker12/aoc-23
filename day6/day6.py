file_path = 'input.txt'

input = []

# the insight is that you only need to store the ranges, and not the values themselves
with open(file_path, 'r') as file:
   input = file.read().strip().split('\n')

def part1():
    ways_to_win = 1
    [times, distances]  = [list(map(int, x.split()[1:])) for x in input]
    zipped = list(zip(times, distances))
    
    for race_duration, record_dist in zipped:
        winning_combos = 0
        for tick in range(1, race_duration + 1):
            if ((race_duration - tick) * tick) > record_dist:
                winning_combos += 1
        ways_to_win *= winning_combos

    return ways_to_win

# print(part1())

def part2():
    time, distance = [int("".join(w for w in l)) for l in [x.split()[1:] for x in input]]

    winning_combos = 0
    for tick in range(1, (time + 1) // 2):
        if ((time - tick) * tick) > distance:
            winning_combos += 2
    return winning_combos

print(part2())
