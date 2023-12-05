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
    return {
        "source": source,
        "destination": destination,
        "maps": sorted(maps, key=lambda x: x["source_start"]),
    }


def process_map(source_stage, seeds, mappings):
    dest_stage = mappings["destination"]
    if source_stage != mappings["source"]:
        raise KeyError

    new_seeds = list()
    allfound = False
    for seedrange in seeds:
        for maprange in mappings["maps"]:
            if (
                seedrange["range_start"] >= maprange["source_start"]
                and seedrange["range_start"] + seedrange["range_length"] - 1
                < maprange["source_start"] + maprange["range_length"]
            ):
                offset = seedrange["range_start"] - maprange["source_start"]
                allfound = True
                new_seeds.append(
                    {
                        "range_start": maprange["destination_start"] + offset,
                        "range_length": seedrange["range_length"],
                    }
                )
                break
            elif (
                seedrange["range_start"] >= maprange["source_start"]
                and seedrange["range_start"]
                < maprange["source_start"] + maprange["range_length"]
            ):
                offset = seedrange["range_start"] - maprange["source_start"]
                new_seeds.append(
                    {
                        "range_start": maprange["destination_start"] + offset,
                        "range_length": maprange["range_length"] - offset,
                    }
                )
                seedrange = {
                    "range_start": seedrange["range_start"]
                    + maprange["range_length"]
                    - offset,
                    "range_length": seedrange["range_length"]
                    - (maprange["range_length"] - offset),
                }

        if not allfound:
            new_seeds.append(seedrange)

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
            seeds = sorted(
                [
                    {
                        "range_start": seeds[2 * i],
                        "range_length": seeds[2 * i + 1],
                    }
                    for i in range(len(seeds) // 2)
                ],
                key=lambda x: x["range_start"],
            )
            continue
        elif seedline:
            seedline = False
            continue

        if line == "\n":
            new_map = parse_map(map_buffer)
            maps[new_map["source"]] = new_map
            map_buffer = []
            current_stage, seeds = process_map(current_stage, seeds, new_map)
            print(f"Current stage: {current_stage} - {seeds}\n")
        else:
            map_buffer.append(line.strip())

    if seeds:
        print(sorted(seeds, key=lambda x: x["range_start"])[0])
