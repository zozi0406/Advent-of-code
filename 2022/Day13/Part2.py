from ast import literal_eval
import functools

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

def comp(packet1,packet2):
    if choose_next_step(packet1,packet2)=="Correct":
        return 1
    else:
        return -1

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
pack1s=[packet[0] for packet in packets]
pack2s=[packet[1] for packet in packets]
pack1s.extend(pack2s)
all_packets=pack1s
all_packets.append([[2]])
all_packets.append([[6]])

sorted_packets=sorted(all_packets,key=functools.cmp_to_key(comp),reverse=True)
print(sorted_packets)
for index, packet in enumerate(sorted_packets):
    if packet == [[2]] or packet==[[6]]:
        print(f"{index+1}: {packet}")





