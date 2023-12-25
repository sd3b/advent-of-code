import numpy as np


def tilt(platform):
    slide_pos = [0] * platform.shape[1]
    new_platform = np.full_like(platform, ".")

    for y, line in enumerate(platform):
        for x, char in enumerate(line):
            if char == "#":
                slide_pos[x] = y + 1
                new_platform[y, x] = "#"
            elif char == "O":
                new_platform[slide_pos[x], x] = "O"
                slide_pos[x] += 1

    return new_platform


def calculate_load(platform):
    HEIGHT, WIDTH = platform.shape
    load = 0

    for y in range(HEIGHT):
        for x in range(WIDTH):
            if platform[y, x] == "O":
                load += HEIGHT - y

    return load

def cycle(platform):
    for _ in range(4):
        platform = tilt(platform)
        platform = np.rot90(platform, k = -1)

    return platform


platform = np.array([[char for char in line.strip()] for line in open("input.txt")])
visited = dict()
visited_list = []
CYCLES = 1000000

for idx in range(CYCLES):
    platform_state = platform.tobytes()

    if platform_state in visited:
        repeat_idx = visited[platform_state]
        final_idx = repeat_idx + (1000000000 - idx) % (idx - repeat_idx)
        print("Part 2:", calculate_load(visited_list[final_idx]))
        break

    visited[platform_state] = idx
    visited_list.append(platform)
    platform = cycle(platform)
