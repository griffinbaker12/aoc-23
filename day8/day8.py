file_path = 'input.txt'

input = []
map = {'L': 0, 'R': 1}

# the insight is that you only need to store the ranges, and not the values themselves
with open(file_path, 'r') as file:
   input = file.read().strip().split('\n')

code, *steps = [x for x in input if x != '']
dir_map = {}

for i, step in enumerate(steps):
    k, partial_v = step.split(' = ')
    if i == 0:
        curr_key = k
    elif i == len(steps) - 1:
        end_key = k
    v = partial_v[1:-1].split(', ')
    dir_map[k] = v

curr_key = "AAA"
end_key = "ZZZ"

step = 0
while curr_key != end_key:
    l_or_r = step % len(code)
    curr_key = dir_map[curr_key][map[code[l_or_r]]] 
    step += 1
print(step)
