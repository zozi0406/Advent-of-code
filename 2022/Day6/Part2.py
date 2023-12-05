with open("./Day6/input.txt",encoding="utf-8") as f:
    line = f.readline()
    line=line.rstrip("\n")
    first = True
    for pointer in range(len(line)-13):
        letters=set(line[pointer:pointer+14])
        if len(letters)==14 and first:
            print(pointer+14)
            first=False
