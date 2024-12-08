from multiprocessing import Pool

def check(line):
    target, vals = line.split(":")
    target = int(target)
    vals = list(map(int, vals.split()))

    ans = vals[0]

    for pos in range(3 ** (len(vals) - 1)):
        ans = vals[0]

        for val in vals[1:]:
            idx = pos % 3

            if idx == 0:
                ans *= val
            elif idx == 1:
                ans += val
            else:
                ans = int(f"{ans}{val}")

            pos //= 3

        if ans == target:
            return target
        elif ans > target:
            continue

    return 0

with Pool() as p:
    part_b = sum(p.map(check, open("inputs/7.txt")))

print("Part B:", part_b)
