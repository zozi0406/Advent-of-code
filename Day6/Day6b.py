import numpy as np

races = [
    {"time": 62737565, "record": 644102312401023},
]


def speed(time):
    return time * 1


def distance(speed, timeleft):
    return speed * timeleft


for race in races:
    distances = [
        distance(speed(time), race["time"] - time) for time in range(race["time"])
    ]
    faster_time = [dist for dist in distances if dist > race["record"]]
    print(len(faster_time))
