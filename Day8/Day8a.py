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
    curr_node = "AAA"
    counter = 0
    while curr_node != "ZZZ":
        letter = directions[counter % len(directions)]
        paths = nodes[curr_node]
        if letter == "L":
            curr_node = paths[0]
        elif letter == "R":
            curr_node = paths[1]
        counter += 1
        print(counter)
