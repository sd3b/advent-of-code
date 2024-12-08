part_a = 0

for line in open("inputs/7.txt"):
    target, vals = line.split(":")
    target = int(target)
    vals = list(map(int, vals.split()))

    for pos in range(2 ** (len(vals) - 1)):
        ans = vals[0]

        for val in vals[1:]:
            if pos & 1:
                ans *= val
            else:
                ans += val
            
            pos //= 2

        if ans == target:
            part_a += target
            break
        elif ans > target:
            continue

print("Part A:", part_a)
