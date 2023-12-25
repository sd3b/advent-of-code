import networkx as nx

graph = nx.Graph()

for line in open("input.txt"):
    src, *connected = line.split()
    graph.add_edges_from((src[:-1], c) for c in connected)

_, (group_1, group_2) = nx.stoer_wagner(graph)

print("Part 1:", len(group_1) * len(group_2))
