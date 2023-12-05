from ast import literal_eval

def comp_int(item1,item2):
    
    if item1<item2:
        return "Correct"
    elif item1==item2:
        return "Inconclusive"
    elif item1>item2:
        return "Incorrect"

def comp_lists(list1,list2):
    #print(f"Comparing {list1}, {list2}")
    for item in range(len(list1)):
        try:
            res=choose_next_step(list1[item],list2[item])
        except:
            return "Incorrect"
        else:
            #print(res)
            if not (res=="Inconclusive"):
                return res
    if len(list1)<len(list2):
        return "Correct"
    else:
        return "Inconclusive"

def comp_leftint(int_input,list_input): 
    return comp_lists([int_input],list_input)

def comp_rightint(list_input,int_input): 
    return comp_lists(list_input,[int_input])

def choose_next_step(left,right):
    if type(left)==int and type(right)==int:
        return comp_int(left,right)
    elif type(left)==list and type(right)==list:
        return comp_lists(left,right)
    elif type(left)==int and type(right)==list:
        return comp_leftint(left,right)
    elif type(left)==list and type(right)==int:
        return comp_rightint(left,right)

counter=0
packets=list()
with open("./Day13/input.txt",encoding="utf-8") as f:
    for line in f.readlines():
        
        if counter==0:
            packets.append([eval(line.strip("\n"))])
        elif counter==1:
            packets[-1].append(eval(line.strip("\n")))
            
        
        counter +=1
        if counter==3:
            counter=0


correct_indices_sum=0
packet_index=1
for packet in packets:
    if choose_next_step(packet[0],packet[1])=="Correct":
        correct_indices_sum+=packet_index
        print(packet[0])
        print(packet[1])
        print("Correct")
    else:
        print(packet[0])
        print(packet[1])
        print("Incorrect")
    packet_index+=1

print(correct_indices_sum)



