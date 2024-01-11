file_path = 'test.txt'

input = []

def extrapolate(arr):
    if all(x == 0 for x in arr):
        return 0    

    deltas = [(y - x) for x, y in zip(arr, arr[1:])]
    diff = extrapolate(deltas)
    return arr[-1] + diff

total = 0

with open(file_path, 'r') as file:
    for line in file:
        arr = [int(x) for x in line.split()]
        total += extrapolate(arr)
    print(total)
