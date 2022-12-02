with open("./Day1/input.txt",encoding="utf-8") as f:
    buffer = list()
    elves_list = list()
    for line in f.readlines():
        
        if line != "\n":
            buffer.append(line)
        else:
            floatbuffer=[float(item.rstrip("\n")) for item in buffer]
            floatbuffer=sum(floatbuffer)
            elves_list.append(floatbuffer)
            buffer = list()
    elves_list.sort(reverse=True)
    print(sum(elves_list[:3]))

