import re

network = {}

with open("input.txt") as f:
    instructions = f.readline().strip()
    f.readline()

    for line in f:
        data = re.findall("(...) = \((...), (...)\)", line)
        node, *connected = data[0]
        network[node] = connected

steps = 0
current_instruction_idx = 0
current_node = "AAA"

while current_node != "ZZZ":
    idx = instructions[current_instruction_idx] == "R"
    current_node = network[current_node][idx]

    steps += 1
    current_instruction_idx += 1
    current_instruction_idx %= len(instructions)

print(steps)
