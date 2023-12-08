import math

with open("./Day8/input.txt", encoding="utf-8") as f:
    first_line = True
    skip_line = True
    nodes = {}
    directions = ""
    for line in f.readlines():
        if first_line:
            directions = line.strip()
            first_line = False
            continue
        elif skip_line:
            skip_line = False
            continue

        node, paths = line.strip().split(" = ")
        nodes[node] = paths[1:-1].split(", ")
    starting_nodes = [node for node in list(nodes.keys()) if node.endswith("A")]
    counter = 0
    curr_nodes = starting_nodes
    print(curr_nodes)
    period_lengths = dict()
    points_complete = 0
    while not all(
        [node.endswith("Z") for node in curr_nodes]
    ) and points_complete != len(curr_nodes):
        letter = directions[counter % len(directions)]
        paths = [nodes[node] for node in curr_nodes]
        for index, node in enumerate(curr_nodes):
            if node.endswith("Z") and index not in list(period_lengths.keys()):
                period_lengths[index] = {
                    "first_Z": counter,
                    "directions_mod": counter % len(directions),
                }
                print(node)
            elif (
                node.endswith("Z")
                and "second_Z" not in list(period_lengths[index].keys())
                and period_lengths[index]["directions_mod"]
                == (counter % len(directions))
            ):
                period_lengths[index]["second_Z"] = counter
                period_lengths[index]["period_length"] = (
                    counter - period_lengths[index]["first_Z"]
                )
                print(node)
                print(counter)

                points_complete += 1
                print(points_complete)

        if points_complete == 6:
            break
        if letter == "L":
            curr_nodes = [path[0] for path in paths]
        elif letter == "R":
            curr_nodes = [path[1] for path in paths]
        counter += 1
    print(counter)

    period_lengths = list(period_lengths.values())
    print(period_lengths)
    for valdict in period_lengths:
        valdict["offset"] = -(
            (counter - valdict["second_Z"]) % valdict["period_length"]
        )
    print(period_lengths)
    least_common_multiple = math.lcm(
        *[period["period_length"] for period in period_lengths]
    )

    val = least_common_multiple
    prev_highest = 0
    while True:
        integer_solutions = 0
        for valdict in period_lengths:
            if ((val - valdict["offset"]) / valdict["period_length"]).is_integer():
                integer_solutions += 1
                if integer_solutions > prev_highest:
                    print(integer_solutions)
                    prev_highest = integer_solutions
                    print(val)
                    print((val - valdict["offset"]) / valdict["period_length"])
            else:
                break

        if integer_solutions == 6:
            print(val)
            break
        val -= 283

    print(val)

    # for index, valdict in enumerate(period_lengths):
    #     for index2, valdict2 in enumerate(period_lengths):
    #         if index != index2:
    #             print(f"GCD between {index} and {index2}: ")
    #             print(math.gcd(valdict["period_length"], valdict2["period_length"]))
