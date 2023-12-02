digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
total = 0

for line in open("input.txt"):
    idx = 0
    value = ""

    while idx < len(line):
        if line[idx].isdigit():
            value += line[idx]
            idx += 1
        else:
            old_idx = idx + 1
            current_str = ""

            while idx < len(line):
                current_str += line[idx]
                idx += 1

                if current_str in digits:
                    value += str(digits.index(current_str) + 1)
                    break

            idx = old_idx

    total += int(value[0] + value[-1])

print("Part 2:", total)