conv = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}

def snafu2dec(snafu: str):
    dec = 0

    for exp, char in enumerate(snafu):
        dec += conv[char] * 5 ** (len(snafu) - exp - 1)

    return dec

s = 0

for snafu in open("input.txt"):
    s += snafu2dec(snafu.strip())

rep = ""

while s:
    rep += "012=-"[s % 5]
    
    if s > 2:
        s += 2
    
    s //= 5

print(rep[::-1])
