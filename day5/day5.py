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

print(part1())
