import numpy as np


def parse_map(map_buffer):
    source = map_buffer[0].split("-")[0]
    destination = map_buffer[0].split("-")[2][:-5]
    maps = [
        {
            "destination_start": int(mapping.split(" ")[0]),
            "source_start": int(mapping.split(" ")[1]),
            "range_length": int(mapping.split(" ")[2]),
        }
        for mapping in map_buffer[1:]
    ]
    return {"source": source, "destination": destination, "maps": maps}


def process_map(source_stage, seeds, mappings):
    dest_stage = mappings["destination"]
    if source_stage != mappings["source"]:
        raise KeyError

    new_seeds = list()
    found = False
    for seed in seeds:
        for maprange in mappings["maps"]:
            if (
                seed >= maprange["source_start"]
                and seed < maprange["source_start"] + maprange["range_length"]
            ):
                offset = seed - maprange["source_start"]
                found = True
                new_seeds.append(maprange["destination_start"] + offset)
                break
        if not found:
            new_seeds.append(seed)

    return dest_stage, new_seeds


with open("./Day5/input.txt", encoding="utf-8") as f:
    maps = dict()
    map_buffer = list()
    seedline = True
    seeds = None
    current_stage = "seed"
    for line in f.readlines():
        if seedline and not seeds:
            seeds = [int(seed) for seed in line.split(": ")[1].split(" ")]
            print(seeds)
            continue
        elif seedline:
            seedline = False
            continue

        if line == "\n":
            new_map = parse_map(map_buffer)
            maps[new_map["source"]] = new_map
            map_buffer = []
            print(new_map)
            current_stage, seeds = process_map(current_stage, seeds, new_map)
            print(f"Current stage: {current_stage} - {seeds}")
        else:
            map_buffer.append(line.strip())
    print(np.min(seeds))
