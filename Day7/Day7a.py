from collections import Counter

cards = reversed(["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"])
card_values = {card: ind + 1 for ind, card in enumerate(cards)}


def find_type(hand):
    counts = Counter(list(hand))
    if counts.most_common(1)[0][1] == 5:
        return 7
    elif counts.most_common(1)[0][1] == 4:
        return 6
    elif counts.most_common(2)[0][1] == 3 and counts.most_common(2)[1][1] == 2:
        return 5
    elif counts.most_common(1)[0][1] == 3:
        return 4
    elif counts.most_common(2)[0][1] == 2 and counts.most_common(2)[1][1] == 2:
        return 3
    elif counts.most_common(1)[0][1] == 2:
        return 2
    else:
        return 1


with open("./Day7/input.txt", encoding="utf-8") as f:
    hands = list()

    for line in f.readlines():
        hand, bid = line.strip().split(" ")
        hands.append({"hand": hand, "bid": int(bid), "type": find_type(hand)})
    hands = sorted(
        hands,
        reverse=False,
        key=lambda hand: (
            hand["type"],
            *[card_values[hand["hand"][i]] for i in range(5)],
        ),
    )
    result = 0
    for rank, hand in enumerate(hands):
        result += hand["bid"] * (rank + 1)

    print(result)
