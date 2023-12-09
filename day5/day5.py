file_path = 'test.txt'

location = float('inf')

input = []

# the insight is that you only need to store the ranges, and not the values themselves
with open(file_path, 'r') as file:
   input = file.read().strip().split('\n\n')

# you have an array of seeds, and then you need to apply a collections of transformations on these seeds
def part1():
    # you want seeds to be an arr of numbers
    seeds = list(map(int, input[0].split(": ")[1].split()))
    blocks = input[1:]

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            x = list(map(int, line.split()))
            ranges.append(x)
        
        new = []
        
        # apply the transformations to the seed
        for seed in seeds:
            for a, b, c in ranges:
                if b <= seed < b + c:
                    new.append(seed + a - b)
                    break
            # only runs if we do not break
            else:
                new.append(seed)
        
        # seeds are now equal to their transformed values
        seeds = new

    return min(seeds)

# print(part1())

# instead of transforming the values, you tranform the range
def part2():
    # you want seeds to be a tuple of (s, e)
    seeds = list(map(int, input[0].split(": ")[1].split()))
    seed_ranges = []

    for i in range(0, len(seeds), 2):
        seed_ranges.append((seeds[i], seeds[i] + seeds[i + 1]))
    
    blocks = input[1:]

    for block in blocks:
        ranges = []
        for line in block.splitlines()[1:]:
            x = list(map(int, line.split()))
            ranges.append(x)
        
        new = []

        while len(seed_ranges) > 0:
            s, e = seed_ranges.pop()
            for a, b, c in ranges:
                os = max(b, s)
                oe = min(e, b + c)
                # if there is an overlap
                if os < oe:
                    # apply transformation to the range
                    new.append((os - b + a, oe - b + a))
                    # check if other parts of seed range can be applied elsewhere
                    if s < os:
                        seed_ranges.append((s, os))
                    if e > oe:
                        seed_ranges.append((e, oe))
                    break
            else:
                new.append((s, e))

        # seeds are now equal to their transformed values
        seed_ranges = new
    
    return sorted(seed_ranges)[0][0]

print(part2())
