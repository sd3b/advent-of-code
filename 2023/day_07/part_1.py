from functools import cmp_to_key

def hand_type(hand: str) -> int:
    card_types = {char: hand.count(char) for char in set(hand)}

    return [
        [1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]
    ].index(
        sorted(card_types.values(), reverse = True)
    )

def same_type(hand_1: str, hand_2: str):
    card_strengths = "AKQJT98765432"

    for card_1, card_2 in zip(hand_1, hand_2):
        if card_1 == card_2:
            continue

        if card_strengths.index(card_1) < card_strengths.index(card_2):
            return 1
       
        return -1

    return 0

hands = []

def cmp(hand_1, hand_2):
    type_1 = hand_type(hand_1[0])
    type_2 = hand_type(hand_2[0])

    if type_1 == type_2:
        return same_type(hand_1[0], hand_2[0])

    return type_1 - type_2

for line in open("input.txt"):
    hand, bid = line.strip().split()
    hands.append([hand, int(bid)])

ranked_hands = sorted(hands, key = cmp_to_key(cmp))

print(sum((idx + 1) * bid for idx, (_, bid) in enumerate(ranked_hands)))
