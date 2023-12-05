import numpy as np
import sys
from time import sleep
with open("./Day14/input.txt",encoding="utf-8") as f:
    canvas=np.zeros((1000,1000),dtype=np.int32)
    minx=1000
    miny=0
    maxx=0
    maxy=0
    for line in f.readlines():
        path=line.strip("\n").split(" -> ")
        path_points=list()
        for step in path:
            x_coord,y_coord=step.split(",")
            x_coord=int(x_coord)
            y_coord=int(y_coord)
            if x_coord>maxx:
                maxx=x_coord
            if x_coord<minx:
                minx=x_coord
            if y_coord>maxy:
                maxy=y_coord

            path_points.append((y_coord,x_coord))

        for step in range(len(path_points)-1):
            if path_points[step][0]==path_points[step+1][0]:
                for offset in range(abs(path_points[step][1]-path_points[step+1][1])+1):
                    if path_points[step][1]>path_points[step+1][1]:
                        canvas[path_points[step][0],path_points[step][1]-offset]=5
                        
                    else:
                        canvas[path_points[step][0],path_points[step][1]+offset]=5
            elif path_points[step][1]==path_points[step+1][1]:
                for offset in range(abs(path_points[step][0]-path_points[step+1][0])+1):
                    if path_points[step][0]>path_points[step+1][0]:
                        canvas[path_points[step][0]-offset,path_points[step][1]]=5
                    else:
                        canvas[path_points[step][0]+offset,path_points[step][1]]=5
    sand_counter=0
    np.set_printoptions(threshold=1000000000)
    print(canvas[miny:(maxy+1),minx:(maxx+1)])
                
    sand_maxy=maxy
    while sand_maxy<=maxy+99:
        sand_loc=(0,500)
        sand_settled=False
        while not sand_settled:
            if sand_loc[0]>sand_maxy+100:
                sand_maxy=sand_loc[0]
                break
            if canvas[sand_loc[0]+1,sand_loc[1]]==0:
                canvas[sand_loc[0]+1,sand_loc[1]]=1
                canvas[sand_loc]=0
                sand_loc=(sand_loc[0]+1,sand_loc[1])
                #print("Fell down")
            elif canvas[sand_loc[0]+1,sand_loc[1]-1]==0:
                canvas[sand_loc[0]+1,sand_loc[1]-1]=1
                canvas[sand_loc]=0
                sand_loc=(sand_loc[0]+1,sand_loc[1]-1)
                #print("Fell down left")
            elif canvas[sand_loc[0]+1,sand_loc[1]+1]==0:
                canvas[sand_loc[0]+1,sand_loc[1]+1]=1
                canvas[sand_loc]=0
                sand_loc=(sand_loc[0]+1,sand_loc[1]+1)
                #print("Fell down right")
            else:
                #print("Settled")
                sand_settled=True
                sand_counter+=1
        print(sand_loc)

    print(sand_counter)
    np.savetxt("test.txt",canvas[miny:maxy,minx:maxx],fmt="%d")
    #np.set_printoptions(threshold=1000000000)
    #print(canvas[miny:maxy,minx:maxx])
                
            