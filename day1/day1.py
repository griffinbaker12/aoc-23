import re

# Python code to read from 'input.txt'
file_path = 'test.txt'

input = []

with open(file_path, 'r') as file:
    input = file.read().strip().split('\n')

def part1Naive():
    values = []
    for i in range(len(input)):
       val = input[i] 
       # go over all of the values and keep track of the first and last values you have seen
       first = None
       last = None
       for j in range(len(val)):
           strVal = val[j]
           if strVal.isdigit() and first == None:
               first = strVal
           if strVal.isdigit():
                last = strVal
       values.append((first, last))
    print(values)

    sum = 0

    for (x, y) in values:
        sum += int(x + y)

    print(sum)

# part1Naive()

def find_first_last_digit(str):
    found = re.findall(r'\d', str)
    first, last = found[0], found[-1]
    return first, last

def part1Improved():
    values = [find_first_last_digit(line) for line in input]    
    return sum(int(x + y) for (x, y) in values)

# print(part1Improved())

num_strs = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': "8", 'nine': '9'}

def part2Naive():
    values = []
    for i in range(len(input)):
       val = input[i] 
       # go over all of the values and keep track of the first and last values you have seen
       first = None
       last = None
       for c1 in range(len(val)):
           for c2 in range(len(val)):
               strVal = val[c1:c2 + 1]

               if (strVal.isdigit() or strVal in num_strs) and first == None:
                   if (strVal.isdigit()): 
                       first = strVal
                   else: 
                       first = num_strs[strVal]

               if (strVal.isdigit() or strVal in num_strs):
                   if (strVal.isdigit()): 
                       last = strVal
                   else: 
                       last = num_strs[strVal]
                
       values.append((first, last))

    sum = 0

    print(values)

    for (x, y) in values:
        sum += int(x + y)

    print(sum)

part2Naive()

# # not totally accurate
# def find_first_last_digit_with_word(s):
#     first, last = None, None
#     word = ""
#     for char in s:
#         # Append character to the word
#         word += char
#
#         print(word)
#
#         # Check if the word is a digit or in num_strs
#         if word.isdigit() or word in num_strs:
#             # Convert word to digit if it's in num_strs
#             digit = num_strs.get(word, word)
#
#             # Update first and last numbers
#             if first is None:
#                 first = digit
#             last = digit
#
#             # Reset the word
#             word = ""
#
#     print(first, last)
#
#     return first, last
#
#
# def part2Improved():
#     values = [find_first_last_digit_with_word(line) for line in input]
#     print(values)
#     return sum(int(x + y) for (x, y) in values if x and y)
#
# print(part2Improved(), 'part 2 improv')
