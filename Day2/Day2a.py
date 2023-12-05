import re


def parse_game(game_string):
    res = {"red": 0, "green": 0, "blue": 0}
    for draw in game_string.split(", "):
        m = re.match(r"(\d+) ([a-z]+)", draw.strip())
        if m:
            res[m.groups()[1]] = int(m.groups()[0])

    return res


with open("./Day2/input.txt", encoding="utf-8") as f:
    gamedata = dict()
    maxnumbers = {"red": 12, "green": 13, "blue": 14}
    for line in f.readlines():
        idstring, gamestring = line.split(": ")
        id = int(idstring[5:])
        gamedata[id] = [
            parse_game(setstring.strip())
            for setstring in gamestring.strip().split("; ")
        ]

    sum_possible = 0
    for ID, game in gamedata.items():
        possible = True
        for gameset in game:
            if (
                gameset["red"] > maxnumbers["red"]
                or gameset["green"] > maxnumbers["green"]
                or gameset["blue"] > maxnumbers["blue"]
            ):
                possible = False
                break
        if possible:
            sum_possible += ID

    print(sum_possible)
