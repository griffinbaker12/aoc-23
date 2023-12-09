file_path = 'input.txt'

input = []
visited = []

with open(file_path, 'r') as file:
    input = file.read().strip().split('\n')

def clean_row(row): 
    clean_nums, clean_your_nums = (
        [num.strip() for num in item.split()] for item in row.split(" | ")
    )
    winning_set = set(clean_nums[2:])

    return clean_your_nums, winning_set

def removeSpace(lst):
    return [x for x in lst if x != ""]

def part1():
    sums = []

    for row in input:
        clean_your_nums, winning_set = clean_row(row)
        
        matches = -1
        for num in clean_your_nums:
            if num in winning_set:
                matches += 1
        if matches >= 0:
            val = 2 ** matches
            sums.append(val)

    return sum(sums)
    
# print(part1())

# if you win, then you get more scratch cards below you
# each of the copies win additional scratch cards (so some multiplier?)

def part2():
    # include profiling to see how long it takes
    copies = {}

    for i, row in enumerate(input):
        clean_your_nums, winning_set = clean_row(row)

        cards_to_add = [x for x in clean_your_nums if x in winning_set]
        winning_len = len(cards_to_add)

        # add the current card
        if i + 1 in copies:
            copies[i + 1] += 1
        else:
            copies[i + 1] = 1

        if not winning_len:
            continue
        
        for n in range(i + 2, i + 2 + winning_len):
            # print(n, 'the winning numbers are for card', i + 1)
            if n in copies:
                copies[n] += (1 * copies[i + 1])
            else:
                copies[n] = (1 * copies[i + 1])

    return sum(x for x in copies.values())

print(part2())
