file_path = 'input.txt'

location = float('inf')

with open(file_path, 'r') as file:
    seeds, *blocks = file.read().strip().split('\n\n')
    seeds = list(map(int, seeds.split(": ")[1].split()))

    for block in blocks:
        # ranges you want to check against
        ranges = []
        
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        new = []

        for x in seeds:
            for a, b, c in ranges:
                if x in range(b, b + c):
                    new.append(x - b + a)
                    break
            else:
                new.append(x)

        seeds = new

    print(min(seeds))
