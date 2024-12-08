l = []
r = []

for line in open("inputs/1.txt"):
    x, y = map(int, line.split())
    l.append(x)
    r.append(y)

l.sort()
r.sort()

print("Part A:", sum(abs(x - y) for x, y in zip(l, r)))
print("Part B:", sum(n * r.count(n) for n in l))
