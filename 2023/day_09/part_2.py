def get_prev(seq: list) -> int:
    if all(n == 0 for n in seq):
        return 0

    diff_seq = [seq[idx + 1] - seq[idx] for idx in range(0, len(seq) - 1)]
    return seq[0] - get_prev(diff_seq)

s = 0

for line in open("input.txt"):
    seq = [int(x) for x in line.split()]
    s += get_prev(seq)

print("Part 2:", s)
