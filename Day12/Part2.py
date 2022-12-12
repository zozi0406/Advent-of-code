import numpy as np
import networkx as nx
import pandas as pd
with open("./Day12/input.txt",encoding="utf-8") as f:
    first = True
    row_counter=0
    for line in f.readlines():
        line=line.rstrip("\n")
        encoded_line=list()
        col_counter=0
        for letter in line:
            if letter == "S":
                encoded_line.append(1)
                start=(row_counter,col_counter)
            elif letter == "E":
                encoded_line.append(26)
                end=(row_counter,col_counter)
            else:
                encoded_line.append(ord(letter)-96)
            col_counter+=1
        encoded_line=np.array(list(encoded_line))
        if first:
            map_arr=encoded_line
            first=False
        else:
            map_arr=np.row_stack([map_arr,encoded_line])
        row_counter+=1
    padded_arr=np.pad(map_arr,(1,1),"constant",constant_values=9999)
    print(padded_arr)
    G=nx.DiGraph()
    node_id=0
    Graph_dict=pd.DataFrame(columns=["Node_id","X","Y"])
    Graph_elevation=pd.DataFrame(columns=["Node_id","Elevation"])
    for row_index in range(map_arr.shape[0]):
        for col_index in range(map_arr.shape[1]):
            G.add_node(node_id)
            df_row=[node_id,row_index,col_index]
            Graph_dict.loc[len(Graph_dict)]=df_row
            Graph_elevation.loc[len(Graph_elevation)]=[node_id,map_arr[row_index,col_index]]
            node_id += 1
            


    for row_index in range(1,padded_arr.shape[0]-1):
        for col_index in range(1,padded_arr.shape[1]-1):
            row_start=max(0,row_index-1)
            row_end=min(row_index+2,padded_arr.shape[0])
            col_start=max(0,col_index-1)
            col_end=min(col_index+2,padded_arr.shape[1])
            subarray=padded_arr[row_start:row_end,col_start:col_end]
            orig_row_index=row_index-1
            orig_col_index=col_index-1
            root_val=subarray[1,1]
            root_node_id=Graph_dict.loc[(Graph_dict["X"]==orig_row_index) & (Graph_dict["Y"]==orig_col_index),"Node_id"].iloc[0]
            
            if subarray[0,1]-root_val<=1:
                dest_node=Graph_dict.loc[(Graph_dict["X"]==orig_row_index-1) & (Graph_dict["Y"]==orig_col_index),"Node_id"].iloc[0]
                G.add_edge(root_node_id,dest_node)
            if subarray[1,0]-root_val<=1:
                dest_node=Graph_dict.loc[(Graph_dict["X"]==orig_row_index) & (Graph_dict["Y"]==orig_col_index-1),"Node_id"].iloc[0]
                G.add_edge(root_node_id,dest_node)
            if subarray[1,2]-root_val<=1:
                dest_node=Graph_dict.loc[(Graph_dict["X"]==orig_row_index) & (Graph_dict["Y"]==orig_col_index+1),"Node_id"].iloc[0]
                G.add_edge(root_node_id,dest_node)
            if subarray[2,1]-root_val<=1:
                dest_node=Graph_dict.loc[(Graph_dict["X"]==orig_row_index+1) & (Graph_dict["Y"]==orig_col_index),"Node_id"].iloc[0]
                G.add_edge(root_node_id,dest_node)
    start_node=Graph_dict.loc[(Graph_dict["X"]==start[0]) & (Graph_dict["Y"]==start[1]),"Node_id"].iloc[0]
    end_node=Graph_dict.loc[(Graph_dict["X"]==end[0]) & (Graph_dict["Y"]==end[1]),"Node_id"].iloc[0]
    paths=dict(nx.single_target_shortest_path_length(G, end_node))

    print(paths.keys())
    min_val=1000
    for a_node in list(Graph_elevation.loc[Graph_elevation["Elevation"]==1,"Node_id"]):
        if a_node in paths.keys():
            if paths[a_node]<min_val:
                min_val=paths[a_node]
    print(min_val)