import numpy as np
from itertools import combinations
import networkx as nx


def find_shortest_path_length(G, coord1, coord2):
    return nx.shortest_path_length(G, coord1, coord2)


def map_to_id(x, gen):
    if x == 1:
        return next(gen)
    else:
        return 0


def id():
    value = 1
    while True:
        yield value
        value += 1


with open("./Day11/test.txt", encoding="utf-8") as f:
    lines = list()
    translator = {"#": 1, ".": 0}
    for line in f.readlines():
        linelist = list(line.strip())
        linelist = [translator[char] for char in linelist]
        lines.append(linelist)
    map_array = np.array(lines)
    expanded_map = map_array.copy()
    expanding_row_indexes = list()
    expanding_column_indexes = list()
    for dim in range(map_array.shape[0]):
        if np.sum(map_array[dim, :]) == 0:
            expanding_row_indexes.append(dim)
    for dim in range(map_array.shape[1]):
        if np.sum(map_array[:, dim]) == 0:
            expanding_column_indexes.append(dim)

    expanded_map = np.insert(map_array, expanding_row_indexes, 0, axis=0)
    expanded_map = np.insert(expanded_map, expanding_column_indexes, 0, axis=1)
    gen = id()
    expanded_map = np.vectorize(map_to_id)(expanded_map, gen)
    n_points = list(range(1, next(gen)))
    paths = list(combinations(n_points, 2))
    point_locs = {point: np.where(point == expanded_map) for point in n_points}
    point_locs = {point: (loc[0][0], loc[1][0]) for point, loc in point_locs.items()}
    G = nx.grid_2d_graph(*expanded_map.shape)
    results = list()
    for a, b in paths:
        results.append(find_shortest_path_length(G, point_locs[a], point_locs[b]))  # type: ignore
    print(np.sum(results))
    np.savetxt("Day11/Map.txt", map_array, fmt="%s")
    np.savetxt("Day11/Exp_Map.txt", expanded_map, fmt="%s")
