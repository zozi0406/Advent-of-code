with open("./Day2/input.txt",encoding="utf-8") as f:
    score=0
    for line in f.readlines():
        partner=line[0]
        you=line[2]

        if partner == "A":
            if you == "X":
                score+=(1+3)
            elif you == "Y":
                score += (2+6)
            elif you == "Z":
                score += (3+0)
        elif partner == "B":
            if you == "X":
                score+=(1+0)
            elif you == "Y":
                score += (2+3)
            elif you == "Z":
                score += (3+6)
        elif partner == "C":
            if you == "X":
                score+=(1+6)
            elif you == "Y":
                score += (2+0)
            elif you == "Z":
                score += (3+3)
    print(score)




