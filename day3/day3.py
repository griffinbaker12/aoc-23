file_path = 'input.txt'

input = []
visited = []

with open(file_path, 'r') as file:
    input = file.read().strip().split('\n')
    input = [list(row) for row in input]

HEIGHT = len(input)
WIDTH = len(input[0])

visited = [[False for _ in range(WIDTH)] for _ in range(HEIGHT)]

non_symbols = set(str(i) for i in range(10))
non_symbols.add(".")

def is_valid(y, x, grid):
    out_of_b = x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT
    if out_of_b:
        return False
    return is_symbol(grid[y][x])

def is_symbol(str):
    return str not in non_symbols

def is_surrounded_by_symbol(y, x, grid):
   # check all directions to see if it is valid   
   right = is_valid(y , x + 1, grid)
   diag_top_right = is_valid(y - 1 , x + 1, grid)
   diag_bottom_right = is_valid(y + 1 , x + 1, grid)

   left = is_valid(y, x - 1, grid)
   diag_top_left = is_valid(y - 1, x - 1, grid)
   diag_bottom_left = is_valid(y + 1, x - 1, grid)

   top = is_valid(y - 1, x, grid)

   bottom = is_valid(y + 1, x, grid)

   return right or left or top or bottom or diag_top_right or diag_bottom_right or diag_top_left or diag_bottom_left

def part1():    
    valid_digits = []
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if not visited[y][x] and input[y][x].isdigit():
                word_scan_x = x
                curr_part_num = ""
                has_seen_symbol = False
                while word_scan_x < WIDTH:
                    if input[y][word_scan_x] == "." or is_symbol(input[y][word_scan_x]):
                        break
                    visited[y][word_scan_x] = True
                    curr_part_num += input[y][word_scan_x]
                    surrounded_by_sym = is_surrounded_by_symbol(y, word_scan_x, input) 
                    if surrounded_by_sym:
                        has_seen_symbol = True
                    word_scan_x += 1
                if has_seen_symbol:
                    valid_digits.append(curr_part_num)
    return sum(int(x) for x in valid_digits)

# print(part1())

def add_gears(y, x, grid, gear_set):
    if y < 0 or x < 0 or y >= HEIGHT or x >= WIDTH:
        return
    if grid[y][x] == "*":
        gear_set.add((x, y))

def get_adj_gears(y, x, grid, gear_set):
   add_gears(y , x + 1, grid, gear_set)
   add_gears(y - 1 , x + 1, grid, gear_set)
   add_gears(y + 1 , x + 1, grid, gear_set)

   add_gears(y, x - 1, grid, gear_set)
   add_gears(y - 1, x - 1, grid, gear_set)
   add_gears(y + 1, x - 1, grid, gear_set)

   add_gears(y - 1, x, grid, gear_set)

   add_gears(y + 1, x, grid, gear_set)

   return gear_set

def part2():
    valid_digits = []
    gears = {}
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if not visited[y][x] and input[y][x].isdigit():
                word_scan_x = x
                curr_part_num = ""
                adj_gears = set()
                while word_scan_x < WIDTH:
                    if input[y][word_scan_x] == "." or is_symbol(input[y][word_scan_x]):
                        break
                    visited[y][word_scan_x] = True
                    curr_part_num += input[y][word_scan_x]

                    get_adj_gears(y, word_scan_x, input, adj_gears)

                    word_scan_x += 1

                for gear_coord in adj_gears:
                    if gear_coord in gears:
                        gears[gear_coord].append(curr_part_num)
                    else:
                        gears[gear_coord] = [curr_part_num]

    print(gears)

    acc = 0

    for gear in gears:
        gear_cs = gears[gear]
        if len(gear_cs) == 2:
            acc += int(gear_cs[0]) * int(gear_cs[1])

    return acc

print(part2())
