import re

def count_slash(line):
    return line.count("/")

with open("./Day7/input.txt",encoding="utf-8") as f:
    cwd=""
    dircounts=dict()
    for line in f.readlines():
        line=line.rstrip("\n")
        if line.startswith("$ cd .."):
            index=-1
            letter=cwd[index]
            while not letter=="/": 
                index -= 1
                letter=cwd[index]
            cwd=cwd[0:index]
        elif line.startswith("$ cd"):
            m=re.match(r"\$ cd ([a-zA-Z0-9/]+).*",line)
            cwd=cwd+"/"+m.group(1)
            if not (cwd in list(dircounts.keys())):
                dircounts[cwd]=0
        elif re.match(r"^\d+.*",line):
            
            m=re.match(r"(\d+)\s.*",line)

            dircounts[cwd]+=int(m.group(1))
            
    result=0
    all_keys=list(dircounts.keys())
    dir_depths={key:count_slash(key) for key in all_keys}
    current_depth=max(dir_depths.values())
    while current_depth>2:
        for key in all_keys:
            if dir_depths[key]==current_depth:
                m=re.match(r"(.*)/[^/]+$",key)
                dircounts[m.group(1)]+=dircounts[key]
        current_depth-=1
    for key, item in dircounts.items():
        if item<100000:
            result +=item
    print(result)
