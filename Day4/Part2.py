with open("./Day4/input.txt",encoding="utf-8") as f:
    result = 0
    for line in f.readlines():
        elf1,elf2=line.split(",")
        elf1_low,elf1_high=elf1.split("-")
        elf2_low,elf2_high=elf2.split("-")
        elf1_range=set(range(int(elf1_low),int(elf1_high)+1))
        elf2_range=set(range(int(elf2_low),int(elf2_high)+1))
        if not elf1_range.isdisjoint(elf2_range): 
            result +=1
    print(result)