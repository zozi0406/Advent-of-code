with open("./Day1/input.txt",encoding="utf-8") as f:
    buffer = list()
    highest = 0
    for line in f.readlines():
        
        if line != "\n":
            buffer.append(line)
        else:
            floatbuffer=[float(item.rstrip("\n")) for item in buffer]
            floatbuffer=sum(floatbuffer)
            if highest<floatbuffer:
                highest=floatbuffer
            buffer=list()
    print(highest)

