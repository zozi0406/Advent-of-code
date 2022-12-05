with open("./Day3/input.txt",encoding="utf-8") as f:
    result=0
    counter=0
    comps=list()
    for line in f.readlines():
        
        if counter==2:
            comps.append(set(line.rstrip("\n")))
            badge=comps[0].intersection(comps[1]).intersection(comps[2]).pop()
            print(badge)
            if ord(badge)<91:
                result +=(ord(badge)-64+26)
            else:
                result += (ord(badge)-96)
            counter=0
            comps=list()

            continue
        
        counter += 1
        comps.append(set(line.rstrip("\n")))

        
    
    
    print(result)
    