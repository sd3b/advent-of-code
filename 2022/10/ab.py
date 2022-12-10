vals = []
register_x = 1

for line in open("input.txt"):
    if line.strip() == "noop":
        vals.append(register_x)
    else:
        vals.extend((register_x, register_x))
        register_x += int(line.strip().split()[1])

signal_sum = sum((vals[cycle - 1] * cycle for cycle in range(20, 221, 40)))
print("Part A:", signal_sum)
print("Part B:")

for y in range(6):
    line = ""

    for x in range(40):
        line += "##" if abs(x - vals[y * 40 + x]) <= 1 else '  '

    print(line)
