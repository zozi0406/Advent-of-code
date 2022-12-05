import re

with open("./Day5/input.txt",encoding="utf-8") as f:
    #Setup
    stacks=[list() for x in range(9)]
    stacks[0]=["V","C","W","L","R","M","F","Q"]
    stacks[1]=["L","Q","D"]
    stacks[2]=["B","N","C","W","G","R","S","P"]
    stacks[3]=["G","Q","B","H","D","C","L"]
    stacks[4]=["S","Z","F","L","G","V"]
    stacks[5]=["P","N","G","D"]
    stacks[6]=["W","C","F","V","P","Z","D"]
    stacks[7]=["S","M","D","P","C"]
    stacks[8]=["C","P","M","V","T","W","N","Z"]

    for stack in stacks:
        stack.reverse()
#[V]     [B]                     [C]
#[C]     [N] [G]         [W]     [P]
#[W]     [C] [Q] [S]     [C]     [M]
#[L]     [W] [B] [Z]     [F] [S] [V]
#[R]     [G] [H] [F] [P] [V] [M] [T]
#[M] [L] [R] [D] [L] [N] [P] [D] [W]
#[F] [Q] [S] [C] [G] [G] [Z] [P] [N]
#[Q] [D] [P] [L] [V] [D] [D] [C] [Z]
# 1   2   3   4   5   6   7   8   9 

    for line in f.readlines():
        #move 1 from 9 to 2
        n_move,source_stack,dest_stack = re.findall(r"\s*(\d+)\s*",line)
        print(n_move)
        print(source_stack)
        print(dest_stack)
        to_move=list()
        for iter in range(int(n_move)):
            to_move.append(stacks[int(source_stack)-1].pop())
        to_move.reverse()
        for move in to_move:
            stacks[int(dest_stack)-1].append(move)
        print([stack for stack in stacks])
    print("".join([stack[-1] for stack in stacks]))
    