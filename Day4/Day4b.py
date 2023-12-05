import re

cards = dict()


class Card:
    card_number = 0
    winning_numbers = []
    your_numbers = []
    card_count = 1

    def __init__(self, cardnum, winnning_numbers, your_numbers):
        self.card_number = cardnum
        self.winning_numbers = winnning_numbers
        self.your_numbers = your_numbers
        self.card_count = 1

    def get_winners(self):
        matches = 0
        for number in self.winning_numbers:
            if number in self.your_numbers:
                matches += 1
        print("matches: " + str(matches))
        if matches > 0:
            for cardnum in range(self.card_number + 1, self.card_number + matches + 1):
                cards[cardnum].add_card(self.card_count)
        return self.card_count

    def add_card(self, number):
        self.card_count += number


with open("./Day4/input.txt", encoding="utf-8") as f:
    result = 0
    for line in f.readlines():
        cardnumber, numbers = line.split(": ")
        cardnumber = int(cardnumber[5:].strip())

        winningnumbers, yournumbers = numbers.strip().split(" | ")

        winningnumbers = winningnumbers.strip().split(" ")
        yournumbers = yournumbers.strip().split(" ")

        winningnumbers = [number for number in winningnumbers if number != ""]
        yournumbers = [number for number in yournumbers if number != ""]

        cards[cardnumber] = Card(cardnumber, winningnumbers, yournumbers)

    for card in cards.keys():
        cards_scratched = cards[card].get_winners()
        result += cards_scratched
        print(str(card) + ": " + str(cards_scratched))

    print(result)
