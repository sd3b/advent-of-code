values_total = 0

for line in open("input.txt"):
    value = ""

    for char in line:
        if char.isdigit():
            value += char

    values_total += int(value[0] + value[-1])

print("Part 1:", values_total)
