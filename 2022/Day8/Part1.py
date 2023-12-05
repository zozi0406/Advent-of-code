import numpy as np

with open("./Day8/input.txt",encoding="utf-8") as f:
    first=True
    for line in f.readlines():
        line=list(line.rstrip("\n"))
        line=",".join(line)
        
        if first:
            print(len(line))
            tree_array = np.fromstring(line, dtype=float, sep=',')
            first=False
        else:
            print(tree_array.shape)
            print(np.fromstring(line, dtype=float, sep=',').shape)
            tree_array = np.row_stack([tree_array,np.fromstring(line, dtype=float, sep=',')])
        print(line)
    first=True
    for row in tree_array:
        row = list(row)
        val=len(row)-3
        print(min(row[val]>row[0:val]) or min(row[val]>row[(val+1):-1]))
        rowmask=np.array([(min(row[val]>row[0:val]) or min(row[val]>row[(val+1):])) for val in range(1,len(row)-1)])
        
        rowmask= np.insert(rowmask, 0, True, axis=0)
        rowmask= np.insert(rowmask,rowmask.shape[0],True,axis=0)
        print(rowmask)
        print(rowmask.shape)
        if first:
            row_arrays=rowmask
            first=False
        else:
            row_arrays = np.row_stack([row_arrays,rowmask])
    
    first=True
    for row in tree_array.T:
            row = list(row)
            val=len(row)-3
            print(min(row[val]>row[0:val]) or min(row[val]>row[(val+1):-1]))
            rowmask=np.array([(min(row[val]>row[0:val]) or min(row[val]>row[(val+1):])) for val in range(1,len(row)-1)])
            
            rowmask= np.insert(rowmask, 0, True, axis=0)
            rowmask= np.insert(rowmask,rowmask.shape[0],True,axis=0)
            print(rowmask)
            print(rowmask.shape)
            if first:
                col_array=rowmask
                first=False
            else:
                col_array = np.row_stack([col_array,rowmask])
    
    combined=np.logical_or(row_arrays,col_array.T)
    print(np.sum(combined))
    print(combined.shape)