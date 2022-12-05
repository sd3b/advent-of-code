import re

input_txt = open("input.txt").readlines()
regex = "(\[.\]|   ) ?" # capture either block of letters or the whitespace gap, with an optional space seperator
line = re.findall(regex, input_txt[0])
stacks = [[] for _ in range(len(line))]

line_no = 0

while line:
    line = re.findall(regex, input_txt[line_no])
    
    for idx, char in enumerate(line):
        if "[" in char:
            letter = char[1]
            stacks[idx].insert(0, letter)

    line_no += 1


for line in input_txt[line_no:]:
    n_to_move, src, dest = [int(x) for x in re.findall("move (\d+) from (\d+) to (\d+)", line)[0]]
    popped_crates = []

    for _ in range(n_to_move):
        popped_crates.append(stacks[src - 1].pop())

    stacks[dest - 1].extend(popped_crates[::-1])

    line_no += 1

for stack in stacks:
    print(stack.pop(), end = "")

print()
