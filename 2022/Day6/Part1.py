with open("./Day6/input.txt",encoding="utf-8") as f:
    line = f.readline()
    line=line.rstrip("\n")
    first = True
    for pointer in range(len(line)-3):
        letters=set(line[pointer:pointer+4])
        if len(letters)==4 and first:
            print(pointer+4)
            first=False
