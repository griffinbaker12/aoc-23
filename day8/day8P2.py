import math
file_path = 'test.txt'

input = []
map = {'L': 0, 'R': 1}

# the insight is that you only need to store the ranges, and not the values themselves
with open(file_path, 'r') as file:
   input = file.read().strip().split('\n')

code, *steps = [x for x in input if x != '']
dir_map = {}
map = {'L': 0, 'R': 1}

start_keys = []

for i, step in enumerate(steps):
    k, partial_v = step.split(' = ')
    if i == 0:
        curr_key = k
    elif i == len(steps) - 1:
        end_key = k
    v = partial_v[1:-1].split(', ')
    dir_map[k] = v
    if k.endswith('A'):
        start_keys.append(k)

print(start_keys)

og_len = len(start_keys)

steps = []

step = 0
while True:
    l_or_r = step % len(code)
    new_keys = []
    go_again = False
    for key in start_keys:
        curr_key = dir_map[key][map[code[l_or_r]]] 
        if curr_key[-1] == "Z":
            steps.append(step+1)
        else:
            new_keys.append(curr_key)
    start_keys = new_keys
    step += 1
    print(steps, start_keys)
    if len(steps) == og_len:
        break
print(math.lcm(*steps))
