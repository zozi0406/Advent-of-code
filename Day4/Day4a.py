with open("./Day4/input.txt", encoding="utf-8") as f:
    result = 0

    for line in f.readlines():
        winningnumbers, yournumbers = line.split(": ")[1].strip().split(" | ")
        winningnumbers = winningnumbers.strip().split(" ")
        yournumbers = yournumbers.strip().split(" ")
        winningnumbers = [number for number in winningnumbers if number != ""]
        yournumbers = [number for number in yournumbers if number != ""]
        print(winningnumbers)
        print(yournumbers)
        matches = 0
        for number in winningnumbers:
            if number in yournumbers:
                matches += 1
        print(matches)
        if matches > 0:
            result += 2 ** (matches - 1)

    print(result)
