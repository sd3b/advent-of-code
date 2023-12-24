patterns = [[line.strip() for line in p.split("\n")] for p in open("input.txt").read().strip().split("\n\n")]

def check_vertical_reflection(pattern, no_mismatch) -> int:
    WIDTH = len(pattern[0])

    for y in range(1, WIDTH):
        mismatch = 0
        left = [line[:y][::-1] for line in pattern]
        right = [line[y:] for line in pattern]

        for left_line, right_line in zip(left, right):
            for a, b in zip(left_line, right_line):
                if a != b:
                    mismatch += 1

        if mismatch == no_mismatch:
            return y

    return -1

def check_horizontal_reflection(pattern, no_mismatch) -> int:
    transposed = list(zip(*pattern))
    return check_vertical_reflection(transposed, no_mismatch)

def solve(no_mismatch):
    ans = 0

    for p in patterns:
        h = check_horizontal_reflection(p, no_mismatch)
        v = check_vertical_reflection(p, no_mismatch)

        if h != -1:
            ans += 100 * h
        elif v != -1:
            ans += v

    return ans

print("Part 1:", solve(0))
print("Part 2:", solve(1))
