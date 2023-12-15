from joblib import Parallel, delayed
import numpy as np
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt


def find_shortest_path_length(G, coord1, coord2):
    return nx.shortest_path_length(G, coord1, coord2, weight="weight")


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
    expanding_row_indexes = list()
    expanding_column_indexes = list()
    for dim in range(map_array.shape[0]):
        if np.sum(map_array[dim, :]) == 0:
            expanding_row_indexes.append(dim)
    for dim in range(map_array.shape[1]):
        if np.sum(map_array[:, dim]) == 0:
            expanding_column_indexes.append(dim)

    gen = id()
    map_array = np.vectorize(map_to_id)(map_array, gen)
    n_points = list(range(1, next(gen)))
    paths = list(combinations(n_points, 2))
    point_locs = {point: np.where(point == map_array) for point in n_points}
    point_locs = {point: (loc[0][0], loc[1][0]) for point, loc in point_locs.items()}
    G = nx.grid_2d_graph(*map_array.shape)
    expansion_level = 100

    for row in expanding_row_indexes:
        for col in range(map_array.shape[1]):
            G[(row, col)][(row + 1, col)]["weight"] = expansion_level
    for col in expanding_column_indexes:
        for row in range(map_array.shape[0]):
            G[(row, col)][(row, col + 1)]["weight"] = expansion_level

    results = list()
    results = Parallel(n_jobs=2)(
        delayed(find_shortest_path_length)(G, point_locs[a], point_locs[b])
        for a, b in paths
    )

    # for a, b in paths:
    #     results.append(find_shortest_path_length(G, point_locs[a], point_locs[b]))  # type: ignore
    if results:
        print(np.sum(results))
    np.savetxt("Day11/Map.txt", map_array, fmt="%s")

    # pos = {(x, y): (y, -x) for x, y in G.nodes()}
    # nx.draw(G, pos=pos, node_color="lightgreen", with_labels=True, node_size=600)
    # labels = nx.get_edge_attributes(G, "weight")
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    # plt.show()
