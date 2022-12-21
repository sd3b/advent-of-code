enc = [(idx, int(x) * 811589153) for idx, x in enumerate(open("input.txt"))]

for round in range(10):
    for i in range(len(enc)):
        pos = [idx for idx, _ in enc].index(i)
        _, n = enc.pop(pos)
        enc.insert((pos + n) % len(enc), (i, n))

zero_idx = [x[1] for x in enc].index(0)
s = 0

for f in (1000, 2000, 3000):
    s += enc[(zero_idx + f) % len(enc)][1]

print(s)
