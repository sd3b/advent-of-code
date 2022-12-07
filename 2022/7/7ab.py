from collections import defaultdict as dd
import itertools

stack = []
fs = dd(lambda: 0)
max_size = 100000

for current_line in open("input.txt").readlines():
    current_line = current_line.strip().split()

    if current_line[1] == "cd":
        if (new_dir := current_line[-1]) == "..":
            stack.pop()
        elif new_dir == "/":
            stack = [""]
        else:
            stack.append(new_dir)
    elif current_line[0].isnumeric():
        size = int(current_line[0])

        for path in itertools.accumulate(stack):
            fs[path] += size

vals = fs.values()

print("Part A:", sum((s for s in vals if s <= max_size)))
print("Part B:", min((s for s in vals if s >= fs[""] - 40000000)))