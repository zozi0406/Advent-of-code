import numpy as np

with open("./Day8/input.txt",encoding="utf-8") as f:
    first=True
    for line in f.readlines():
        line=list(line.rstrip("\n"))
        line=",".join(line)
        
        if first:

            tree_array = np.fromstring(line, dtype=float, sep=',')
            first=False
        else:

            tree_array = np.row_stack([tree_array,np.fromstring(line, dtype=float, sep=',')])

    scores=np.zeros((99,99))
    for row_index in range(99):
        for column_index in range(99):
            #Up_score
            up_score=0
            if row_index!=0:
                for tree_above in range(row_index-1,-1,-1):
                    if tree_array[row_index,column_index]>tree_array[tree_above,column_index]:
                        up_score+=1
                    elif tree_array[row_index,column_index]==tree_array[tree_above,column_index]:
                        up_score+=1
                        break
            #Down_score
            down_score=0
            if row_index!=98:
                for tree_below in range(row_index+1,99,1):
                    if tree_array[row_index,column_index]>tree_array[tree_below,column_index]:
                        down_score+=1
                    elif tree_array[row_index,column_index]==tree_array[tree_below,column_index]:
                        down_score+=1
                        break
            #Left_score
            left_score=0
            if column_index!=0:
                for tree_left in range(column_index-1,-1,-1):
                    if tree_array[row_index,column_index]>tree_array[row_index,tree_left]:
                        left_score+=1
                    elif tree_array[row_index,column_index]==tree_array[row_index,tree_left]:
                        left_score+=1
                        break
            #Right_score
            right_score=0
            if column_index!=98:
                for tree_right in range(column_index+1,99,1):
                    if tree_array[row_index,column_index]>tree_array[row_index,tree_right]:
                        right_score+=1
                    elif tree_array[row_index,column_index]==tree_array[row_index,tree_right]:
                        right_score+=1
                        break
            scores[row_index,column_index]=up_score*down_score*left_score*right_score
    print(np.max(scores))    
    
