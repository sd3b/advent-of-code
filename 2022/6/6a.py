marker_len = 4
line = open("input.txt").readline()

for idx in range(len(line)):
    marker = line[idx: idx + marker_len]

    if len(set(marker)) == marker_len:
        print(idx + marker_len)
        break