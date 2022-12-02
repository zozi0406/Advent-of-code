with open("./Day2/input.txt",encoding="utf-8") as f:
    score=0
    for line in f.readlines():
        partner=line[0]
        you=line[2]

        if partner == "A":
            if you == "X":
                score+=(0+3)
            elif you == "Y":
                score += (3+1)
            elif you == "Z":
                score += (6+2)
        elif partner == "B":
            if you == "X":
                score+=(0+1)
            elif you == "Y":
                score += (3+2)
            elif you == "Z":
                score += (6+3)
        elif partner == "C":
            if you == "X":
                score+=(0+2)
            elif you == "Y":
                score += (3+3)
            elif you == "Z":
                score += (6+1)
    print(score)




