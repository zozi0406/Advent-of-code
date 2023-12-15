import numpy as np

coord_offsets = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "F": ((1, 0), (0, 1)),
    "J": ((0, -1), (-1, 0)),
    "7": ((0, -1), (1, 0)),
    "L": ((-1, 0), (0, 1)),
}


class Connection:
    conn_type = str()
    coord_offsets = tuple()
    coords = tuple()
    connected_coords = list()

    def __init__(self, char, coords):
        self.conn_type = char
        self.coords = coords
        if self.conn_type != "S":
            self.coord_offsets = coord_offsets[char]
            self.connected_coords = [
                (self.coords[0] + offset[0], self.coords[1] + offset[1])
                for offset in self.coord_offsets
            ]
        else:
            self.coord_offsets = [
                (x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) != (0, 0)
            ]
            self.connected_coords = [
                (self.coords[0] + offset[0], self.coords[1] + offset[1])
                for offset in self.coord_offsets
            ]

    def get_connected_coords(self):
        return self.connected_coords


with open("./Day10/input.txt", encoding="utf-8") as f:
    lines = list()
    for line in f.readlines():
        linelist = list(line.strip())
        lines.append(linelist)
    map_array = np.array(lines)
    start_coords = np.where(map_array == "S")
    start_coords = (start_coords[0][0], start_coords[1][0])
    start_symbol = Connection("S", start_coords)
    start_directions = start_symbol.get_connected_coords()
    start_dir_conns = [
        Connection(map_array[coords], coords)
        for coords in start_directions
        if map_array[coords] != "."
    ]
    start_connection = [
        adjacent
        for adjacent in start_dir_conns
        if start_coords in adjacent.get_connected_coords()
    ][0]

    current_coord = start_connection.coords
    current_conn = start_connection
    prev_coord = start_coords
    prev_conn = start_symbol
    Conn_path = [start_symbol]
    coord_path = [start_coords]
    while current_coord != start_coords:
        Conn_path.append(current_conn)

        coord_path.append(current_coord)  # type: ignore
        connected_coords = current_conn.get_connected_coords()

        for coords in connected_coords:
            if coords != prev_coord:
                prev_coord = current_coord
                prev_conn = current_conn
                current_conn = Connection(map_array[coords], coords)
                current_coord = coords
                break

    enclosed = list()
    new_map = np.full(shape=map_array.shape, fill_value=".", dtype=str)
    for conn in Conn_path:
        new_map[conn.coords] = conn.conn_type
    candidate1 = None
    candidate2 = None
    for index, current_coord in enumerate(coord_path):
        # prev_coord = coord_path[index - 1]
        next_coord = coord_path[(index + 1) % len(coord_path)]
        if next_coord[0] == current_coord[0]:
            if next_coord[1] - current_coord[1] > 0:
                candidate1 = (next_coord[0] - 1, next_coord[1])
                candidate2 = (next_coord[0] - 1, next_coord[1])
            else:
                candidate1 = (current_coord[0] + 1, current_coord[1])
                candidate2 = (next_coord[0] + 1, next_coord[1])
        elif next_coord[1] == current_coord[1]:
            if next_coord[0] - current_coord[0] > 0:
                candidate1 = (current_coord[0], current_coord[1] + 1)
                candidate2 = (next_coord[0], next_coord[1] + 1)
            else:
                candidate1 = (current_coord[0], current_coord[1] - 1)
                candidate2 = (next_coord[0], next_coord[1] - 1)
        if candidate1:
            if candidate1 not in enclosed and candidate1 not in coord_path:
                try:
                    enclosed.append(candidate1)
                    new_map[candidate1] = "I"
                except:
                    continue
        if candidate2:
            if candidate2 not in enclosed and candidate2 not in coord_path:
                try:
                    enclosed.append(candidate2)
                    new_map[candidate2] = "I"
                except:
                    continue
    prev_enclosed = None
    print(len(enclosed))
    while prev_enclosed != enclosed:
        prev_enclosed = enclosed.copy()
        for coords in enclosed:
            offsets = [
                (x, y)
                for x in [-1, 0, 1]
                for y in [-1, 0, 1]
                if (x, y) != (0, 0) and abs(x) + abs(y) < 2
            ]
            for offset in offsets:
                candidate = (offset[0] + coords[0], offset[1] + coords[1])
                if candidate not in enclosed and candidate not in coord_path:
                    enclosed.append(candidate)
                    new_map[candidate] = "I"
        print(len(enclosed))
    np.savetxt("Day10/Map.txt", new_map, fmt="%s")
