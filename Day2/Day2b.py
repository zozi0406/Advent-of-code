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
    for line in f.readlines():
        idstring, gamestring = line.split(": ")
        id = int(idstring[5:])
        gamedata[id] = [
            parse_game(setstring.strip())
            for setstring in gamestring.strip().split("; ")
        ]

    sum_power = 0
    for ID, game in gamedata.items():
        minnumbers = {"red": 0, "green": 0, "blue": 0}
        for gameset in game:
            minnumbers["red"] = max(minnumbers["red"], gameset["red"])
            minnumbers["green"] = max(minnumbers["green"], gameset["green"])
            minnumbers["blue"] = max(minnumbers["blue"], gameset["blue"])
        sum_power += minnumbers["red"] * minnumbers["green"] * minnumbers["blue"]

    print(sum_power)
