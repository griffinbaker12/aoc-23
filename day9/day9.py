file_path = 'input.txt'

input = []

# the insight is that you only need to store the ranges, and not the values themselves
with open(file_path, 'r') as file:
    for line in file:
        input.append([int(x) for x in line.split()])

def are_all_zeros(arr):
    all_zeros = True
    for x in arr:
        if x is not 0:
            all_zeros = False
            break
    return all_zeros

final_numbers = []
for row in input:
    arr = row
    diff_arr = [arr]
    while True: 
        int_arr = []
        print(arr, 'the arr')
        for i, number in enumerate(arr):
            if i == len(arr) - 1:
                break   
            diff = arr[i+1] - arr[i]
            int_arr.append(diff)
        diff_arr.append(int_arr)
        arr = int_arr
        if are_all_zeros(arr):
            break
    diff_arr.reverse()
    acc = 0
    # 0000, 33333, 03691215
    # p2 is the same logic, but you subtract the first items
    for i, diff in enumerate(diff_arr):
        if i == len(diff_arr) - 1:
            break
        print(diff)
        acc = diff_arr[i+1][0] - acc
        print(acc, 'the acc is')
    final_numbers.append(acc)
print(sum(final_numbers))

# take the diff of the rows until the final row is all 0s, if there is a non-zero, then you need to do this again
