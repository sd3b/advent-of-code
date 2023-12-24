def HASH(string):
    hash_value = 0

    for char in string:
        hash_value += ord(char)
        hash_value *= 17
        hash_value %= 256

    return hash_value

print("Part 1:", sum(HASH(step) for step in open("input.txt").readline().split(",")))
