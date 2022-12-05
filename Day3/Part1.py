with open("./Day3/input.txt",encoding="utf-8") as f:
    result=0
    for line in f.readlines():
        
        n_items=len(line.rstrip("\n"))
        comp1=set(line[:(n_items//2)])
        comp2=set(line[(n_items//2):])
        common_item=comp1.intersection(comp2).pop()
        if ord(common_item)<91:
            result +=(ord(common_item)-64+26)
        else:
            result += (ord(common_item)-96)
        
    
    
    print(result)
    