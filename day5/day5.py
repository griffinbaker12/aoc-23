file_path = 'test.txt'

location = float('inf')

# the insight is that you only need to store the ranges, and not the values themselves
with open(file_path, 'r') as file:
    seeds, *blocks = file.read().strip().split('\n\n')
    seeds = list(map(int, seeds.split(": ")[1].split()))

    seed_tuples = []

    for val in range(0, len(seeds), 2):
        seed_tuples.append((seeds[val], seeds[val] + seeds[val + 1]))

    print(seed_tuples)

    for block in blocks:
        # ranges you want to check against
        ranges = []
        
        for line in block.splitlines()[1:]:
            ranges.append(list(map(int, line.split())))

        new = []

        while len(seed_tuples) > 0:
            s, e = seed_tuples.pop()
            print('start', s, 'end', e)
            for a, b, c in ranges:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os + a - b, oe + a - b))
                    if os > s:
                        seed_tuples.append((s, os))
                    if e > oe:
                        seed_tuples.append((oe, e))
                    break
            else:
                new.append((s, e))

        seed_tuples = new
    
    print(sorted(seed_tuples),  'the tuples are')
