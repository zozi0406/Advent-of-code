import numpy as np

races = [
    {"time": 62, "record": 644},
    {"time": 73, "record": 1023},
    {"time": 75, "record": 1240},
    {"time": 65, "record": 1023},
]


def speed(time):
    return time * 1


def distance(speed, timeleft):
    return speed * timeleft


results = []

for race in races:
    distances = [
        distance(speed(time), race["time"] - time) for time in range(race["time"])
    ]
    print(distances)
    faster_time = [dist for dist in distances if dist > race["record"]]
    results.append(len(faster_time))

print(results)
print(np.product(results))
