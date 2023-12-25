import random
from collections import defaultdict, deque
from itertools import pairwise
from tqdm import tqdm

graph = defaultdict(set)
vertices = []

for line in open("input.txt"):
    src, *connected = line.split()
    src = src[:-1]
    graph[src].update(connected)
    vertices.append(src)

    for c in connected:
        graph[c].add(src)


def BFS(u, v):
    start = ([u],)
    queue = deque(start)
    visited = set()

    while queue:
        current_path = queue.popleft()
        if current_path[-1] == v:
            return current_path

        for n in graph[current_path[-1]]:
            if n not in visited:
                queue.append(current_path + [n])
                visited.add(n)

    return []


edge_freq = defaultdict(int)

for _ in tqdm(range(10000)):
    path = BFS(random.choice(vertices), random.choice(vertices))

    for src, dest in pairwise(path):
        edge = tuple(sorted((src, dest)))
        edge_freq[edge] += 1


def get_subgraph_size(start, wires_to_cut):
    stack = [start]
    visited = set()
    subgraph_nodes = 0

    while stack:
        current_node = stack.pop()

        for n in graph[current_node]:
            if n in visited:
                continue

            if (current_node, n) in wires_to_cut or (n, current_node) in wires_to_cut:
                continue

            stack.append(n)
            visited.add(n)
            subgraph_nodes += 1

    return subgraph_nodes


edge_freq = sorted(edge_freq.items(), key = lambda x: x[1])
wires_to_cut = [wire[0] for wire in edge_freq[-3:]]
group_1 = get_subgraph_size(wires_to_cut[0][0], wires_to_cut)
group_2 = get_subgraph_size(wires_to_cut[0][1], wires_to_cut)

print("Part 1:", group_1 * group_2)
