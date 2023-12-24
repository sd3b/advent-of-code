platform = [line.strip() for line in open("input.txt")]
HEIGHT, WIDTH = len(platform), len(platform[0])
slide_pos = [0] * WIDTH

load = 0

for y, line in enumerate(platform):
    for x, char in enumerate(line):
        if char == "#":
            slide_pos[x] = y + 1
        elif char == "O":
            y_slide = slide_pos[x]
            slide_pos[x] += 1
            load += (HEIGHT - y_slide)

print("Part 1:", load)
