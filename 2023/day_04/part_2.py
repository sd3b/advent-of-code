import re

cards = []
cards_no = []

points = 0

for line in open("input.txt"):
    winning_nums, nums_on_card = (set(re.findall("\d+", nums)) for nums in line.split(":")[-1].split("|"))
    cards.append(len(winning_nums & nums_on_card))
    cards_no.append(1)

for idx, card in enumerate(cards):
    for card_copy_idx in range(idx + 1, idx + card + 1):
        cards_no[card_copy_idx] += cards_no[idx]

print("Part 2:", sum(cards_no))
