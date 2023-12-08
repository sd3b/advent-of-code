import re
from math import lcm

network = {}
current_nodes = []

with open("input.txt") as f:
    instructions = f.readline().strip()
    f.readline()

    for line in f:
        data = re.findall("(...) = \((...), (...)\)", line)
        node, *connected = data[0]
        network[node] = connected

        if node[-1] == "A":
            current_nodes.append(node)

steps = 0
current_instruction_idx = 0
cycle_lengths = [-1] * len(current_nodes)

while -1 in cycle_lengths:
    path = instructions[current_instruction_idx] == "R"

    for idx, current_node in enumerate(current_nodes):
        current_nodes[idx] = network[current_node][path]

        if current_nodes[idx][-1] == "Z" and cycle_lengths[idx] == -1:
            cycle_lengths[idx] = steps + 1

    steps += 1
    current_instruction_idx += 1
    current_instruction_idx %= len(instructions)

print(lcm(*cycle_lengths))
